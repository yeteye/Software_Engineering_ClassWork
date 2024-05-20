from PySide6 import QtCore
from PySide6.QtGui import QFont, QPixmap, QIcon, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLCDNumber, QSizePolicy, QLabel, QMessageBox
from PySide6.QtCore import QTimer
import json
from levelSystem import LevelSystem

class CountdownWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.flag = 1
        self.timeLast = 0
        self.task_times = 0
        self.time_left = 1500
        self.ExpShow = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_display)
        self.display_text = "25:00"
        self.LevelSystem = LevelSystem()
        self.ExpShow = None
        self.PetShow = None
        self.MainWindow = None




        layout = QVBoxLayout(self)
        layout.setSpacing(20)

        self.lcd = QLCDNumber()
        self.lcd.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )  # 设置 LCD 数字显示的大小策略为尽可能扩展
        self.lcd.setDigitCount(5)  # 设置显示位数
        self.lcd.display(self.display_text)  # 初始显示值为00:00
        layout.addWidget(self.lcd)

        # 设置Qlabel字体
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setFamily("Arial")

        # 添加中间的使用说明部分和任务完成次数显示
        self.explain = QLabel(self)
        self.explain.setFont(font)
        self.explain.setObjectName(u"explain")
        self.setTimes()
        self.explain.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(self.explain, alignment=QtCore.Qt.AlignmentFlag.AlignTop)

        # 添加start和stop的button
        self.start_button = QPushButton("开始\n你的下一次专注吧！！！")
        self.start_button.clicked.connect(
            self.start_countdown
        )  # 点击时，调用start_countdown
        layout.addWidget(self.start_button, alignment=QtCore.Qt.AlignmentFlag.AlignBottom)

        self.stop_button = QPushButton("工作累了\n休息一下吧")
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(
            self.stop_countdown
        )  # 点击时，调用stop_countdown
        layout.addWidget(self.stop_button, alignment=QtCore.Qt.AlignmentFlag.AlignBottom)

    # button功能实现
    def start_countdown(self):
        self.PetShow.change_state(2)
        self.time_Update()
        self.LcdDisplay(self.time_left)
        self.timer.stop()
        self.timer.start(1000)  # 每秒触发一次timeout信号
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_countdown(self):
        self.PetShow.change_state(3)
        self.flag = 2
        self.time_Update()
        self.LcdDisplay(self.time_left)
        self.timer.stop()
        self.timer.start(1000)
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.flag = 1

    # lcd倒计时
    def update_display(self):
        self.time_left -= 1
        if self.time_left <= 0:
            self.timer.stop()
            self.time_left = 0
            self.flag = 1
            self.task_times += 1
            self.setTimes()
            try:
                with open("profile.json", 'r') as f:
                    data = json.load(f)
                    data['plannedTime'] = self.timeLast
                    data['task_times'] = self.task_times
            except FileNotFoundError:
                data = {
                    'level': 1,
                    'exp': 0,
                    'task_times': self.task_times,
                    'plannedTime': self.timeLast
                }
            with open("profile.json", 'w') as f:
                json.dump(data, f)
            self.LevelSystem.levelCalculate()
            self.ExpShow.update_labels()
            self.timeLast = 0
            if not self.start_button.isEnabled():
                if self.MainWindow:
                    self.MainWindow.shake_signal.emit()
                self.RaiseWork()
            if self.start_button.isEnabled():
                if self.MainWindow:
                    self.MainWindow.shake_signal.emit()
                self.RaiseRelax()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
        self.LcdDisplay(self.time_left)





    # lcd显示实现
    def LcdDisplay(self, Time):
        minutes = Time // 60
        seconds = Time % 60
        self.display_text = f"{minutes:02d}:{seconds:02d}"
        self.lcd.display(self.display_text)

    # 获取专注/休息时间长度
    def time_Update(self):
        if self.flag == 1:
            self.timeLast = 1500
            self.time_left = self.timeLast
        elif self.flag == 2:
            self.timeLast = 300
            self.time_left = self.timeLast
        else:
            self.time_left = self.timeLast

    def setTimes(self):
        self.explain.setText("直接按下'开始'默认专注" + str(25) + "mins\n" + "\n" +
                             "按下'休息'固定休息" + str(5) + "mins\n" +
                             "可选择点击右侧已创建任务\n以修改专注时间\n" + "\n" +
                             "(最多只能创建"+str(10)+"个任务)"+"\n"
                             "已专注次数:  " + str(self.task_times))

    def RaiseWork(self):
        message_box = QMessageBox(QMessageBox.Information, "工作完成!", "工作完成!")
        message_box.setWindowIcon(QIcon(QPixmap("image/f3006b49c9f1fc1519d2bf688fc52e70.ico")))
        message_box.setWindowFlags(message_box.windowFlags() | Qt.WindowStaysOnTopHint)
        message_box.exec()

    def RaiseRelax(self):
        message_box = QMessageBox(QMessageBox.Information, "休息完成!", "休息完成!")
        message_box.setWindowIcon(QIcon(QPixmap("image/f3006b49c9f1fc1519d2bf688fc52e70.ico")))
        message_box.setWindowFlags(message_box.windowFlags() | Qt.WindowStaysOnTopHint)
        message_box.exec()
