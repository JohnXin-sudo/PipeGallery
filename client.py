
# 导入程序运行必须模块
import sys
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

import cv2


# argvs = sys.argv
# 支援flash
# argvs.append('--ppapi-flash-path=./pepflashplayer.dll')
class WebEngineView(QWebEngineView):
    def createWindow(self,QWebEnginePage_WebWindowType):
        page = WebEngineView(self)
        page.urlChanged.connect(self.on_url_changed)
        return page
    def on_url_changed(self,url):
        self.setUrl(url)


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, op_mysql,parent=None, ip="192.168.3.20"):


        # 1. 用户注册
        # try :
        #     self.serverIP = ip
        #     self.regData = userRegister(ip=serverIP)
        # except Exception:
        #     print("用户信息获取失败")

        # 数据库信息
        self.op_mysql = op_mysql
                     #将场景添加至视图
 



        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)



        # self.setWindowOpacity(1)
        # 设置 无边框
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setStyleSheet(
            # "#MainWindow{border-image:url(./image/backgroundark.png);}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\images\\icon.png"),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon = QtGui.QIcon(".\\images\\icon.ico") 
        self.setWindowIcon(icon)
        self.setWindowTitle("综合管廊客户端")


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
#####################################################################################

        self.rect = QtCore.QRect(10, 100, 1061, 811)
        self.rectWeb = QtCore.QRect(10, 100, 1320, 811)

        # 重写部分功能
        self.stackedWidget = PyQt5.QtWidgets.QStackedWidget(self.centralwidget)
        # 0, 90, 1261, 901
        self.stackedWidget.setGeometry(QtCore.QRect(10, 100, 1061, 811))

        self.plotpannel = QtWidgets.QWidget(self.stackedWidget)
        # self.plotpannel.setGeometry(QtCore.QRect(10, 100, 1061, 811))
        self.plotpannel.setObjectName("plotpannel")        

        self.plotCurve = MatplotlibWidget(parent=self.plotpannel, op_mysql=self.op_mysql)
        self.plotCurve.setContentsMargins(0, 0, 0, 0)        
        
        self.web = WebEngineView(self.stackedWidget)   

        self.controlGridLayout = QtWidgets.QWidget(self.stackedWidget)
        self.controlGridLayout.setGeometry(QtCore.QRect(10, 100, 1061, 811))
        self.controlGridLayout.setObjectName("controlGridLayout")      
        self.controlGridLayout.setVisible(False)
        # self.controlGridLayout.
        img = cv2.imread("image\icon.png")                 #读取图像                                 
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


        self.homeButton.setStyleSheet('QPushButton{background: transparent;border:0px;font-family:\'楷体\';color:white;}QPushButton:hover{background:blue;}')
        self.listButton.setStyleSheet('QPushButton{background: transparent;border:0px;font-family:\'楷体\';color:white;}QPushButton:hover{background:blue;}')
        self.controlButton.setStyleSheet('QPushButton{background: transparent;border:0px;font-family:\'楷体\';color:white;}QPushButton:hover{background:blue;}')
        self.videoButton.setStyleSheet('QPushButton{background: transparent;border:0px;font-family:\'楷体\';color:white;}QPushButton:hover{background:blue;}')
        self.yuzhishezhi.setStyleSheet('QPushButton{background: transparent;border:0px;font-family:\'楷体\';color:white;}QPushButton:hover{background:blue;}')


        self.label.setStyleSheet("color:white")
        self.label_2.setStyleSheet("color:white")
        self.label_3.setStyleSheet("color:white")


        self.plotCurve.setStyleSheet("background: transparent;border:0px") 


   
#####################################################################################

#####################################################################################
        # 导航栏
        self.tab = ['系统概述', '设备清单',"远程控制","视频监控","阈值设置"]   

        self.stackedWidget.addWidget(self.plotCurve)
        self.stackedWidget.addWidget(self.web)

        # 网页
        self.web.load(QUrl("https://www.bilibili.com/video/BV1T5411M7pk"))
        self.web.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.web.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)


       

        
        try:
            t = threading.Thread(target=lambda: self.web.show())
            t.setDaemon(True) # 设置线程为守护线程，防止退出主线程时，子线程仍在运行
            t.start()
        except Exception:
            print("浏览器线程启动失败")
        
#####################################################################################

        # homeButton listButton
        self.homeButton.clicked.connect(lambda: self.update_(self.homeButton))
        self.listButton.clicked.connect(lambda: self.update_(self.listButton))

        
#####################################################################################



    def update_(self,btn):
        """
        用按钮实现上端导航栏的切换功能
        """
        if btn.text() == "设备清单":
            self.stackedWidget.setGeometry(self.rectWeb)
            pass
            # self.listButton.setStyleSheet("background-color: gray")
        elif btn.text() == "系统概述":
            self.stackedWidget.setGeometry(self.rect)
            
        # print(btn.text)    
        self.stackedWidget.setCurrentIndex(self.tab.index(btn.text()))

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
