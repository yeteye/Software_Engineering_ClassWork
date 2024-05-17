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
