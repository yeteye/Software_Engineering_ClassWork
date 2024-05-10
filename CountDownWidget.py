from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLCDNumber, QSizePolicy
from PySide6.QtCore import QTimer


class CountdownWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.flag = 1
        self.time_left = self.time_Update()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)

        layout = QVBoxLayout(self)

        self.lcd = QLCDNumber()
        self.lcd.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )  # 设置 LCD 数字显示的大小策略为尽可能扩展
        self.lcd.setDigitCount(5)  # 设置显示位数
        self.lcd.display("00:00")  # 初始显示值为00:00
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
        self.timer.stop()
        self.timer.start(1000)  # 每秒触发一次timeout信号
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_countdown(self):
        self.flag = 2
        self.time_Update()
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

        minutes = self.time_left // 60
        seconds = self.time_left % 60
        display_text = f"{minutes:02d}:{seconds:02d}"
        self.lcd.display(display_text)

    def time_Update(self):
        if self.flag == 1:
            self.time_left = 1500
        elif self.flag == 2:
            self.time_left = 300
