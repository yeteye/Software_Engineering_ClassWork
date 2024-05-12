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
        Ok_Button = self.buttonBox.button(QDialogButtonBox.Ok)
        Ok_Button.clicked.connect(self.CreateTask())

    def CreateTask(self):
        if self.lineEdit.text() == "" or self.timeEdit.time().minute() * 60 + self.timeEdit.time().second() < 300:# 方便试验设为10seconds
            return
        else:
            task_name = self.lineEdit.text()
            task_time = self.timeEdit.time().minute() * 60 + self.timeEdit.time().second()
            if self.FatherWindow.flag == 1:
                self.Task.deleteTaskFromProfile(self.Task.name)
                self.Task.timeLast = task_time
                self.Task.name = task_name
                self.Task.addTaskToProfile(self.Task.name, self.Task.timeLast)
                self.Task.nameLabel.setText(task_name)
                self.FatherWindow.ui.flag = 0
            else:
                # 创建Task对象并设置属性
                self.Task = Task(task_name, task_time)
                self.Task.addTaskToProfile(task_name, task_time)
                self.Task.AddTaskUi = self
                self.Task.MainWindow = self.FatherWindow

                # 将Task添加到TaskList中
                Stretch = self.FatherWindow.ui.TaskListContainer.takeAt(
                    self.FatherWindow.ui.TaskListContainer.count() - 1)
                self.FatherWindow.ui.TaskListContainer.removeItem(Stretch)
                self.FatherWindow.AddTaskToList(self.Task)
                self.FatherWindow.ui.TaskListContainer.insertStretch(-1, 1)



    def UiInitialize(self):
        if self.FatherWindow.flag == 1:
            return