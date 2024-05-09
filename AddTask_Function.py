from PySide6.QtGui import QMouseEvent, Qt
from PySide6.QtWidgets import QDialog, QWidget, QDialogButtonBox

from AddTask_Ui import Ui_AddTask
from Task import Task
from PySide6.QtWidgets import QDialog
from AddTask_Ui import Ui_AddTask

class AddTaskWindow(QDialog, Ui_AddTask):
    def __init__(self, PomodoroWindowGerner):
        super().__init__()
        self.setupUi(self)
        self.FatherWindow = PomodoroWindowGerner
        Ok_Button = self.buttonBox.button(QDialogButtonBox.Ok)
        Ok_Button.clicked.connect(self.CreateTask())


    def CreateTask(self):
        if self.lineEdit.text() == "" or self.timeEdit.time().minute() * 60 + self.timeEdit.time().second() == 0:
            return
        else:
            task_name = self.lineEdit.text()
            task_time = self.timeEdit.time().minute() * 60 + self.timeEdit.time().second()

            # 创建Task对象并设置属性
            task = Task(task_name, task_time, self)

            # 将Task添加到TaskList中
            self.FatherWindow.AddTaskToList(task)
        return
