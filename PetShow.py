import os
import time

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget, QSizePolicy
from PySide6.QtCore import QTimer, Qt, QSize
from PySide6.QtGui import QPixmap
import json
import random

class ClickableLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked()

    def clicked(self):
        # 触发点击事件
        self.parent().click_event()

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
        self.label = ClickableLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("""
                    QLabel {
                        border: 2px solid #8f8f91;
                        border-radius: 10px;
                        padding: 5px;
                        background-color: #f0f0f0;
                        background-image: url('image/Pbackground.png');
                        background-position: center;
                        background-size: cover;
                        color: #333;
                        font-size: 18px;
                        font-weight: bold;
                    }
                """)
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
        self.flag = flag

    def change_animation(self, flag):
        if flag == 1:
            self.image_folder = 'image/PET/Normal'
            self.interval = 400
        elif flag == 2:
            self.image_folder = 'image/PET/Study/A_Normal'
            self.interval = 500
        elif flag == 3:
            self.image_folder = 'image/PET/Sleep'
            self.interval = 700
        elif flag == 5:
            self.image_folder = 'image/PET/Study/B_Normal'
            self.interval = 700
        elif flag == 6:
            self.image_folder = 'image/PET/Study/C_Normal'
            self.interval = 500


        self.display(self.image_folder, self.interval)


    def load_data(self):
        try:
            with open('profile.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def click_event(self):
        if self.random()==1:
            self.image_folder = 'image/PET/Touch_Body/A_Happy'
            self.interval = 300
        elif self.random()==2:
            self.image_folder = 'image/PET/Touch_Body/B_Happy'
            self.interval = 300
        elif self.random()==3:
            self.image_folder = 'image/PET/Touch_Body/C_Happy'
            self.interval = 300

        self.display(self.image_folder, self.interval)

        QTimer.singleShot(2000, lambda: self.change_animation(self.flag))  # 2秒后恢复原状态

    def random(self):
        random_number = random.randint(1, 3)
        return random_number
    def display(self, image_folder, interval):
        self.load_images(image_folder)
        self.timer.stop()

        self.start_animation(interval)
        self.update_frame()
