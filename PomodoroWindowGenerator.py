from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QDialog, QDialogButtonBox, QLineEdit, \
    QScrollArea, QVBoxLayout, QFrame
from PySide6.QtGui import QMouseEvent, Qt, QPixmap, QMovie
import json

from AddTask_Function import Ui_AddTask, AddTaskWindow
from TaskGenerator import TaskGenerator
from main_window import Ui_MainWindow


class PomodoroWindowGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.profile = self.loadProfile()
        self.avatarPath = self.profile['avatar']
        self.ui.avatar.setPixmap(QPixmap(self.avatarPath))
        self.ui.avatar.mousePressEvent = self.changeAvatar
        self.ui.TaskCreator.mousePressEvent = self.createTaskUI

        # 创建一个垂直布局，用于放置Task
        self.taskLayout = QVBoxLayout()
        self.taskLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # 创建一个QWidget，作为QScrollArea的内部部件
        self.taskWidget = QWidget()
        self.taskWidget.setLayout(self.taskLayout)

        # 创建一个QScrollArea，并将taskWidget设置为其部件
        self.taskScrollArea = QScrollArea()
        self.taskScrollArea.setWidgetResizable(True)
        self.taskScrollArea.setWidget(self.taskWidget)

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
        # self.TaskCreator_ui = TaskGenerator()
        # self.TaskCreator_ui.ui.setupUi(dialog)
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

    def AddTaskToList(self,Task):
        self.ui.TaskList.setWidget(Task)

        # 创建并添加一个分隔线
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setFixedHeight(1)  # 设置分隔线的高度
        self.taskLayout.addWidget(line)
        return