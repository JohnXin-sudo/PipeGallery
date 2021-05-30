# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from .MatplotlibWidget import MatplotlibWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1524, 985)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1319, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.homeButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(36)
        self.homeButton.setFont(font)
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout.addWidget(self.homeButton)
        self.listButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(36)
        self.listButton.setFont(font)
        self.listButton.setObjectName("listButton")
        self.horizontalLayout.addWidget(self.listButton)
        self.controlButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(36)
        self.controlButton.setFont(font)
        self.controlButton.setObjectName("controlButton")
        self.horizontalLayout.addWidget(self.controlButton)
        self.videoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(36)
        self.videoButton.setFont(font)
        self.videoButton.setObjectName("videoButton")
        self.horizontalLayout.addWidget(self.videoButton)
        self.yuzhishezhi = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(36)
        self.yuzhishezhi.setFont(font)
        self.yuzhishezhi.setObjectName("yuzhishezhi")
        self.horizontalLayout.addWidget(self.yuzhishezhi)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 90, 1261, 901))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.plotCurve = MatplotlibWidget(self.gridLayoutWidget_3)
        self.plotCurve.setContentsMargins(0, 0, 0, 0)
        self.plotCurve.setObjectName("plotCurve")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 110, 371, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.historycommitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.historycommitbutton.setGeometry(QtCore.QRect(1420, 170, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.historycommitbutton.setFont(font)
        self.historycommitbutton.setObjectName("historycommitbutton")
        self.historyinput = QtWidgets.QLineEdit(self.centralwidget)
        self.historyinput.setGeometry(QtCore.QRect(1270, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.historyinput.setFont(font)
        self.historyinput.setObjectName("historyinput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1270, 130, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1270, 550, 241, 367))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startrealtimeplot = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.startrealtimeplot.setFont(font)
        self.startrealtimeplot.setObjectName("startrealtimeplot")
        self.verticalLayout.addWidget(self.startrealtimeplot)
        self.stoprealtimeplot = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.stoprealtimeplot.setFont(font)
        self.stoprealtimeplot.setObjectName("stoprealtimeplot")
        self.verticalLayout.addWidget(self.stoprealtimeplot)
        self.starthistoryplot = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.starthistoryplot.setFont(font)
        self.starthistoryplot.setObjectName("starthistoryplot")
        self.verticalLayout.addWidget(self.starthistoryplot)
        self.stophistoryplot = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.stophistoryplot.setFont(font)
        self.stophistoryplot.setObjectName("stophistoryplot")
        self.verticalLayout.addWidget(self.stophistoryplot)
        self.startpredict = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.startpredict.setFont(font)
        self.startpredict.setObjectName("startpredict")
        self.verticalLayout.addWidget(self.startpredict)
        self.stoppredict = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.stoppredict.setFont(font)
        self.stoppredict.setObjectName("stoppredict")
        self.verticalLayout.addWidget(self.stoppredict)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(1270, 340, 241, 201))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.greenButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.greenButton.setFont(font)
        self.greenButton.setObjectName("greenButton")
        self.gridLayout_3.addWidget(self.greenButton, 0, 0, 1, 1)
        self.fengji = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.fengji.setFont(font)
        self.fengji.setObjectName("fengji")
        self.gridLayout_3.addWidget(self.fengji, 0, 1, 1, 1)
        self.redButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.redButton.setFont(font)
        self.redButton.setObjectName("redButton")
        self.gridLayout_3.addWidget(self.redButton, 1, 0, 1, 1)
        self.shuibeng = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.shuibeng.setFont(font)
        self.shuibeng.setObjectName("shuibeng")
        self.gridLayout_3.addWidget(self.shuibeng, 1, 1, 1, 1)
        self.yellowButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.yellowButton.setFont(font)
        self.yellowButton.setObjectName("yellowButton")
        self.gridLayout_3.addWidget(self.yellowButton, 2, 0, 1, 1)
        self.baojing = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.baojing.setFont(font)
        self.baojing.setObjectName("baojing")
        self.gridLayout_3.addWidget(self.baojing, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1270, 230, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.speedCommitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.speedCommitbutton.setGeometry(QtCore.QRect(1420, 270, 93, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.speedCommitbutton.setFont(font)
        self.speedCommitbutton.setObjectName("speedCommitbutton")
        self.speedinput = QtWidgets.QLineEdit(self.centralwidget)
        self.speedinput.setGeometry(QtCore.QRect(1270, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.speedinput.setFont(font)
        self.speedinput.setObjectName("speedinput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1524, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.homeButton.setText(_translate("MainWindow", "系统概述"))
        self.listButton.setText(_translate("MainWindow", "设备清单"))
        self.controlButton.setText(_translate("MainWindow", "远程控制"))
        self.videoButton.setText(_translate("MainWindow", "视频监控"))
        self.yuzhishezhi.setText(_translate("MainWindow", "阈值设置"))
        self.label_5.setText(_translate("MainWindow", "城市综合管廊智慧管控平台"))
        self.historycommitbutton.setText(_translate("MainWindow", "提交"))
        self.label.setText(_translate("MainWindow", "输入查看的历史数据数量"))
        self.startrealtimeplot.setText(_translate("MainWindow", "实时数据"))
        self.stoprealtimeplot.setText(_translate("MainWindow", "关闭实时数据"))
        self.starthistoryplot.setText(_translate("MainWindow", "历史数据"))
        self.stophistoryplot.setText(_translate("MainWindow", "关闭历史数据"))
        self.startpredict.setText(_translate("MainWindow", "实施预测"))
        self.stoppredict.setText(_translate("MainWindow", "关闭实时预测"))
        self.greenButton.setText(_translate("MainWindow", "绿灯"))
        self.fengji.setText(_translate("MainWindow", "风机"))
        self.redButton.setText(_translate("MainWindow", "红灯"))
        self.shuibeng.setText(_translate("MainWindow", "水泵"))
        self.yellowButton.setText(_translate("MainWindow", "黄灯"))
        self.baojing.setText(_translate("MainWindow", "报警"))
        self.label_2.setText(_translate("MainWindow", "输入历史数据数据回放速度"))
        self.speedCommitbutton.setText(_translate("MainWindow", "提交"))
        self.menu.setTitle(_translate("MainWindow", "管廊控制"))
