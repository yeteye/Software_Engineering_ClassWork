from PySide6.QtGui import QMouseEvent, Qt


class Task(object):
    def __init__(self,name,time):
        self.name = name
        self.timeLast = time
