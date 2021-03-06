# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\plotWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class PlotWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1338, 815)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1061, 811))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.plotpannel_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.plotpannel_2.setContentsMargins(0, 0, 0, 0)
        self.plotpannel_2.setObjectName("plotpannel_2")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(1080, 260, 241, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.commitpannel = QtWidgets.QGridLayout(self.layoutWidget)
        self.commitpannel.setContentsMargins(0, 0, 0, 0)
        self.commitpannel.setObjectName("commitpannel")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.commitpannel.addWidget(self.label_3, 0, 0, 1, 2)
        self.idinput = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.idinput.setFont(font)
        self.idinput.setObjectName("idinput")
        self.commitpannel.addWidget(self.idinput, 1, 0, 1, 1)
        self.idcommitbutton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.idcommitbutton.setFont(font)
        self.idcommitbutton.setObjectName("idcommitbutton")
        self.commitpannel.addWidget(self.idcommitbutton, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.commitpannel.addWidget(self.label, 2, 0, 1, 2)
        self.historyinput = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.historyinput.setFont(font)
        self.historyinput.setObjectName("historyinput")
        self.commitpannel.addWidget(self.historyinput, 3, 0, 1, 1)
        self.historycommitbutton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.historycommitbutton.setFont(font)
        self.historycommitbutton.setObjectName("historycommitbutton")
        self.commitpannel.addWidget(self.historycommitbutton, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.commitpannel.addWidget(self.label_2, 4, 0, 1, 2)
        self.speedinput = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.speedinput.setFont(font)
        self.speedinput.setObjectName("speedinput")
        self.commitpannel.addWidget(self.speedinput, 5, 0, 1, 1)
        self.speedCommitbutton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.speedCommitbutton.setFont(font)
        self.speedCommitbutton.setObjectName("speedCommitbutton")
        self.commitpannel.addWidget(self.speedCommitbutton, 5, 1, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1930, 280, 251, 181))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stoprealtimeplot = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.stoprealtimeplot.setFont(font)
        self.stoprealtimeplot.setObjectName("stoprealtimeplot")
        self.verticalLayout_2.addWidget(self.stoprealtimeplot)
        self.stophistoryplot = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.stophistoryplot.setFont(font)
        self.stophistoryplot.setObjectName("stophistoryplot")
        self.verticalLayout_2.addWidget(self.stophistoryplot)
        self.stoppredict = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.stoppredict.setFont(font)
        self.stoppredict.setObjectName("stoppredict")
        self.verticalLayout_2.addWidget(self.stoppredict)
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(1080, 21, 241, 221))
        self.graphicsView.setObjectName("graphicsView")
        self.layoutWidget_3 = QtWidgets.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(1080, 520, 241, 243))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.plotpannel = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.plotpannel.setContentsMargins(0, 0, 0, 0)
        self.plotpannel.setObjectName("plotpannel")
        self.startrealtimeplot = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.startrealtimeplot.setFont(font)
        self.startrealtimeplot.setObjectName("startrealtimeplot")
        self.plotpannel.addWidget(self.startrealtimeplot)
        self.starthistoryplot = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.starthistoryplot.setFont(font)
        self.starthistoryplot.setObjectName("starthistoryplot")
        self.plotpannel.addWidget(self.starthistoryplot)
        self.startpredict = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.startpredict.setFont(font)
        self.startpredict.setObjectName("startpredict")
        self.plotpannel.addWidget(self.startpredict)
        self.stopplot = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(24)
        self.stopplot.setFont(font)
        self.stopplot.setObjectName("stopplot")
        self.plotpannel.addWidget(self.stopplot)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "????????????????????????"))
        self.idcommitbutton.setText(_translate("Form", "??????"))
        self.label.setText(_translate("Form", "????????????????????????"))
        self.historycommitbutton.setText(_translate("Form", "??????"))
        self.label_2.setText(_translate("Form", "????????????????????????"))
        self.speedCommitbutton.setText(_translate("Form", "??????"))
        self.stoprealtimeplot.setText(_translate("Form", "??????????????????"))
        self.stophistoryplot.setText(_translate("Form", "??????????????????"))
        self.stoppredict.setText(_translate("Form", "??????????????????"))
        self.startrealtimeplot.setText(_translate("Form", "????????????"))
        self.starthistoryplot.setText(_translate("Form", "????????????"))
        self.startpredict.setText(_translate("Form", "????????????"))
        self.stopplot.setText(_translate("Form", "????????????"))
