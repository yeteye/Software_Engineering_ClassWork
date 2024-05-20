from PySide6.QtCore import QTime, QCoreApplication, QPropertyAnimation, QRect, Signal, QTimer, QUrl
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QDialog, QDialogButtonBox, QLineEdit, \
    QScrollArea, QVBoxLayout, QFrame, QSizePolicy
from PySide6.QtGui import QMouseEvent, Qt, QPixmap, QPainter, QPainterPath
import json
from WebWindow import WebWindow
from levelSystem import LevelSystem
from main_window import Ui_MainWindow
from AddTask_Function import AddTaskWindow
from Task import Task

class PomodoroWindowGenerator(QWidget):
    shake_signal = Signal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filename = "pomodoro.json"
        self.data = self.load_data()
        self.flag = 0
        self.TaskCreator_ui = None
        self.tasklist = {}
        # 将缓存信息装入
        self.profile = self.loadProfile()
        self.INITIALIZE()
        # 设置头像
        self.avatarPath = self.profile['avatar']
        self.ui.avatar.setPixmap(self.CreateRoundedPixmap())
        self.ui.avatar.mousePressEvent = self.changeAvatar
        self.ui.TaskCreator.mousePressEvent = self.createTaskUI
        self.ui.community.mousePressEvent = self.TurnToWeb

        self.ui.clock.ExpShow = self.ui.widget_2  #原expShow
        self.ui.clock.PetShow = self.ui.widget

        self.ui.clock.ExpShow.AddClock(self.ui.clock)
        self.shake_sound = QSoundEffect(self)
        self.shake_sound.setSource(QUrl.fromLocalFile("image/shakese.wav"))
        self.ui.clock.MainWindow = self
        self.shake_signal.connect(self.start_shake)
        self.shake_timer = QTimer(self)
        self.shake_timer.timeout.connect(self.shake_window)


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
        self.ui.avatar.setPixmap(self.CreateRoundedPixmap())

    # 创建AddTask的Ui界面
    def createTaskUI(self, mouseEvent: QMouseEvent):
        if self.ui.TaskListContainer.count() <= 10:
            if mouseEvent.button() != Qt.LeftButton:
                return
            self.CreatorUiInit(None)

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
        # self.clearAll(self.ui.TaskListContainer)
        for key in tasklist:
            task = Task(key,tasklist[key],self)
            self.AddTaskToList(task)
            task.MainWindow = self
        self.ui.TaskListContainer.insertStretch(-1, 1)
        tasklistFile.close()
        return tasklist

    def AddTaskToList(self, task):
        self.ui.TaskListContainer.addWidget(task)
        self.tasklist.update({task.name: task.timeLast})
        return


    def CreateRoundedPixmap(self):
        pixmap = QPixmap(self.avatarPath).scaled(115, 115, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        rounded_pixmap = QPixmap(pixmap.size())
        rounded_pixmap.fill(Qt.transparent)
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        path = QPainterPath()
        path.addEllipse(0, 0, pixmap.width(), pixmap.height())
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        return rounded_pixmap

    def CreatorUiInit(self,Task):
        dialog = QDialog()
        self.TaskCreator_ui = AddTaskWindow(self)
        self.TaskCreator_ui.setupUi(dialog)
        if self.flag == 1:
            self.TaskCreator_ui.Task = Task
            self.TaskCreator_ui.lineEdit.setText(Task.name)
            time = QTime(0, Task.timeLast // 60, Task.timeLast % 60)
            self.TaskCreator_ui.timeEdit.setTime(time)
        dialog.exec()

    def TurnToWeb(self, mouseEvent: QMouseEvent):
        if mouseEvent.button() != Qt.LeftButton:
            return
        import sys
        self.WebWindow = WebWindow()
        self.WebWindow.show()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)
        f.close()

    def AddMainWindow(self):
        self.ui.clock.MainWindow = self

    def start_shake(self):
        self.shake_timer.start(50)
        self.shake_sound.play()
        self.shake_count = 0
        self.original_pos = self.pos()

    def shake_window(self):
        dx = dy = 5
        if self.shake_count % 2 == 0:
            dx = -dx
        if (self.shake_count // 2) % 2 == 0:
            dy = -dy
        self.move(self.original_pos.x() + dx, self.original_pos.y() + dy)
        self.shake_count += 1

        if self.shake_count == 10:
            self.shake_timer.stop()
            self.shake_sound.stop()
            self.move(self.original_pos)