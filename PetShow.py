import os
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer, Qt, QSize
from PySide6.QtGui import QPixmap
import json

class PetShow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = self.load_data()
        self.image_folder = 'image/PET/Normal'
        self.flag = 1
        self.interval = 400
        self.images = []
        self.current_index = 0

        self.load_images(self.image_folder)
        self.init_ui()
        self.start_animation(self.interval)

    def load_images(self, image_folder):
        # 加载文件夹中的所有 PNG 图像
        self.images.clear()
        self.image_folder = image_folder
        if not os.path.exists(self.image_folder):
            print(f"Image folder {self.image_folder} does not exist.")
            return
        for filename in sorted(os.listdir(self.image_folder)):
            if filename.endswith('.png'):
                self.images.append(os.path.join(self.image_folder, filename))
        if not self.images:
            print(f"No PNG images found in folder {self.image_folder}.")
        self.current_index = 0  # Reset index after loading images

    def init_ui(self):
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.label.setMaximumSize(QSize(200, 200))
        self.label.setScaledContents(True)

    def start_animation(self, interval):
        # 设置定时器以切换图像
        self.interval = interval
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(self.interval)

    def update_frame(self):
        # 切换图像
        if self.images:
            pixmap = QPixmap(self.images[self.current_index])
            self.label.setPixmap(pixmap)
            self.current_index = (self.current_index + 1) % len(self.images)
        else:
            print("No images to display.")

    def change_state(self, flag):
        self.change_animation(flag)

    def change_animation(self, flag):
        if flag == 1:
            self.image_folder = 'image/PET/Normal'
            self.interval = 400
        elif flag == 2:
            self.image_folder = 'image/PET/Study'
            self.interval = 500
        elif flag == 3:
            self.image_folder = 'image/PET/Sleep'
            self.interval = 700
        elif flag == 4:
            self.image_folder = 'image/PET/Touch_Body'
            self.interval = 200
        self.display(self.image_folder, self.interval)

    def load_data(self):
        try:
            with open('profile.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def click_event(self):
        return {}

    def display(self, image_folder, interval):
        self.load_images(image_folder)
        self.timer.stop()
        self.start_animation(interval)
        self.update_frame()
