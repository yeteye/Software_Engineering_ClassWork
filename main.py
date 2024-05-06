from PySide6.QtWidgets import QApplication
from PomodoroWindowGenerator import PomodoroWindowGenerator

if __name__ == '__main__':
    app = QApplication()
    pomodoroWindowGenerator = PomodoroWindowGenerator()
    pomodoroWindowGenerator.show()

    app.exec()