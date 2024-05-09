from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt


class Task(QWidget):
    def __init__(self, name, timeLast, parent=None):
        super().__init__(parent)

        # 保存任务名和持续时间
        self.name = name
        self.timeLast = timeLast

        # 创建水平布局
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(Qt.AlignCenter)  # 设置布局中部件的对齐方式为居中对齐

        # 创建显示任务名的标签，并设置居中对齐
        self.nameLabel = QLabel(self.name)
        self.nameLabel.setAlignment(Qt.AlignCenter)  # 设置标签的文本对齐方式为居中对齐
        layout.addWidget(self.nameLabel)

        # 设置固定高度
        self.setFixedHeight(30)  # 例如，设定为30像素

        # 设置自适应宽度
        self.nameLabel.adjustSize()
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)  # 宽度自适应
