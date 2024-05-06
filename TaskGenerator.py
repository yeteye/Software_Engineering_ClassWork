from PySide6.QtWidgets import QDialog
from AddTask import Ui_AddTask
import json


class TaskGenerator(QDialog):
    def __init__(self):
        super().__init__()
        self.tasklist = self.loadTask()
        self.ui = Ui_AddTask()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.on_accepted)

    def on_accepted(self):
        name = self.ui.lineEdit.text()
        time = self.ui.timeEdit.time().minute() * 60 + self.ui.timeEdit.time().second()
        self.addTask(name, time)
        self.accept()

    def loadTask(self):
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
