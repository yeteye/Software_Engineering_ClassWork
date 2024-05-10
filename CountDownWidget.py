from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLCDNumber, QSizePolicy
from PySide6.QtCore import QTimer
import json
from levelSystem import LevelSystem

class CountdownWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.flag = 1
        self.timeLast = 0
        self.time_left = 1500
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.display_text = "25:00"


        layout = QVBoxLayout(self)

        self.lcd = QLCDNumber()
        self.lcd.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )  # 设置 LCD 数字显示的大小策略为尽可能扩展
        self.lcd.setDigitCount(5)  # 设置显示位数
        self.lcd.display(self.display_text)  # 初始显示值为00:00
        layout.addWidget(self.lcd)

        #设置间距
        verticalSpacer = QtWidgets.QSpacerItem(
            10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        layout.addItem(verticalSpacer)


        self.start_button = QPushButton("开始\n你的下一次专注吧！！！")
        self.start_button.clicked.connect(
            self.start_countdown
        )  # 点击时，调用start_countdown
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("工作累了\n休息一下吧")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(
            self.stop_countdown
        )  # 点击时，调用stop_countdown
        layout.addWidget(self.stop_button)

    #
    def start_countdown(self):
        self.time_Update()
        self.LcdDisplay(self.time_left)
        self.timer.stop()
        self.timer.start(1000)  # 每秒触发一次timeout信号
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_countdown(self):
        self.flag = 2
        self.time_Update()
        self.LcdDisplay(self.time_left)
        self.timer.stop()
        self.timer.start(1000)
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.flag = 1

    def update_display(self):
        self.time_left -= 1
        if self.time_left <= 0:
            self.timer.stop()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
            self.time_left = 0
            self.flag = 1
            try:
                with open("profile.json", 'r') as f:
                    data = json.load(f)
                    data['plannedTime'] = self.timeLast
            except FileNotFoundError:
                data = {
                    'level': 1,
                    'exp': 0,
                    'task_times': 0,
                    'plannedTime': self.timeLast
                }
            with open("profile.json", 'w') as f:
                json.dump(data, f)


        self.LcdDisplay(self.time_left)

    def LcdDisplay(self, Time):
        minutes = Time // 60
        seconds = Time % 60
        self.display_text = f"{minutes:02d}:{seconds:02d}"
        self.lcd.display(self.display_text)

    def time_Update(self):
        if self.flag == 1:
            self.timeLast = 1500
            self.time_left = self.timeLast
        elif self.flag == 2:
            self.timeLast = 300
            self.time_left = self.timeLast
        else:
            self.time_left = self.timeLast
