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
    def __init__(self, parent=None):
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

    #def mousePressEvent(self, event):


    def count_exp(self,data):
        self.level = data['level']
        self.exp = data['exp']
        if self.exp>=10 :
            self.level += 1
            exp = 0


        self.cexp.connect(self.update_display)

        layout = QVBoxLayout(self)

        self.lcd = QLCDNumber()
        self.lcd.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )  # 设置 LCD 数字显示的大小策略为尽可能扩展
        self.lcd.setDigitCount(5)  # 设置显示位数
        self.lcd.display("00:00")  # 初始显示值为00:00
        layout.addWidget(self.lcd)

        display_text = f"{self.level:02d}:{self.exp:02d}"
        self.lcd.display(display_text)

        verticalSpacer = QtWidgets.QSpacerItem(
            10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        layout.addItem(verticalSpacer)




