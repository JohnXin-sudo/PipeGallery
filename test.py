from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt
from random import randint

tab = ['pushButton', 'pushButton_2']

class Ui_MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(Ui_MainWindow, self).__init__(*args, **kwargs)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton.setText('pushButton')
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 10, 75, 23))
        self.pushButton_2.setText('pushButton_2')

        # 创建stackedWidget
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 50, 751, 521))
        MainWindow.setCentralWidget(self.centralwidget)

        # 两个按钮对应两个页面
        for i in range(2):
                label = QLabel('这是页面 %d' % i, self)
                label.setAlignment(Qt.AlignCenter)
                # 此处加了一个margin边距(方便区分QStackedWidget和QLabel的颜色)
                label.setStyleSheet('background: rgb(%d, %d, %d);margin: 50px;' % (
                        randint(0, 255), randint(0, 255), randint(0, 255)))
                self.stackedWidget.addWidget(label)

        # 每个按钮单击时设置触发事件
        self.pushButton.clicked.connect(lambda: self.update_(self.pushButton))
        self.pushButton_2.clicked.connect(lambda: self.update_(self.pushButton_2))

    # stackedWidget内容切换，通过更改其页面ID实现
    def update_(self,btn):
        self.stackedWidget.setCurrentIndex(tab.index(btn.text()))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())