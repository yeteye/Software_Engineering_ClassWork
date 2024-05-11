import json

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QSizePolicy, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent


class Task(QWidget):
    def __init__(self, name, timeLast, AddTaskWindow, parent=None):
        super().__init__(parent)
        self.creatorWindow = AddTaskWindow
        # 保存任务名和持续时间
        self.name = name
        self.timeLast = timeLast
        self.tasklist = self.loadTask()
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
        if self.creatorWindow.FatherWindow.ui.clock.start_button.isEnabled():
            if mouseEvent.button() == Qt.LeftButton:
                self.creatorWindow.FatherWindow.ui.clock.timer.stop()
                self.creatorWindow.FatherWindow.ui.clock.stop_button.setEnabled(False)
                self.creatorWindow.FatherWindow.ui.clock.flag = 3
                self.creatorWindow.FatherWindow.ui.clock.timeLast = self.timeLast
                self.creatorWindow.FatherWindow.ui.clock.LcdDisplay(self.timeLast)
        return

    def contextMenuEvent(self, event: QMouseEvent):
        menu = QMenu(self)
        menu.setStyleSheet("QMenu { border-radius: 10px; }")
        DeleteTask = menu.addAction("Delete")
        EditTask = menu.addAction("Edit")
        action = menu.exec_(self.mapToGlobal(event.pos()))
        if action == DeleteTask:
            self.deleteTask(self.name)
            self.layout().removeWidget(self.nameLabel)
            self.nameLabel.deleteLater()
            self.deleteLater()
        if action == EditTask:
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

    def addTask(self, name, time):
        self.tasklist.update({name: time})
        tasklistFile = open("tasklist.json", "w")
        tasklistFile.write(json.dumps(self.tasklist, indent=4))
        tasklistFile.close()

    def deleteTask(self, name):
        self.tasklist.pop(name)
        tasklistFile = open("tasklist.json", "w")
        tasklistFile.write(json.dumps(self.tasklist, indent=4))
        tasklistFile.close()
