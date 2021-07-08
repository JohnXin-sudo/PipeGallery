# 导入程序运行必须模块
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
import base64
# 是任务栏图标发生改变
import ctypes
import json, time
import sys
import threading
import numpy as np

import PyQt5
# import cv2
from PyQt5 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtGui import *
from PyQt5.QtGui import QImage, QTextDocument, QTextCursor
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication

from client.ControlWidget import Ui_Form
from client.MatplotlibWidget import MatplotlibWidget
from client.PlotWidget import PlotWidget
# from client.main_1 import Ui_MainWindow  # 测试
from client.main import Ui_MainWindow
from utils.actuator import actuator
from utils.database import OperationMysql
from utils.register import userRegister

# 导入designer工具生成的login模块
# from client.mainWindow  import Ui_MainWindow

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


# js调用python的处理类，实现各种js调用的函数
class WebChannelDeal(QObject):
    def __init__(self, op_mysql):
        super().__init__()
        self.op_mysql = op_mysql
        self.historyFlag = 0
        self.predN = 100

    # pyqtSlot槽函数用以处理同名的监听事件
    @pyqtSlot(str, result=str)
    def print_img(self, img_url):
        # 去掉头部的base64标示
        img_url = img_url.replace('data:image/png;base64,', '')
        # 将base64解码成二进制
        url = base64.b64decode(img_url)
        # QImage加载二进制，形成图片流
        image = QImage()
        image.loadFromData(url)
        '''直接输出打印到pdf'''
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName('./testfile/test.pdf')
        # 实例化一个富文本
        document = QTextDocument()
        cursor = QTextCursor(document)
        cursor.insertImage(image)
        # 调用print（）方法 参数为当前实例化的打印函数
        document.print(printer)
        return 'sucess'  # 处理成功传回success，返回信息被js回调函数处理

    @pyqtSlot(str, result=str)
    def jsPrint(self, message):
        print(message)

    @pyqtSlot(str, result=str)
    def getData(self, js):
        return self.plotThread(js)

    def plotThread(self, js):
        # print("js arguments: " + js)
        jsData = json.loads(js)
        id = int(jsData['id'])
        windowsize = int(jsData['windowsize'])
        # plotSpeed = int(jsData['plotSpeed'])
        plotType = jsData['plotType']
        step = 1
        if 200 < windowsize <= 400:
            step = 2
        elif 400 < windowsize <= 800:
            step = 4
        elif 800 < windowsize <= 1600:
            step = 8
        elif 1600 < windowsize <= 3200:
            step = 16
        elif 3200 < windowsize <= 6400:
            step = 32
        elif 6400 < windowsize <= 12800:
            step = 64
        elif 12800 < windowsize <= 25600:
            step = 128
        elif 25600 < windowsize <= 51200:
            step = 256
        elif 51200 < windowsize <= 102400:
            step = 512
        elif 102400 < windowsize <= 204800:
            step = 1024
        _, dataWindow, index = self.op_mysql.getData(
            id=id, window_size=windowsize, step=step)
        print(dataWindow.shape)

        ph4 = dataWindow[:, 0].tolist()
        temperature = dataWindow[:, 1].tolist()
        humility = dataWindow[:, 2].tolist()
        o2 = dataWindow[:, 3].tolist()
        t = []
        for x in index:
            t.append(x.strftime('%H:%M:%S'))

        data = {'x': t, 'ph4': ph4, 'temperature': temperature, "humility": humility, 'o2': o2}
        return json.dumps(data)


# 视频监控部件
class WebEngineView(QWebEngineView):
    # TODO pyqt python与js的互相调用还是很有意思的，想一个好的互动方式
    def __init__(self):
        super(WebEngineView, self).__init__()

        # self.load(QUrl('file:///./html/index.html'))
        self.load(QUrl('file:///./html/video.html'))
        # self.load(QUrl('https://www.iotclient.com/platform/index.php'))

        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)  # 隐藏滚动条

    # 实现页面内部网页跳转
    def createWindow(self, QWebEnginePage_WebWindowType):
        page = WebEngineView(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    def on_url_changed(self, url):
        self.setUrl(url)


# 首页绘图功能由网页端实现
class PlotWebView(QWebEngineView):
    def __init__(self, op_mysql):
        super(PlotWebView, self).__init__()

        self.load(QUrl('file:///./html/index.html'))

        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)  # 隐藏滚动条
        # 实现js调用python代码
        self.channel = QWebChannel()
        self.webChannelDeal = WebChannelDeal(op_mysql=op_mysql)
        self.channel.registerObject('pyjs', self.webChannelDeal)
        self.page().setWebChannel(self.channel)

        self.op_mysql = op_mysql
        self.i = 370
        self.historyFlag = 0
        self.predN = 100



    # 实现页面内部网页跳转
    def createWindow(self, QWebEnginePage_WebWindowType):
        page = WebEngineView(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    def on_url_changed(self, url):
        self.setUrl(url)

    # python调用js的回调函数
    def js_callback(self, result):
        print(result)

    # python调用js的函数
    def call_Js(self, value):
        # 向js中传值
        print('pythonCallJs("' + value + '");')
        # self.page().runJavaScript('pythonCallJs("' + value + '");', self.js_callback)
        # self.page().runJavaScript("pythonCallJs({});".format(value),
        #                           self.js_callback)  # 第一个参数是调用html中js。第二个参数是js的返回值  。注意：第一个参数有传值的话，一定有双引号

    def forHsitoryThreadsFunction(self, window_size=50, speed=0.1):
        while True:
            window_size = self.predN
            if self.historyFlag == 0:
                return

            _, dataWindow, index = self.op_mysql.getData(
                id=self.i, window_size=window_size)

            ph4 = dataWindow[:, 0].tolist()
            temperature = dataWindow[:, 1].tolist()
            humility = dataWindow[:, 2].tolist()
            o2 = dataWindow[:, 3].tolist()
            t = []
            for time in index:
                t.append(time.strftime('%H:%M:%S'))

            data = {'x': t, 'ph4': ph4, 'temperature': temperature, "humility": humility, 'o2': o2}
            data = json.dumps(data)
            self.i += 1

            # self.call_Js(data)
            print (data)

            time.sleep(self.historySpeed)
            # print("数据更新！")

    def plotHistory(self, window_size=50, speed=0.1):
        # 防止线程冲突
        if self.historyFlag == 1:
            self.historyFlag = 0
            time.sleep(1)

        self.historyFlag = 1
        t = threading.Thread(
            target=self.forHsitoryThreadsFunction, args=(window_size, speed))
        t.setDaemon(True)  # 设置线程为守护线程，防止退出主线程时，子线程仍在运行
        t.start()


# 首页绘图部件
class PlotForm(QtWidgets.QWidget, PlotWidget):
    def __init__(self, op_mysql):
        super(PlotForm, self).__init__()
        self.setupUi(self)
        self.op_mysql = op_mysql
        self.setUp()  # TODO 我真是服了QT的布局功能，或许是我不会用吧

    def setUp(self):
        self.plotCurve = MatplotlibWidget(parent=self, op_mysql=self.op_mysql)
        self.plotCurve.setContentsMargins(0, 0, 0, 0)

        self.rect = QtCore.QRect(0, 0, 1061, 811)
        self.plotCurve.setGeometry(self.rect)
        self.plotCurve.show()
        # 实现界面的图片显示
        # 只能在当前文件夹下cv2才好用
        img = cv2.imread("image\A.jpg")  # 读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]

        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)  # 创建像素图元

        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(item)

        self.graphicsView.setScene(self.scene)

        self.graphicsView.setStyleSheet("background: transparent;border:0px")
        self.graphicsView.setHorizontalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)
        self.label.setStyleSheet("color:white")
        self.label_2.setStyleSheet("color:white")
        self.label_3.setStyleSheet("color:white")

        self.plotCurve.setStyleSheet("background: transparent;border:0px")

        self.startrealtimeplot.clicked.connect(self.startRealTimePlot)
        self.stoprealtimeplot.clicked.connect(self.stopRealTimePlot)
        self.starthistoryplot.clicked.connect(self.startHistoryPlot)
        self.stophistoryplot.clicked.connect(self.stopHistoryPlot)
        self.startpredict.clicked.connect(self.startpredictPlot)
        self.stoppredict.clicked.connect(self.stoppredictPlot)
        self.stopplot.clicked.connect(self.stopPlot)

        self.historycommitbutton.clicked.connect(self.historyCommit)
        self.speedCommitbutton.clicked.connect(self.speedCommit)
        self.idcommitbutton.clicked.connect(self.idCommit)

    def stopPlot(self):
        self.plotCurve.stopPlotPredicated()
        self.plotCurve.stopPlotRealTime()
        self.plotCurve.stopPlot()

    def historyCommit(self):
        num = self.historyinput.text()
        if not num.isdigit():
            print("输入整形")
            return
        print(num)

        # self.plotCurve.stopPlot()
        print("显示数据数量改变")
        self.plotCurve.changePredN(N=int(num))
        # self.plotCurve.plot(window_size=int(num))
        pass

    def speedCommit(self):
        num = self.speedinput.text()
        try:
            num = float(num)
        except Exception:
            print("输入数字")
            return
        print(num)
        print("显示数据速度改变")
        self.plotCurve.changeSpeed(speed=num)

    def idCommit(self):
        num = self.idinput.text()
        if not num.isdigit():
            print("输入整形")
            return
        print(num)

        print("显示数据位置改变")
        self.plotCurve.changeId(id=int(num))

    def startpredictPlot(self):
        print("显示预测数据")
        self.plotCurve.plotPredicated()

    def stoppredictPlot(self):
        self.plotCurve.stopPlotPredicated()
        print("停止预测数据")

    def startRealTimePlot(self):
        print("显示实时数据")
        self.plotCurve.plotRealTime(self.op_mysql)

    def stopRealTimePlot(self):
        self.plotCurve.stopPlotRealTime()
        print("停止实时数据")

    def startHistoryPlot(self):
        print("显示历史数据")
        self.plotCurve.plot(window_size=1000)

    def stopHistoryPlot(self):
        self.plotCurve.stopPlot()
        print("停止历史数据")


# control Form 部件类 通过qtdesigner设计 
# TODO 建立了简易界面与核心功能实现还需要美化界面
class ControlForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self, regData, serverIP):
        super(ControlForm, self).__init__()
        self.setupUi(self)
        self.regData = regData
        self.serverIP = serverIP
        self.setUp()

    def setUp(self):
        # 黄灯 button
        self.yellowButton.clicked.connect(self.yellowButtonClicked)
        self.yellowFlag = 0
        self.yellowButton.setStyleSheet("background-color: gray")

        # 红灯 button
        self.redButton.clicked.connect(self.redButtonClicked)
        self.redFlag = 0
        self.redButton.setStyleSheet("background-color: gray")

        # 绿灯button
        self.greenButton.clicked.connect(self.greenButtonClicked)
        self.greenFlag = 0
        self.greenButton.setStyleSheet("background-color: gray")

        # 风机button
        self.fengji.clicked.connect(self.fengjiButtonClicked)
        self.fengjiFlag = 0
        self.fengji.setStyleSheet("background-color: gray")
        # 报警灯button
        self.baojing.clicked.connect(self.baojingButtonClicked)
        self.baojingFlag = 0
        self.baojing.setStyleSheet("background-color: gray")
        # # # 水泵button
        self.shuibeng.clicked.connect(self.shuibengButtonClicked)
        self.shuibengFlag = 0
        self.shuibeng.setStyleSheet("background-color: gray")

    def nameFlag(self, nameCN, action=-1):
        if nameCN == "水泵":
            if action == 1:
                self.shuibengFlag = 1
                self.shuibeng.setStyleSheet("background-color: green")
            elif action == 0:
                self.shuibengFlag = 0
                self.shuibeng.setStyleSheet("background-color: gray")
            return self.shuibengFlag
        elif nameCN == "风机":
            if action == 1:
                self.fengjiFlag = 1
                self.fengji.setStyleSheet("background-color: green")
            elif action == 0:
                self.fengjiFlag = 0
                self.fengji.setStyleSheet("background-color: gray")
            return self.fengjiFlag
        elif nameCN == "报警灯":
            if action == 1:
                self.baojingFlag = 1
                self.baojing.setStyleSheet("background-color: green")
            elif action == 0:
                self.baojingFlag = 0
                self.baojing.setStyleSheet("background-color: gray")
            return self.baojingFlag
        elif nameCN == "红灯":
            if action == 1:
                self.redFlag = 1
                self.redButton.setStyleSheet("background-color: green")
            elif action == 0:
                self.redFlag = 0
                self.redButton.setStyleSheet("background-color: gray")
            return self.redFlag
        elif nameCN == "黄灯":
            if action == 1:
                self.yellowFlag = 1
                self.yellowButton.setStyleSheet("background-color: green")
            elif action == 0:
                self.yellowFlag = 0
                self.yellowButton.setStyleSheet("background-color: gray")
            return self.yellowFlag
        elif nameCN == "绿灯":
            if action == 1:
                self.greenFlag = 1
                self.greenButton.setStyleSheet("background-color: green")
            elif action == 0:
                self.greenFlag = 0
                self.greenButton.setStyleSheet("background-color: gray")
            return self.greenFlag

    def threadsFunction(self, nameCN):
        print(threading.current_thread().name)
        flag = self.nameFlag(nameCN)
        if flag:
            if actuator(actuatorName=nameCN, action=0, regData=self.regData, ip=self.serverIP):
                self.nameFlag(nameCN, action=0)
                print("{0}已关闭".format(nameCN))

            else:
                print("系统未响应")
        else:
            if actuator(actuatorName=nameCN, action=1, regData=self.regData, ip=self.serverIP):
                self.nameFlag(nameCN, action=1)
                # self.shuibengFlag = 1
                print("{0}已开启".format(nameCN))
            else:
                print("系统未响应")

    def shuibengButtonClicked(self):
        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.setDaemon(True)  # 设置线程为守护线程，防止退出主线程时，子线程仍在运行
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def baojingButtonClicked(self):

        try:
            t = threading.Thread(target=self.threadsFunction, args=("报警灯",))
            t.setDaemon(True)
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def fengjiButtonClicked(self):
        try:
            t = threading.Thread(target=self.threadsFunction, args=("风机",))
            t.setDaemon(True)
            t.start()

            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def yellowButtonClicked(self):

        try:
            t = threading.Thread(target=self.threadsFunction, args=("黄灯",))
            t.setDaemon(True)
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def redButtonClicked(self):

        try:
            t = threading.Thread(target=self.threadsFunction, args=("红灯",))
            t.setDaemon(True)
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def greenButtonClicked(self):

        try:
            t = threading.Thread(target=self.threadsFunction, args=("绿灯",))
            t.setDaemon(True)
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")


# 程序托盘类 
# TODO 还需要实现这个功能
class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, MainWindow, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.ui = MainWindow
        self.createMenu()

    def createMenu(self):
        self.menu = QtWidgets.QMenu()
        self.showAction1 = QtWidgets.QAction("启动", self, triggered=self.show_window)
        self.showAction2 = QtWidgets.QAction("显示通知", self, triggered=self.showMsg)
        self.quitAction = QtWidgets.QAction("退出", self, triggered=self.quit)

        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

        # 设置图标
        self.setIcon(QtGui.QIcon("image/icon1.ico"))
        self.icon = self.MessageIcon()

        # 把鼠标点击图标的信号和槽连接
        self.activated.connect(self.onIconClicked)

    def showMsg(self):
        self.showMessage("Message", "skr at here", self.icon)

    def show_window(self):
        # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
        self.ui.showNormal()
        self.ui.activateWindow()

    def quit(self):
        QtWidgets.qApp.quit()

    # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
    def onIconClicked(self, reason):
        if reason == 2 or reason == 3:
            # self.showMessage("Message", "skr at here", self.icon)
            if self.ui.isMinimized() or not self.ui.isVisible():
                # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
                self.ui.showNormal()
                self.ui.activateWindow()
                self.ui.setWindowFlags(QtCore.Qt.Window)
                self.ui.show()
            else:
                # 若不是最小化，则最小化
                self.ui.showMinimized()
                self.ui.setWindowFlags(QtCore.Qt.SplashScreen)
                self.ui.show()
                # self.ui.show()


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, op_mysql, regData=None, parent=None, ip="192.168.3.20"):

        # 管廊系统用户信息
        self.regData = regData
        # 数据库信息
        self.op_mysql = op_mysql
        # ip
        self.serverIP = ip

        # 将场景添加至视图
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        #####################################################################################

        #####################################################################################

        self.setWindowOpacity(1)
        # 设置 无边框
        # https://blog.csdn.net/kobeyu652453/article/details/108362771?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-5.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-5.control

        self.setStyleSheet("#MainWindow{border-image:url(./image/backgroundark.png);}")
        # self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        # self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        icon = QtGui.QIcon(".\\image\\icon.ico")
        self.setWindowIcon(icon)
        self.setWindowTitle("综合管廊客户端")
        #####################################################################################

        #####################################################################################
        self.rectWeb = QtCore.QRect(10, 80, 1341, 871)
        self.hide = QtCore.QRect(0, 0, 0, 0)
        # 重写部分功能
        # 实现一个堆叠控件用于切换界面
        self.stackedWidget = PyQt5.QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(self.rectWeb)
        # # 系统首界面 绘制图形
        # self.plotWidget = PlotForm(op_mysql=self.op_mysql)
        # 系统首界面，通过web实现 与上一种选一种方式即可
        self.plotWidget = PlotWebView(op_mysql=self.op_mysql)
        # 视频监控通过web实现
        self.web = WebEngineView()
        # 控制面板 通过widget实现
        self.controlWidget = ControlForm(regData=self.regData, serverIP=self.serverIP)
        # 设备清单 通过widget实现 现在尚未实现
        self.listWidget = QWebEngineView()
        self.listWidget.load(QUrl("file:///D:/桌面/PipeGallery/html/list/list.html"))
        # 阈值设置
        self.threshold = QWebEngineView()
        self.threshold.load(QUrl("file:///D:/桌面/PipeGallery/html/yuzhishezhi/threshold.html"))

        # 实现头部导航栏的按钮样式
        self.homeButton.setStyleSheet(
            'QPushButton{background: transparent;border-radius:8px;border:0px;font-family:\'楷体\';color:white'
            ';}QPushButton:hover{background:rgb(44 , 137 , 255);}')
        self.listButton.setStyleSheet(
            'QPushButton{background: transparent;border-radius:8px;border:0px;font-family:\'楷体\';color:white'
            ';}QPushButton:hover{background:rgb(44 , 137 , 255);}')
        self.controlButton.setStyleSheet(
            'QPushButton{background: transparent;border-radius:8px;border:0px;font-family:\'楷体\';color:white'
            ';}QPushButton:hover{background:rgb(44 , 137 , 255);}')
        self.videoButton.setStyleSheet(
            'QPushButton{background: transparent;border-radius:8px;border:0px;font-family:\'楷体\';color:white'
            ';}QPushButton:hover{background:rgb(44 , 137 , 255);}')
        self.yuzhishezhi.setStyleSheet(
            'QPushButton{background: transparent;border-radius:8px;border:0px;font-family:\'楷体\';color:white'
            ';}QPushButton:hover{background:rgb(44 , 137 , 255);}')
        #####################################################################################

        #####################################################################################
        # 导航栏
        self.tab = ['系统概述', '设备清单', "远程控制", "视频监控", "阈值设置"]

        self.stackedWidget.addWidget(self.plotWidget)  # 系统概述
        self.plotWidget.show()
        self.stackedWidget.addWidget(self.listWidget)  # 设备清单
        self.stackedWidget.addWidget(self.controlWidget)  # 远程控制
        self.stackedWidget.addWidget(self.web)  # 视频监控
        self.stackedWidget.addWidget(self.threshold)  # 视频监控

        self.stackedWidget.setVisible(True)
        #####################################################################################
        self.buttonClicked()


        #####################################################################################

    def stackedWidgetThread(self, btn):
        """
        用按钮实现上端导航栏的切换功能
        """
        if btn.text() == "系统概述":
            pass
            self.plotWidget.show()
            self.stackedWidget.setGeometry(self.rectWeb)
        if btn.text() == "设备清单":
            pass
            self.stackedWidget.setGeometry(self.rectWeb)
            self.listWidget.show()
        if btn.text() == "远程控制":
            pass
            self.stackedWidget.setGeometry(self.rectWeb)
            self.controlWidget.show()
        if btn.text() == "视频监控":
            self.web.show()
            pass
            self.stackedWidget.setGeometry(self.rectWeb)
        if btn.text() == "阈值设置":
            self.stackedWidget.setGeometry(self.rectWeb)
            self.yuzhishezhi.show()
            pass

        self.stackedWidget.setCurrentIndex(self.tab.index(btn.text()))

    def buttonClicked(self):

        self.homeButton.clicked.connect(lambda: self.stackedWidgetThread(self.homeButton))
        self.listButton.clicked.connect(lambda: self.stackedWidgetThread(self.listButton))
        # self.listButton.clicked.connect(lambda: self.web.call_Js())

        self.controlButton.clicked.connect(lambda: self.stackedWidgetThread(self.controlButton))
        self.videoButton.clicked.connect(lambda: self.stackedWidgetThread(self.videoButton))
        self.yuzhishezhi.clicked.connect(lambda: self.stackedWidgetThread(self.yuzhishezhi))


if __name__ == "__main__":

    # serverIP = "192.168.3.20"
    serverIP = "localhost"
    user = "root"
    # password = "123456" # 服务器数据库密码
    password = "123456"  # 本地电脑数据库密码
    database = "pipegallery"
    table = "sensor_data_formated"
    try:
        op_mysql = OperationMysql(
            user=user, password=password, database=database, ip=serverIP)
    except Exception as e:
        print("数据库连接失败")

    #  用户注册
    regData = None
    # try:
    #     regData = userRegister(ip=serverIP)
    #     print(regData)
    # except Exception:
    #     print("用户信息获取失败")

    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm(op_mysql=op_mysql, ip=serverIP, regData=regData)
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
