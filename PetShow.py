import os
from PySide6.QtWidgets import  QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer, Qt, QSize
from PySide6.QtGui import QPixmap
import json
class PetShow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_folder = 'image/PET/Sleep'
        self.flag= 1
        self.interval = 700
        self.images = []
        self.current_index = 0

        self.load_images()
        self.init_ui()
        self.start_animation()

    def load_images(self):
        # 加载文件夹中的所有 PNG 图像
        for filename in sorted(os.listdir(self.image_folder)):
            if filename.endswith('.png'):
                self.images.append(os.path.join(self.image_folder, filename))

    def init_ui(self):
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


        #self.setFixedSize(200, 200)  # 固定窗口大小为 200x200
        self.label.setMaximumSize(QSize(200, 200))
        self.label.setScaledContents(True)

    def start_animation(self):
        # 设置定时器以切换图像
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(self.interval)

    def update_frame(self):
        # 切换图像
        if self.images:
            pixmap = QPixmap(self.images[self.current_index])
            self.label.setPixmap(pixmap)
            self.current_index = (self.current_index + 1) % len(self.images)





