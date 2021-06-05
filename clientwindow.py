
# 导入程序运行必须模块
import sys,os,time
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
# 导入designer工具生成的login模块
# from client.mainWindow  import Ui_MainWindow

import sys,threading,PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings

# from client.main_1 import Ui_MainWindow  # 测试
from client.main import Ui_MainWindow
from register import userRegister
from actuator import actuator
from database import OperationMysql


from client.MatplotlibWidget import MatplotlibWidget
from client.ControlWidget import Ui_Form
from client.PlotWidget import PlotWidget

import cv2

# 是任务栏图标发生改变
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

# argvs = sys.argv
# 支援flash
# argvs.append('--ppapi-flash-path=./pepflashplayer.dll')


# 视频监控部件
class WebEngineView(QWebEngineView):

    def __init__(self):
        super(WebEngineView,self).__init__() 
                # 加载网站网页
        # self.web.load(QUrl("https://www.bilibili.com"))
        # 加载本地网页
        # self.web.load(QUrl("file:.///video.html"))
        'file:///E:/****/test.html'
        # 先读取后设置
        self.webFlag = 0 # 用于判断浏览器功能是否打开
        f = open("video.html",'r',encoding='utf-8')
        self.html = f.read()
        f.close()   
        self.setHtml(self.html)

        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

    def createWindow(self,QWebEnginePage_WebWindowType):
        page = WebEngineView(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    def on_url_changed(self,url):
        self.setUrl(url)

# 首页绘图部件
class PlotForm(QtWidgets.QWidget,PlotWidget): 
    def __init__(self,op_mysql): 
        super(PlotForm,self).__init__() 
        self.setupUi(self)
        self.op_mysql = op_mysql
        self.setUp()

    def setUp(self):
        self.plotCurve = MatplotlibWidget(parent=self,op_mysql=self.op_mysql)        
        self.plotCurve.setContentsMargins(0, 0, 0, 0)

        self.rect = QtCore.QRect(0, 0, 1061, 811)
        self.plotCurve.setGeometry(self.rect) 
        self.plotCurve.show()
        # 实现界面的图片显示
        # 只能在当前文件夹下cv2才好用
        img = cv2.imread("image\shmtu-badge.png")                 #读取图像                                 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)             #转换图像通道
        x = img.shape[1]                                        #获取图像大小
        y = img.shape[0]
        self.zoomscale=1                                        #图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)                      #创建像素图元
        #self.item.setScale(self.zoomscale)
        self.scene=QGraphicsScene()                             #创建场景
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
        try :
            num=float(num)
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
class ControlForm(QtWidgets.QWidget,Ui_Form): 
    def __init__(self,regData,serverIP): 
        super(ControlForm,self).__init__() 
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
            t.setDaemon(True) # 设置线程为守护线程，防止退出主线程时，子线程仍在运行
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def baojingButtonClicked(self):

        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.setDaemon(True)
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def fengjiButtonClicked(self):
        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.setDaemon(True)
            t.start()
            
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def yellowButtonClicked(self):

        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.setDaemon(True)
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def redButtonClicked(self):

        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.setDaemon(True)
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def greenButtonClicked(self):
        self.plotCurve.plotPredicated()
        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.setDaemon(True)
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

# 程序托盘类
class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self,MainWindow,parent=None):
        super(TrayIcon, self).__init__(parent)
        self.ui = MainWindow
        self.createMenu()
    
    def createMenu(self):
        self.menu = QtWidgets.QMenu()
        self.showAction1 = QtWidgets.QAction("启动", self, triggered=self.show_window)
        self.showAction2 = QtWidgets.QAction("显示通知", self,triggered=self.showMsg)
        self.quitAction = QtWidgets.QAction("退出", self, triggered=self.quit)
 
        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)
 
        #设置图标
        self.setIcon(QtGui.QIcon("image/icon1.ico"))
        self.icon = self.MessageIcon()
 
        #把鼠标点击图标的信号和槽连接
        self.activated.connect(self.onIconClicked)
 
    def showMsg(self):
        self.showMessage("Message", "skr at here", self.icon)
 
    def show_window(self):
        #若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
        self.ui.showNormal()
        self.ui.activateWindow()
        
 
    def quit(self):
        QtWidgets.qApp.quit()
 
    #鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
    def onIconClicked(self, reason):
        if reason == 2 or reason == 3:
            # self.showMessage("Message", "skr at here", self.icon)
            if self.ui.isMinimized() or not self.ui.isVisible():
                #若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
                self.ui.showNormal()
                self.ui.activateWindow()
                self.ui.setWindowFlags(QtCore.Qt.Window)
                self.ui.show()
            else:
                #若不是最小化，则最小化
                self.ui.showMinimized()
                self.ui.setWindowFlags(QtCore.Qt.SplashScreen)
                self.ui.show()
                # self.ui.show()


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, op_mysql,regData=None,parent=None, ip="192.168.3.20"):

        # 管廊系统用户信息
        self.regData = regData
        # 数据库信息
        self.op_mysql = op_mysql
        # ip
        self.serverIP = ip

        #将场景添加至视图
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
#####################################################################################

#####################################################################################

        # self.setWindowOpacity(1)
        # 设置 无边框
        # https://blog.csdn.net/kobeyu652453/article/details/108362771?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-5.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-5.control

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("#MainWindow{border-image:url(./image/backgroundark.png);}")
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)

  
        icon = QtGui.QIcon(".\\image\\icon1.ico") 
        self.setWindowIcon(icon)
        self.setWindowTitle("综合管廊客户端")
#####################################################################################

#####################################################################################
        self.rectWeb = QtCore.QRect(10, 100, 1320, 811)
        self.hide = QtCore.QRect(0, 0, 0, 0)
        # 重写部分功能
        # 实现一个堆叠控件用于切换界面
        self.stackedWidget = PyQt5.QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(self.rectWeb)
        # 系统首界面 绘制图形
        self.plotWidget = PlotForm(op_mysql=self.op_mysql)    
        # 视频监控通过web实现
        self.web = WebEngineView() 
        # 控制面板 通过widegt实现
        self.controlWidget = ControlForm(regData=self.regData,serverIP=self.serverIP)        
        # 设备清单 通过widegt实现 现在尚未实现
        self.listWidget = QtWidgets.QWidget(self.stackedWidget)   

        # 实现头部导航栏的按钮样式
        self.homeButton.setStyleSheet('QPushButton{background: transparent;border:0px;font-family:\'楷体\';color:white;}QPushButton:hover{background:#0c3d6b;}')
        self.listButton.setStyleSheet('QPushButton{background: transparent;border:0px;font-family:\'楷体\';color:white;}QPushButton:hover{background:#0c3d6b;}')
        self.controlButton.setStyleSheet('QPushButton{background: transparent;border:0px;font-family:\'楷体\';color:white;}QPushButton:hover{background:#0c3d6b;}')
        self.videoButton.setStyleSheet('QPushButton{background: transparent;border:0px;font-family:\'楷体\';color:white;}QPushButton:hover{background:#0c3d6b;}')
        self.yuzhishezhi.setStyleSheet('QPushButton{background: transparent;border:0px;font-family:\'楷体\';color:white;}QPushButton:hover{background:#0c3d6b;}')
#####################################################################################

#####################################################################################
        # 导航栏
        self.tab = ['系统概述', '设备清单',"远程控制","视频监控","阈值设置"]   
        
        self.stackedWidget.addWidget(self.plotWidget) # 系统概述
        self.plotWidget.show()
        self.stackedWidget.addWidget(self.listWidget) # 设备清单
        self.stackedWidget.addWidget(self.controlWidget) #远程控制
        self.stackedWidget.addWidget(self.web) # 视频监控
        
        self.stackedWidget.setVisible(True)
#####################################################################################
        self.buttonClicked() 

#####################################################################################

    def stackedWidgetThread(self,btn):
        """
        用按钮实现上端导航栏的切换功能
        """
        if btn.text() == "系统概述":
            # self.plotWidget.show()
            self.stackedWidget.setGeometry(self.rectWeb)
        if btn.text() == "设备清单":
            self.stackedWidget.setGeometry(self.rectWeb) 
            # self.listWidget.show()           
        if btn.text() == "远程控制":         
            self.stackedWidget.setGeometry(self.rectWeb)
            # self.controlWidget.show()
        if btn.text() == "视频监控":
            self.stackedWidget.setGeometry(self.rectWeb)     
                  
        self.stackedWidget.setCurrentIndex(self.tab.index(btn.text()))

    def buttonClicked(self):
        
        self.homeButton.clicked.connect(lambda: self.stackedWidgetThread(self.homeButton))
        self.listButton.clicked.connect(lambda: self.stackedWidgetThread(self.listButton))
        self.controlButton.clicked.connect(lambda: self.stackedWidgetThread(self.controlButton))
        self.videoButton.clicked.connect(lambda: self.stackedWidgetThread(self.videoButton))




if __name__ == "__main__":

    # serverIP = "192.168.3.20"
    serverIP = "localhost"
    user = "root"
    # password = "123456" # 服务器数据库密码
    password = "123456" # 本地电脑数据库密码
    database = "pipegallery"
    table = "sensor_data_formated"
    try:
        op_mysql = OperationMysql(
                user=user, password=password, database=database,ip=serverIP)
    except Exception as e:
        print("数据库连接失败")


    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm(op_mysql=op_mysql,ip=serverIP)
    # 将窗口控件显示在屏幕上
    myWin.setStyleSheet("#MainWindow{border-image:url(./image/backgroundark.png);}") 
    # myWin.setStyleSheet("#MainWindow{background-color: #f15a22}")
    # myWin.setStyleSheet("#MainWindow{background-color: #BEE7E9}")
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
