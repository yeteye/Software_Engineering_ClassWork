from PySide6.QtWidgets import QWidget


class Task(QWidget):
    def __init__(self):
        super().__init__()
        self.done = False
        self.time = 0