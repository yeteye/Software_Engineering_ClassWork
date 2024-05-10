from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout ,QLCDNumber ,QSizePolicy
from PySide6.QtCore import QSize
import json

# 打开并读取json文件
with open('profile.json', 'r') as f:
    data = json.load(f)

class GIFWindow(QWidget):
    def __init__(self,data, parent=None):
        super().__init__(parent)

        # 创建QMovie对象并加载GIF文件
        self.movie = QMovie("image\pet.gif")
        self.movie.setScaledSize(QSize(200, 200))
        # 创建一个QLabel来显示GIF
        self.gif_label = QLabel()
        self.gif_label.setAlignment(Qt.AlignCenter)

        # 设置QMovie对象到QLabel上
        self.gif_label.setMovie(self.movie)

        # 开始动画
        self.movie.start()


        # 创建布局并将QLabel添加到其中
        layout = QVBoxLayout(self)
        layout.addWidget(self.gif_label)
        self.setLayout(layout)

        verticalSpacer = QtWidgets.QSpacerItem(
            10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        layout.addItem(verticalSpacer)
        #def mousePressEvent(self, event):


    def count_exp(self):
        self.level = 1
        self.exp = 1
        if self.exp >= 10:
            self.level += 1
            self.exp = 0

        display_text = f"{self.level:02d}:{self.exp:02d}"
        self.gif_label.setText(display_text)

        layout = QVBoxLayout(self)
        layout.addWidget(self.gif_label)
        self.setLayout(layout)



