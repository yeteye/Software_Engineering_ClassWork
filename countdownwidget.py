from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLCDNumber
from PySide6.QtCore import QTimer


class CountdownWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.time_left = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)

        layout = QVBoxLayout(self)

        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(5)  # 设置显示位数
        self.lcd.display("00:00")  # 初始显示值为00:00
        layout.addWidget(self.lcd)

        self.start_button = QPushButton("开始\n你的下一次专注吧！！！")
        self.start_button.clicked.connect(self.start_countdown)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("工作累了\n休息一下吧")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_countdown)
        layout.addWidget(self.stop_button)

    def start_countdown(self):
        self.time_left = self.get_time_input()
        self.timer.start(1000)  # 每秒触发一次timeout信号
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_countdown(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

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

    def get_time_input(self):
        # 这里可以自定义时间输入的逻辑，比如从输入框中获取用户输入的时间，转换为秒数并返回
        # 这里为了简单起见，直接使用固定的时间60秒
        return 60
