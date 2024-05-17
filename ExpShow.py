from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QSizePolicy, QLabel, QVBoxLayout, QWidget, QProgressBar
import json

class Exp_Show(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.filename = "profile.json"
        self.data = self.load_data()
        self.display_text = (f"<br><br>LV：{self.data['level']}"
                             f"<br>EXP：{self.data['exp']}/{self.data['level']*100}")

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
        self.progress_bar = QProgressBar()
        # 设置进度条的范围和初始值
        self.SetProgressBar()
        #进度条外观设置
        self.progress_bar.setStyleSheet(
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
        layout.addWidget(self.progress_bar)

        # 顶靠
        verticalSpacer = QtWidgets.QSpacerItem(
            10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        layout.addItem(verticalSpacer)

    def update_labels(self):
        # 获取等级和经验值
        self.data = self.load_data()
        print(self.data['exp'])
        # 更新 QLabel 显示的文本
        self.display_text = (f"<br><br>LV：{self.data['level']}"
                             f"<br>EXP：{self.data['exp']}/{self.data['level']*100}")
        self.label.setText(self.display_text)
        self.SetProgressBar()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def SetProgressBar(self):
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(self.data['level'] * 100)
        self.progress_bar.setValue(self.data['exp'])  # 设置初始值
        self.progress_bar.setFormat(f"{(self.data['exp'] / self.data['level']):.2f}%")
