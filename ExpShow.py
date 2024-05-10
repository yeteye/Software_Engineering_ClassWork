from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QSizePolicy, QLabel, QVBoxLayout, QWidget, QProgressBar
from levelSystem import LevelSystem

class Exp_Show(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.level = 1
        self.exp = 3
        self.display_text = (f"<br><br>LV：{self.level}"
                             f"<br>EXP：{self.exp}")

        layout = QVBoxLayout(self)

        #显示文本
        self.label = QLabel(self.display_text)
        #文本左对齐
        self.label.setAlignment(Qt.AlignLeft)
        #设置字体大小
        font = self.label.font()
        font.setPointSize(20)  # 设置字体大小为 20
        self.label.setFont(font)
        #设置字体颜色
        self.label.setStyleSheet("color: green;")
        # 创建一个进度条对象
        progress_bar = QProgressBar()
        # 设置进度条的范围和初始值
        progress_bar.setMinimum(0)
        progress_bar.setMaximum(100)
        progress_bar.setValue(50)  # 设置初始值为 50
        #进度条外观设置
        progress_bar.setStyleSheet(
            "QProgressBar {"
            "    border: 2px solid grey;"
            "    border-radius: 5px;"
            "    background-color: lightgrey;"
            "    text-align: center;"  # 让显示的文本居中对齐
            "}"
            "QProgressBar::chunk {"
            "    background-color: green;"
            "    width: 20px;"  # 设置进度块宽度
            "}"
        )
        #对文本大小进行设置
        self.label.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        # 显示的大小策略为尽可能扩展
        layout.addWidget(self.label)
        layout.addWidget(progress_bar)

        # 顶靠
        verticalSpacer = QtWidgets.QSpacerItem(
            10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        layout.addItem(verticalSpacer)

    def update_display(self):
        self.level = 2
        self.exp = 4

        self.Display(self.level , self.exp)
    def Display(self):
        self.display_text = f" {self.level},  {self.exp}"
        self.lcd.display(self.display_text)

