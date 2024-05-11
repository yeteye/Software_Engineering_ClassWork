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
        self.tasklist = {}
        # 将缓存信息装入
        self.profile = self.loadProfile()
        self.INITIALIZE()
        # 设置头像
        self.avatarPath = self.profile['avatar']
        self.ui.avatar.setPixmap(QPixmap(self.avatarPath))
        self.ui.avatar.mousePressEvent = self.changeAvatar
        self.ui.TaskCreator.mousePressEvent = self.createTaskUI


    def INITIALIZE(self):
        # 加入缓存任务
        self.tasklist = self.loadTask()
        # 设置完成次数
        self.ui.clock.task_times = self.profile['task_times']
        self.ui.clock.setTimes()

        return
    # 更改头像
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

    # 创建AddTask的Ui界面
    def createTaskUI(self, mouseEvent: QMouseEvent):
        if self.ui.TaskListContainer.count() <= 10:
            if mouseEvent.button() != Qt.LeftButton:
                return
            dialog = QDialog()
            self.TaskCreator_ui = AddTaskWindow(self)
            self.TaskCreator_ui.setupUi(dialog)
            dialog.exec()

    # 向程序转入缓存文件内容
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
            task.MainWindow = self
        self.ui.TaskListContainer.insertStretch(-1, 1)
        tasklistFile.close()
        return tasklist

    def AddTaskToList(self, task):
        self.ui.TaskListContainer.addWidget(task)
        self.tasklist.update({task.name: task.timeLast})
        return

