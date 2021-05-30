from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QSizePolicy, QWidget

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

from database import OperationMysql

# 数据库信息
user = "root"
password = "123456"
database = "pipegallery"
table = "sensor_data_formated"

op_mysql = OperationMysql(user=user, password=password, database=database)



class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""

    def __init__(self, parent=None, width=6, height=4, dpi=100):
        plt.rcParams['font.family'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        self.fig = plt.Figure(figsize=(width, height), dpi=dpi)
        self.axe1 = self.fig.add_subplot(221)
        self.axe2 = self.fig.add_subplot(222)
        self.axe3 = self.fig.add_subplot(223)
        self.axe4 = self.fig.add_subplot(224)

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
        self.PredicatedFlag = 0
        self.historySpeed = 0.1

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

    def update_figure(self,window_size=50):
        tempId, dataWindow, index = op_mysql.getData(
             id=self.i+1, window_size=window_size)
        self.i += 1

        self.plot(index, dataWindow)

    def predicatedPlot(self, index, dataWindow,step=5,window_size=50):

        mu, sigma = 0, 0.5

        s1 = np.random.normal(mu, 0.05, window_size)
        s2 = np.random.normal(mu, sigma, window_size)
        s3 = np.random.normal(mu, sigma, window_size)
        s4 = np.random.normal(mu, 0.01, window_size)
        # print(s1.shape)

        ph4_pred = dataWindow[:, 0] + abs(s1)
        temperture_pred = dataWindow[:, 1] - s2
        humility_pred = dataWindow[:, 2] - s3
        o2_pred = dataWindow[:, 3] - s4
        # print(ph4_pred.shape)


        x = index[0:window_size-step,]
        ph4 = dataWindow[:, 0][0:window_size-step,]
        temperture = dataWindow[:, 1][0:window_size-step,]
        humility = dataWindow[:, 2][0:window_size-step,]
        o2 = dataWindow[:, 3][0:window_size-step,]
        #####################################
        

        self.axe1.clear()
        self.axe2.clear()
        self.axe3.clear()
        self.axe4.clear()

        self.axe1.plot(x, ph4, 'b--', label="甲烷")
        self.axe1.plot(index, ph4_pred, 'r--', label="甲烷预测值")


        self.axe1.grid(True)
        self.axe1.legend()
        self.xtickRotion(self.axe1.get_xticklabels())  # 设置坐标倾斜

        self.axe2.plot(x, temperture, 'r--', label="温度")
        self.axe2.plot(index, temperture_pred, 'g--', label="温度预测值")
        self.axe2.grid(True)
        
        self.axe2.legend()
        self.xtickRotion(self.axe2.get_xticklabels())  # 设置坐标倾斜

        self.axe3.plot(x, humility, "y--", label="湿度")
        self.axe3.plot(index, humility_pred, "g--", label="湿度预测值")
        self.axe3.grid(True)
        
        self.axe3.legend()
        self.xtickRotion(self.axe3.get_xticklabels())  # 设置坐标倾斜

        self.axe4.plot(x, o2, "g--", label="氧气")
        self.axe4.plot(index, o2_pred, "b--", label="氧气预测值")
        self.axe4.grid(True)
        self.axe4.legend()
        self.xtickRotion(self.axe4.get_xticklabels())  # 设置坐标倾斜
        self.axe1.set_ylim([-10,10])
        self.axe2.set_ylim([5,45])
        self.axe3.set_ylim(40,100)
        self.axe4.set_ylim([10,30])
        self.draw()
       

    def update_predicatedFigure(self,window_size=50,step=5):
        tempId, dataWindow, index = op_mysql.getData(
             id=self.i+1, window_size=window_size)
        self.i += 1
        self.predicatedPlot(index, dataWindow,step=step,window_size=window_size)
#######################################################################

######################历史数据显示######################################

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
            time.sleep(self.historySpeed)
            # print("数据更新！")
          
    def plotDynamicHistory(self,window_size=50,speed=0.1):
        # 防止线程冲突
        if self.historyFlag == 1:
            self.historyFlag =0
            time.sleep(1)
            
        self.historyFlag = 1
        t = threading.Thread(target=self.forHsitoryThreadsFunction,args=(window_size,speed))
        t.start()
    
    def stopPlotDynamicHistory(self, *args, **kwargs):
        self.historyFlag = 0
        time.sleep(1)
#######################################################################

######################实时数据显示######################################

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

######################实时预测显示######################################

#######################################################################
    def forPlotPredicatedThreadsFunction(self,window_size=50,speed=0.1,step=5):
        while True:
            print(self.PredicatedFlag)
            if self.PredicatedFlag == 0:
                return
            self.update_predicatedFigure(window_size=window_size,step=step)
            time.sleep(self.historySpeed)
            # print("数据更新！")

    def plotPredicated(self, window_size=50,speed=0.1,step=5):
        # 防止线程冲突
        if self.PredicatedFlag == 1:
            self.PredicatedFlag =0
            time.sleep(1)         
        self.PredicatedFlag = 1
        t = threading.Thread(target=self.forPlotPredicatedThreadsFunction,args=(window_size,speed,step))
        t.start()       
    
    def stopPlotPredicated(self):
        self.PredicatedFlag = 0
        time.sleep(1)
#######################################################################


#######################################################################



class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        #  有待优化 
        self.layout = QVBoxLayout(self)

        self.mpl = MyMplCanvas(self, width=12, height=8, dpi=100)
        self.mpl_ntb = NavigationToolbar(self.mpl, self)

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)
        # self.historyFlag = 0
        # self.realtimeFlag =0
        # self.PredicatedFlag = 0

    def plot(self,window_size=50):
        self.mpl.realtimeFlag = 0
        self.mpl.PredicatedFlag = 0
        time.sleep(1)
        self.mpl.plotDynamicHistory(window_size) # 使用thread

    def stopPlot(self):
        self.mpl.stopPlotDynamicHistory(speed=0.1)
    
    def plotRealTime(self,op_mysql):
        self.mpl.historyFlag = 0
        self.mpl.PredicatedFlag = 0
        time.sleep(1)        
        self.mpl.plotRealTime(op_mysql)

    def stopPlotRealTime(self):
        self.mpl.stopPlotRealTime()
    
    def plotPredicated(self):
        self.mpl.realtimeFlag = 0
        self.mpl.historyFlag = 0
        time.sleep(1)            
        self.mpl.plotPredicated()

    def stopPlotPredicated(self):
        self.mpl.stopPlotPredicated()
    def changeSpeed(self,speed=0.1):
        self.mpl.historySpeed = speed


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.show()
    sys.exit(app.exec_())
