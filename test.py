import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton

class ProgressBarExample(QWidget):
    def __init__(self):
        super().__init__()

        self.data = {'exp': 0}

        self.initUI()

    def initUI(self):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(self.data['exp'])

        self.button = QPushButton('Increase', self)
        self.button.clicked.connect(self.increaseProgress)

        layout = QVBoxLayout()
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setWindowTitle('Progress Bar Example')
        self.setGeometry(300, 300, 300, 200)

    def increaseProgress(self):
        if self.data['exp'] < 100:
            self.data['exp'] += 10
            self.progress_bar.setValue(self.data['exp'])

def main():
    app = QApplication(sys.argv)
    ex = ProgressBarExample()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
import sys
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Qt, QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("窗口抖动示例")
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton("抖动窗口", self)
        self.button.setGeometry(150, 120, 100, 50)
        self.button.clicked.connect(self.start_shake)

        self.shake_timer = QTimer(self)
        self.shake_timer.timeout.connect(self.shake_window)

    def start_shake(self):
        self.shake_timer.start(50)
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
            self.move(self.original_pos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
