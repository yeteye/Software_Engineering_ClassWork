from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class PetExpWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        label = QLabel("Hello World")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
