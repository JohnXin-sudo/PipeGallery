
import sys,base64
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QLabel
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtGui import QImage,QTextDocument,QTextCursor
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
 
class Test(QObject):
    def __init__(self):
        super().__init__()
    @pyqtSlot(str,result=str)
    def print_img(self,img_url):
        #去掉头部的base64标示
        img_url=img_url.replace('data:image/png;base64,', '')
        #将base64解码成二进制
        url=base64.b64decode(img_url)
        #QImage加载二进制，形成图片流
        image=QImage()
        image.loadFromData(url)
 
 
        '''直接输出打印到pdf'''
        printer=QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName('test.pdf')
        #实例化一个富文本
        document=QTextDocument()
        cursor=QTextCursor(document)
        cursor.insertImage(image)
        #调用print（）方法 参数为当前实例化的打印函数
        document.print(printer)
 
        return 'sucess'         #处理成功传回success
 
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    #加载网页
    view=QWebEngineView()
    # f = open("test.html",'r',encoding='utf-8')
    # html = f.read()
    # f.close()   
    # view.setHtml(html)
    view.load(QUrl('file:///test.html'))
    # '''流程：定义通道，连接通道'''
    # #定义通道
    channel = QWebChannel()   #必须定义成全局的，否则会出错，不能在定义界面的类里面里面定义会出错
    # #定义pyqt操作函数
    test = Test()  # 必须定义成全局的，否则会出错，不能在定义界面的类里面会出错
    # #通道与操作函数连接，也就是注册
    channel.registerObject('pyjs', test)
    # #网页连接通道
    view.page().setWebChannel(channel)
 
    view.show()
    sys.exit(app.exec_())