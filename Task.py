import json

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy, QMenu, QDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent

class Task(QWidget):
    def __init__(self, name, timeLast, MainWidow):
        super().__init__()
        # 保存任务名和持续时间
        self.name = name
        self.timeLast = timeLast
        self.MainWindow = MainWidow
        self.MainWindow.tasklist = self.loadTask()
        self.setStyleSheet("border: 1px solid black;")



        # 创建水平布局
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)  # 设置布局中部件的对齐方式为居中对齐

        # 创建显示任务名的标签，并设置居中对齐
        self.nameLabel = QLabel(self.name)
        self.nameLabel.setAlignment(Qt.AlignCenter)  # 设置标签的文本对齐方式为居中对齐
        layout.addWidget(self.nameLabel)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)  # 宽度自适应
        layout.setAlignment(Qt.AlignTop)
        self.mousePressEvent = self.SendTime  # 点击添加的任务，传输任务时间

    def SendTime(self, mouseEvent: QMouseEvent):
        if self.MainWindow.ui.clock.start_button.isEnabled():
            if mouseEvent.button() == Qt.LeftButton:
                self.MainWindow.ui.clock.timer.stop()
                self.MainWindow.ui.clock.stop_button.setEnabled(False)
                self.MainWindow.ui.clock.flag = 3
                self.MainWindow.ui.clock.timeLast = self.timeLast
                self.MainWindow.ui.clock.current_task_time = f'{self.timeLast//60:02d}:{self.timeLast%60:02d}'
                self.MainWindow.ui.clock.current_task = self.name
                self.MainWindow.ui.clock.LcdDisplay(self.timeLast)
        return

    def contextMenuEvent(self, event: QMouseEvent):
        menu = QMenu(self)
        menu.setStyleSheet("QMenu { border-radius: 10px; }")
        DeleteTask = menu.addAction("Delete")
        EditTask = menu.addAction("Edit")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == DeleteTask:
            self.deleteTaskFromProfile(self.name)
            self.layout().removeWidget(self.nameLabel)
            self.nameLabel.deleteLater()
            self.deleteLater()

        if action == EditTask:
            self.MainWindow.flag = 1
            self.MainWindow.CreatorUiInit(self)
            return

    def loadTask(self):
        try:
            tasklistFile = open("tasklist.json")
        except FileNotFoundError:
            tasklistFile = open("tasklist.json", "w")
        try:
            tasklist = json.load(tasklistFile)
        except ValueError:
            tasklist = {}
        tasklistFile.close()
        return tasklist

    def addTaskToProfile(self, name, time):
        self.MainWindow.tasklist.update({name: time})
        tasklistFile = open("tasklist.json", "w")
        tasklistFile.write(json.dumps(self.MainWindow.tasklist, indent=4))
        tasklistFile.close()
        print(self.MainWindow.tasklist)



    def deleteTaskFromProfile(self, name):
        self.MainWindow.tasklist.pop(name)
        tasklistFile = open("tasklist.json", "w")
        tasklistFile.write(json.dumps(self.MainWindow.tasklist, indent=4))
        tasklistFile.close()

