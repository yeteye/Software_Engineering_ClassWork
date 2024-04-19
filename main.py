from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog
from PySide6.QtGui import QMouseEvent, Qt, QPixmap, QMovie
from main_window import Ui_MainWindow
import os

class PomodoroWindowGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication()
    pomodoroWindowGenerator = PomodoroWindowGenerator()
    pomodoroWindowGenerator.show()
    app.exec()