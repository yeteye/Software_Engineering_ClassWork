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
        Ok_Button.mousePressEvent = self.CreateTask


    def CreateTask(self, mouseEvent: QMouseEvent):
        print(12)
        # task_name = self.lineEdit.text()
        # task_time = self.timeEdit.time()
        #
        # # 创建Task对象并设置属性
        # task = Task()
        # task.title = task_name
        # task.timeLast = task_time
        #
        # # 将Task添加到TaskList中
        # self.FatherWindow.AddTaskToList(task)
        #
        # # 关闭AddTask的UI窗口
        # self.close()
        return
