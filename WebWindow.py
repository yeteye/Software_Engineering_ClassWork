from PySide6.QtCore import QSize
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon


class WebWindow(QMainWindow):
    def __init__(self, if_index=True,task='',task_time=''):
        super().__init__()
        self.if_index = if_index
        self.task = task
        self.task_time = task_time
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
            url = f'http://frp-fly.top:53065/' # 本地服务器地址，运行时请修改
        else:
            url = f'http://frp-fly.top:53065/post/new/?task={self.task}&task_time={self.task_time}' # 本地服务器地址，运行时请修改
        self.webView.setUrl(url)
