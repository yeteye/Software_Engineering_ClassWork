from PySide6.QtCore import QSize
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon


class WebWindow(QMainWindow):
    def __init__(self, if_index=True):
        super().__init__()
        self.if_index = if_index
        self.setUI()

    def setUI(self):
        self.setWindowTitle('Pomodoro Community')
        self.setGeometry(100, 100, 1050, 600)
        # 添加Icon
        icon = QIcon()
        icon.addFile(u"image/f3006b49c9f1fc1519d2bf688fc52e70.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        # 创建Web视图
        self.webView = QWebEngineView()
        self.setCentralWidget(self.webView)
        if self.if_index:
        # 加载网页
            self.webView.setUrl('http://10.16.205.138:8000/')
        else:
            self.webView.setUrl('http://10.16.205.138:8000/post/new/')

