from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
from PySide6.QtGui import QMouseEvent, Qt, QPixmap, QMovie
from main_window import Ui_MainWindow
import os

class PomodoroWindowGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.avatarPath = "Images/novPzrqvE3.jpg"
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.avatar.mousePressEvent = self.changeAvatar
        self.ui.TaskCreator.mousePressEvent = self.createTask

    def changeAvatar(self, mouseEvent: QMouseEvent):
        if mouseEvent.button() != Qt.LeftButton:
            return
        r = QFileDialog.getOpenFileName(parent=self, caption="Select Avatar", filter="Images (*.png *.jpg)")
        imagePath = r[0]
        if not imagePath:
            return
        self.avatarPath = imagePath
        self.ui.avatar.setPixmap(QPixmap(imagePath))

    def createTask(self,mouseEvent: QMouseEvent):
        if mouseEvent.button() != Qt.LeftButton:
            return

    def ChangeTask(self, mouseEvent: QMouseEvent):
        if mouseEvent.button() == Qt.RightButton:
            return



if __name__ == '__main__':
    app = QApplication()
    pomodoroWindowGenerator = PomodoroWindowGenerator()
    pomodoroWindowGenerator.show()
    app.exec()