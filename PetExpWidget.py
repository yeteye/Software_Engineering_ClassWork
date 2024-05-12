from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from ExpShow import Exp_Show
from PetShow import GIFWindow

class PetExpWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.petShow = GIFWindow(parent)
        self.petShow.setObjectName(u"Show")
        self.expShow = Exp_Show(parent)
        self.expShow.setObjectName(u"Show")
        layout.addWidget(self.petShow)
        layout.addWidget(self.expShow)
        layout.setStretch(2, 0)
        self.setLayout(layout)
