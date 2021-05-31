
# 导入程序运行必须模块
import sys
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
# 导入designer工具生成的login模块
# from client.mainWindow  import Ui_MainWindow

from client.main_1 import Ui_MainWindow  # 测试


from register import userRegister
import threading

from actuator import actuator
from database import OperationMysql


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, ip="192.168.3.20"):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        # self.setWindowOpacity(1)
        # 设置 无边框
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setStyleSheet(
        #     "#MainWindow{border-image:url(./image/backgroundark.png);}")
        # self.setWindowIcon(QtGui.QIcon("./images/icon.png"))
        self.setWindowTitle("综合管廊客户端")

        self.serverIP = ip
        self.regData = userRegister(ip=self.serverIP)

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


        self.historycommitbutton.clicked.connect(self.historyCommit)
        self.speedCommitbutton.clicked.connect(self.speedCommit)
        self.idcommitbutton.clicked.connect(self.idCommit)

        # 1. 用户注册
        self.serverIP = "192.168.3.20"
        self.regData = userRegister(ip=serverIP)
        # 数据库信息
        user = "root"
        password = "123456"
        database = "pipegallery"
        table = "sensor_data_formated"

        self.op_mysql = OperationMysql(
            user=user, password=password, database=database)

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
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def baojingButtonClicked(self):

        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def fengjiButtonClicked(self):
        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def yellowButtonClicked(self):

        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def redButtonClicked(self):

        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")

    def greenButtonClicked(self):
        self.plotCurve.plotPredicated()
        try:
            t = threading.Thread(target=self.threadsFunction, args=("水泵",))
            t.start()
            # t.join() # 主进程卡在这等线程执行完毕
        except:
            print("Error: unable to start thread")


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    serverIP = "192.168.3.20"
    # myWin = MyMainForm(ip=serverIP)
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上

    # myWin.setStyleSheet("#MainWindow{border-image:url(./image/backgroundark.png);}") 
    # myWin.setStyleSheet("#MainWindow{background-color: #f15a22}")

    myWin.setStyleSheet("#MainWindow{background-color: #BEE7E9}")

    myWin.show()

    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
