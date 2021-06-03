import sys,os
from clientwindow import MyMainForm
from database import OperationMysql
from PyQt5.QtWidgets import QApplication, QMainWindow
import threading

def mainThread(op_mysql,serverIP):
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
# try:
    # t = threading.Thread(target=mainThread)
    # t.setDaemon(True)
    # t.start()
    # t.join() # 主进程卡在这等线程执行完毕
# except:
#     print("Error: unable to start thread")

mainThread(op_mysql,serverIP)


