from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QSizePolicy, QWidget
from database import OperationMysql
import matplotlib.animation as animation
import matplotlib.lines as line
import queue
import threading
import time
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore
import sys
import matplotlib


import random

matplotlib.use("Qt5Agg")


# 绘图逻辑需要的库


sys.path.append("..")


# 数据库信息
user = "root"
password = "123456"
database = "pipegallery"
table = "sensor_data_formated"

op_mysql = OperationMysql(user=user, password=password, database=database)


tempId = 0


def plotHistory():

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体，不然中文无法显示
    plt.rcParams['figure.figsize'] = (18.0, 14.0)
    plt.rcParams['image.cmap'] = 'gray'
    plt.rcParams['image.interpolation'] = 'nearest'  # 设置 interpolation style
    plt.rcParams.update({'font.size': 14})

    for i in range(5000):

        tempId, dataWindow, index = op_mysql.getData(
            table=table, id=i+1, window_size=50)

        ph4 = dataWindow[:, 0]
        temperture = dataWindow[:, 1]
        humility = dataWindow[:, 2]
        o2 = dataWindow[:, 3]

        plt.ion()

        plt.clf()  # 清除之前画的图

        ax1 = plt.subplot(221)
        plt.plot(index, ph4, 'bo--', label="甲烷")  # o
        # ax1.set_xlabel("甲烷",fontsize=16)
        ax1.legend()
        plt.grid()
        plt.xticks(rotation=25)
        plt.ylim(-5, 60)

        ax2 = plt.subplot(222)
        plt.plot(index, temperture, 'rd--', label="温度")  # d
        # ax2.set_xlabel("温度",fontsize=16)
        ax2.legend()
        plt.grid()
        plt.xticks(rotation=25)

        ax3 = plt.subplot(223)
        plt.plot(index, humility, "yd--", label="湿度")  # d
        # ax3.set_xlabel("湿度",fontsize=16)
        ax3.legend()
        plt.grid()
        plt.xticks(rotation=25)

        ax4 = plt.subplot(224)
        plt.plot(index, o2, "go--", label="氧气")  # o
        # ax4.set_xlabel("氧气",fontsize=16)
        ax4.legend()
        plt.grid()  # 坐标网格
        plt.xticks(rotation=25)
        plt.ylim(20.5, 21.5)

        plt.suptitle('地下综合管廊智慧管控平台', fontsize=24, color='b')

        plt.ioff()  # 关闭画图窗口
        # plt.pause (0.01)  # 这个为停顿0.01s，能得到产生实时的效

# def plotTest():


# 这是一些与音频信号有关的常量
CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100


class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=6, height=4, dpi=100):
        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体，不然中文无法显示
        # plt.rcParams['figure.figsize'] = (18.0, 14.0)
        # plt.rcParams['image.cmap'] = 'gray'
        # plt.rcParams['image.interpolation'] = 'nearest'  # 设置 interpolation style
        # plt.rcParams.update({'font.size': 14})

        self.fig = plt.Figure(figsize=(width, height), dpi=dpi)
        self.axe1 = self.fig.add_subplot(221)
        self.axe2 = self.fig.add_subplot(222)
        self.axe3 = self.fig.add_subplot(223)
        self.axe4 = self.fig.add_subplot(224)
        # self.axes.hold(False)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self,
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)

        self.i = 1 # 历史数据计数用
        self.historyFlag = 0
        self.realtimeFlag =0


        # 下面这种方法太卡了
        # self.timer = QtCore.QTimer(self)
        # self.timer.timeout.connect(self.update_figure)


    # def start_dynamic_plot(self, *args, **kwargs):
    #     self.historyFlag = 1
    #     self.timer.start(1000)

    # def stop_dynamic_plot(self, *args, **kwargs):
    #     # self.timer.stop()
    #     self.historyFlag = 0
#######################################################################
    def xtickRotion(self, xticks, rotation=25):
        for tick in xticks:
            tick.set_rotation(rotation)

    def plot(self, index, dataWindow):

        ph4 = dataWindow[:, 0]
        temperture = dataWindow[:, 1]
        humility = dataWindow[:, 2]
        o2 = dataWindow[:, 3]

        self.axe1.clear()
        self.axe2.clear()
        self.axe3.clear()
        self.axe4.clear()

        self.axe1.plot(index, ph4, 'bo--', label="甲烷")

        self.axe1.grid(True)
        self.axe1.legend()
        self.xtickRotion(self.axe1.get_xticklabels())  # 设置坐标倾斜

        self.axe2.plot(index, temperture, 'rd--', label="温度")
        self.axe2.grid(True)
        self.axe2.legend()
        self.xtickRotion(self.axe2.get_xticklabels())  # 设置坐标倾斜

        self.axe3.plot(index, humility, "yd--", label="湿度")
        self.axe3.grid(True)
        self.axe3.legend()
        self.xtickRotion(self.axe3.get_xticklabels())  # 设置坐标倾斜

        self.axe4.plot(index, o2, "go--", label="氧气")
        self.axe4.grid(True)
        self.axe4.legend()
        self.xtickRotion(self.axe4.get_xticklabels())  # 设置坐标倾斜
        self.draw()
#######################################################################

#######################################################################
    def plotHistory(self, window_size):
        tempId, dataWindow, index = op_mysql.getData(
             id=self.i+1, window_size=window_size)
        self.plot(index, dataWindow)

    def forHsitoryThreadsFunction(self,window_size=50,speed=0.1):
        while True:
            if self.historyFlag == 0:
                return

            self.update_figure(window_size=window_size)
            time.sleep(speed)
            # print("数据更新！")
          
    def plotDynamicHistory(self,window_size=50,speed=0.1):
        # 防止线程冲突
        if self.historyFlag == 1:
            self.historyFlag =0
            time.sleep(1)
            
        self.historyFlag = 1
        t = threading.Thread(target=self.forHsitoryThreadsFunction,args=(window_size,speed))
        t.start()
    
    def stopplotDynamicHistory(self, *args, **kwargs):
        # self.timer.stop()
        self.historyFlag = 0
        time.sleep(1)
#######################################################################

#######################################################################
    def update_figureForRealtime(self, id,op_mysql, window_size=50):
        tempId, dataWindow, index = op_mysql.getData(
            id=id, window_size=window_size)
        self.plot(index, dataWindow)

    def forRealTimeThreadsFunction(self,op_mysql):
        # 防止线程冲突
        if self.realtimeFlag == 1:
            self.realtimeFlag =0
            time.sleep(1)

        tempId = op_mysql.last_record(table=table, item_id="id")
        currentTime = time.time()
        self.realtimeFlag = 1

        self.update_figure() # 测试用

        while True:
            if self.realtimeFlag == 0:
                break
            if time.time()-currentTime > 10:
                print("实时数据查询超时")
                return 0
            latestId = op_mysql.last_record(table=table, item_id="id")
            if latestId > tempId:
                self.update_figureForRealtime(id=latestId-50+1,op_mysql=op_mysql,window_size=50)
                continue
            else:
                tempId = latestId
                time.sleep(0.5)  # 暂停一段时间，不然画的太快会卡住显示不出
    
    def plotRealTime(self, op_mysql):
        t = threading.Thread(target=self.forRealTimeThreadsFunction,args=(op_mysql,))
        t.start()
    
    def stopPlotRealTime(self):
        self.realtimeFlag = 0
        time.sleep(1)
#######################################################################
        

#######################################################################
    def update_figure(self,window_size=50):
        tempId, dataWindow, index = op_mysql.getData(
             id=self.i+1, window_size=window_size)
        self.i += 1

        self.plot(index, dataWindow)


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        # self.setWindowIcon(QIcon("./images/Python2.ico"))
        # self.setWindowTitle("Matplotlib of PyQt5")

        self.layout = QVBoxLayout(self)
        # self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        # 0, 80, 1261, 901
        self.mpl = MyMplCanvas(self, width=12, height=8, dpi=100)
        # self.mpl_ntb = NavigationToolbar(self.mpl, self)

        self.layout.addWidget(self.mpl)
        # self.layout.addWidget(self.mpl_ntb)
        # self.initariateV()

    def plot(self,window_size=50):
        # self.mpl.start_dynamic_plot() # 使用Qt Timer
        self.mpl.plotDynamicHistory(window_size) # 使用thread

    def stopPlot(self):
        self.mpl.stopplotDynamicHistory(speed=0.1)
    
    def plotRealTime(self,op_mysql):
        self.mpl.plotRealTime(op_mysql)

    def stopPlotRealTime(self):
        self.mpl.stopPlotRealTime()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.show()
    sys.exit(app.exec_())
