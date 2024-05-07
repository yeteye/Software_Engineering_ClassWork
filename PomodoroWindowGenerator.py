from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QDialog
from PySide6.QtGui import QMouseEvent, Qt, QPixmap, QMovie
import json

from main_window import Ui_MainWindow
from TaskGenerator import TaskGenerator
import os


class PomodoroWindowGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.profile = self.loadProfile()
        self.avatarPath = self.profile["avatar"]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.avatar.setPixmap(QPixmap(self.avatarPath))
        self.ui.avatar.mousePressEvent = self.changeAvatar
        self.ui.TaskCreator.mousePressEvent = self.createTask

    def changeAvatar(self, mouseEvent: QMouseEvent):
        if mouseEvent.button() != Qt.LeftButton:
            return
        r = QFileDialog.getOpenFileName(
            parent=self, caption="Select Avatar", filter="Images (*.png *.jpg)"
        )
        imagePath = r[0]
        if not imagePath:
            return
        self.avatarPath = imagePath
        self.updateProfile("avatar", imagePath)
        self.ui.avatar.setPixmap(QPixmap(imagePath))

    def createTask(self, mouseEvent: QMouseEvent):
        if mouseEvent.button() != Qt.LeftButton:
            return
        taskgenerator = TaskGenerator()
        taskgenerator.exec()

    def ChangeTask(self, mouseEvent: QMouseEvent):
        if mouseEvent.button() == Qt.RightButton:
            return

    def loadProfile(self):
        try:
            profileFile = open("profile.json")
        except FileNotFoundError:
            profileFile = open("profile.json", "w")
        try:
            profile = json.load(profileFile)
        except ValueError:
            profile = {
                "avatar": "",
                "level": "",
                "exp": "",
                "name": "",
                "task_times": "",
            }
        profileFile.close()
        return profile

    def updateProfile(self, item, value):
        profile = self.profile
        profile[item] = value
        profileFile = open("profile.json", "w")
        profileFile.write(json.dumps(profile, indent=4))
        profileFile.close()
