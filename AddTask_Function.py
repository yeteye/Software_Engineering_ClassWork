from PySide6.QtCore import QPropertyAnimation, QRect
from PySide6.QtWidgets import QDialogButtonBox
from Task import Task
from PySide6.QtWidgets import QDialog
from AddTask_Ui import Ui_AddTask

class AddTaskWindow(QDialog, Ui_AddTask):
    def __init__(self, PomodoroWindowGerner):   #主界面显示添加任务界面
        super().__init__()
        self.setupUi(self)
        self.Task = None
        self.FatherWindow = PomodoroWindowGerner

    def CreateTask(self):
        if self.lineEdit.text() == "":
            return
        else:
            task_name = self.lineEdit.text()
            task_time = self.timeEdit.time().minute() * 60 + self.timeEdit.time().second()
            Stretch = self.FatherWindow.ui.TaskListContainer.takeAt(self.FatherWindow.ui.TaskListContainer.count() - 1)
            self.FatherWindow.ui.TaskListContainer.removeItem(Stretch)
            if self.FatherWindow.flag == 1:
                self.FatherWindow.ui.TaskListContainer.removeWidget(self.Task)
                self.Task.deleteTaskFromProfile(self.Task.name)
                self.Task.timeLast = task_time
                self.Task.name = task_name
                self.Task.addTaskToProfile(self.Task.name, self.Task.timeLast)
                self.Task.nameLabel.setText(task_name)
                self.FatherWindow.AddTaskToList(self.Task)
                self.FatherWindow.flag = 0
            else:
                # 创建Task对象并设置属性
                for taskName in self.FatherWindow.tasklist:
                    if taskName == self.lineEdit.text():
                        return
                self.Task = Task(task_name, task_time, self.FatherWindow)
                self.Task.addTaskToProfile(task_name, task_time)
                self.Task.AddTaskUi = self
                self.Task.MainWindow = self.FatherWindow

                # 将Task添加到TaskList中

                self.FatherWindow.AddTaskToList(self.Task)
            self.FatherWindow.ui.TaskListContainer.insertStretch(-1, 1)

    def ShakeWindow(self):
        # 定义动画效果，抖动窗口
        animation = QPropertyAnimation(self, b"geometry")
        animation.setDuration(70)
        for i in range(0, 3, 2):
            animation.setKeyValueAt(i / 10, QRect(self.x() - 5, self.y(), self.width(), self.height()))
            animation.setKeyValueAt((i + 1) / 10, QRect(self.x() + 5, self.y(), self.width(), self.height()))
        animation.setEndValue(QRect(self.x(), self.y(), self.width(), self.height()))
        animation.start(QPropertyAnimation.DeleteWhenStopped)