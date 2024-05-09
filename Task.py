from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel


class Task(QWidget):
    def __init__(self, name, timeLast, parent=None):
        super().__init__(parent)

        # 保存任务名和持续时间
        self.name = name
        self.timeLast = timeLast

        # 创建水平布局
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 创建显示任务名的标签
        self.nameLabel = QLabel(self.name)
        layout.addWidget(self.nameLabel)

        # 设置固定高度
        self.setFixedHeight(30)  # 例如，设定为30像素

        # 设置自适应宽度
        self.nameLabel.adjustSize()
        self.setFixedWidth(self.nameLabel.width())  # 宽度根据任务名的长度自适应
