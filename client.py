
#导入程序运行必须模块
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from client.mainWindow  import Ui_MainWindow
from register import userRegister


from actuator import actuator

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None,ip="192.168.3.20"):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # #添加登录按钮信号和槽。注意display函数不加小括号()
        # self.login_Button.clicked.connect(self.display)
        # #添加退出按钮信号和槽。调用close函数
        # self.cancel_Button.clicked.connect(self.close)
        
        self.serverIP=ip
        self.regData = userRegister(ip=self.serverIP)

        # 黄灯 button
        self.yellowButton.clicked.connect(self.yellowButtonClicked)
        self.yellowFlag = 0
        self.yellowButton.setStyleSheet("background-color: gray");

        # 红灯 button
        self.redButton.clicked.connect(self.redButtonClicked)
        self.redFlag = 0
        self.redButton.setStyleSheet("background-color: gray");

        # 绿灯button
        self.greenButton.clicked.connect(self.greenButtonClicked)
        self.greenFlag = 0
        self.greenButton.setStyleSheet("background-color: gray");

        # 风机button
        self.fengji.clicked.connect(self.fengjiButtonClicked)
        self.fengjiFlag = 0
        self.fengji.setStyleSheet("background-color: gray");
        # 报警灯button
        self.baojing.clicked.connect(self.baojingButtonClicked)
        self.baojingFlag = 0
        self.baojing.setStyleSheet("background-color: gray");
        # # 水泵button
        self.shuibeng.clicked.connect(self.shuibengButtonClicked)
        self.shuibengFlag = 0
        self.shuibeng.setStyleSheet("background-color: gray");

    def shuibengButtonClicked(self):
        if self.shuibengFlag:            
            if actuator(actuatorName="水泵", action=0,regData=self.regData,ip=self.serverIP):
                self.shuibengFlag = 0
                print("报警灯已关闭")                
                self.shuibeng.setStyleSheet("background-color: gray")      
            else:
                print("系统未响应")
        else:                    
            if actuator(actuatorName="水泵", action=1,regData=self.regData,ip=self.serverIP):
                self.shuibengFlag = 1
                print("报警灯已打开")                
                self.shuibeng.setStyleSheet("background-color: green")
            else:
                print("系统未响应")                

    def baojingButtonClicked(self):
        if self.baojingFlag:
            
            if actuator(actuatorName="报警灯", action=0,regData=self.regData,ip=self.serverIP):
                self.baojingFlag = 0
                print("报警灯已关闭")                
                self.baojing.setStyleSheet("background-color: gray")
            else:
                print("系统未响应")                            
        else:                    
            if actuator(actuatorName="报警灯", action=1,regData=self.regData,ip=self.serverIP):
                self.baojingFlag = 1
                print("报警灯已打开")                
                self.baojing.setStyleSheet("background-color: green")
            else:
                print("系统未响应")                

    def fengjiButtonClicked(self):
        if self.fengjiFlag:
            
            if actuator(actuatorName="风机", action=0,regData=self.regData,ip=self.serverIP):
                self.fengjiFlag = 0
                print("风机已关闭")                
                self.fengji.setStyleSheet("background-color: gray")
            else:
                print("系统未响应")                             
        else:                    
            if actuator(actuatorName="风机", action=1,regData=self.regData,ip=self.serverIP):
                self.fengjiFlag = 1
                print("风机已打开")                
                self.fengji.setStyleSheet("background-color: green")
            else:
                print("系统未响应")                
    
    def yellowButtonClicked(self):
        if self.yellowFlag:
            
            if actuator(actuatorName="黄灯", action=0,regData=self.regData,ip=self.serverIP):
                self.yellowFlag = 0
                print("黄灯已关闭")                
                self.yellowButton.setStyleSheet("background-color: gray");             
        else:                    
            if actuator(actuatorName="黄灯", action=1,regData=self.regData,ip=self.serverIP):
                self.yellowFlag = 1
                print("黄灯已打开")                
                self.yellowButton.setStyleSheet("background-color: yellow");

    def redButtonClicked(self):
        if self.redFlag:
            
            if actuator(actuatorName="红灯", action=0,regData=self.regData,ip=self.serverIP):
                self.redFlag = 0
                print("红灯已关闭")
                self.redButton.setStyleSheet("background-color: gray") 
            else:
                print("系统未响应")                           
        else:                    
            if actuator(actuatorName="红灯", action=1,regData=self.regData,ip=self.serverIP):
                self.redFlag = 1
                print("红灯已打开")                
                self.redButton.setStyleSheet("background-color: red")
            else:
                print("系统未响应")                

    def greenButtonClicked(self):
        if self.greenFlag:
            
            if actuator(actuatorName="绿灯", action=0,regData=self.regData,ip=self.serverIP):
                self.greenFlag = 0
                print("绿灯已关闭")
                self.greenButton.setStyleSheet("background-color: gray")
            else:
                print("系统未响应")                             
        else:                    
            if actuator(actuatorName="绿灯", action=1,regData=self.regData,ip=self.serverIP):
                self.greenFlag = 1
                print("绿灯已打开")
                self.greenButton.setStyleSheet("background-color: green")
            else:
                print("系统未响应")                



if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    serverIP = "192.168.3.20"
    myWin = MyMainForm(ip=serverIP)
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())


    

    
    