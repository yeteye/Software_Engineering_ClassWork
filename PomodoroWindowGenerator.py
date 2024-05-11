from asyncio import sleep, wait

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QDialog, QDialogButtonBox, QLineEdit, \
    QScrollArea, QVBoxLayout, QFrame, QSizePolicy
from PySide6.QtGui import QMouseEvent, Qt, QPixmap, QMovie
import json

from AddTask_Function import Ui_AddTask, AddTaskWindow
from TaskGenerator import TaskGenerator
from main_window import Ui_MainWindow
from AddTask_Function import AddTaskWindow
from Task import Task

class PomodoroWindowGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.profile = self.loadProfile()
        self.tasklist = {}
        self.tasklist = self.loadTask()
        self.avatarPath = self.profile['avatar']
        self.ui.avatar.setPixmap(QPixmap(self.avatarPath))
        self.ui.avatar.mousePressEvent = self.changeAvatar
        self.ui.TaskCreator.mousePressEvent = self.createTaskUI
        self.ui.listWidget.itemDoubleClicked.connect(self.onItemDoubleClicked)

    ##更改头像
    def changeAvatar(self, mouseEvent: QMouseEvent):
        if mouseEvent.button() != Qt.LeftButton:
            return
        r = QFileDialog.getOpenFileName(parent=self, caption="Select Avatar", filter="Images (*.png *.jpg)")
        imagePath = r[0]
        if not imagePath:
            return
        self.avatarPath = imagePath
        self.updateProfile('avatar', imagePath)
        self.ui.avatar.setPixmap(QPixmap(imagePath))

    ##创建AddTask的Ui界面
    def createTaskUI(self, mouseEvent: QMouseEvent):
        if mouseEvent.button() != Qt.LeftButton:
            return
        dialog = QDialog()
        self.TaskCreator_ui = AddTaskWindow(self)
        self.TaskCreator_ui.setupUi(dialog)
        dialog.exec()


    def ChangeTask(self, mouseEvent: QMouseEvent):##更改任务的信息
        print(12)
        if mouseEvent.button() == Qt.RightButton:
            return

    def loadProfile(self):
        profileFile = open("profile.json")
        profile = json.load(profileFile)
        profileFile.close()
        return profile

    def updateProfile(self, item, value):
        profileFile = open("profile.json", "w")
        profile = self.profile
        profile[item] = value
        profileFile.write(json.dumps(profile, indent=4))
        profileFile.close()

    def loadTask(self):
        try:
            tasklistFile = open("tasklist.json")
        except FileNotFoundError:
            tasklistFile = open("tasklist.json", "w")
        try:
            tasklist = json.load(tasklistFile)
        except ValueError:
            tasklist = {}
        for key in tasklist:
            task = Task(key, tasklist[key])
            self.AddTaskToList(task)
        tasklistFile.close()
        return tasklist

    def AddTaskToList(self, task):
        self.ui.listWidget.addItem(task.name)
        self.tasklist.update({task.name: task.timeLast})
        self.ui.listWidget.repaint()
        return

    def onItemDoubleClicked(self, item):
        # 获取双击的项，并将其传递给 SendTime 方法
        task_name = item.text()
        self.SendTime(task_name)

    def SendTime(self, item):
        if self.ui.clock.start_button.isEnabled():
            self.ui.clock.timer.stop()
            self.ui.clock.stop_button.setEnabled(False)
            self.ui.clock.flag = 3
            self.ui.clock.timeLast = self.tasklist[item]
            self.ui.clock.LcdDisplay(self.tasklist[item])
        return
