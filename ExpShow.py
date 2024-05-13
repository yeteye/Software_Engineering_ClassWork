from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QSizePolicy, QLabel, QVBoxLayout, QWidget, QProgressBar
import json

with open("profile.json", 'r') as file:
    data = json.load(file)
class Exp_Show(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.level = data['level']
        self.exp = data['exp']
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
        progress_bar.setMaximum(int(self.level)*100)
        progress_bar.setValue(int(self.exp))  # 设置初始值
        progress_bar.setFormat(f"{(int(self.exp)/(int(self.level)*100))*100:.2f}%")

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

    def update_labels(self):
        # 获取等级和经验值
        self.level = data['level']
        self.exp = data['exp']

        # 更新 QLabel 显示的文本
        self.display_text = (f"<br><br>LV：{self.level}"
                             f"<br>EXP：{self.exp}")
