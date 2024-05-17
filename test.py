import sys
import os
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPixmap

class GifPlayer(QWidget):
    def __init__(self, image_folder, interval=100):
        super().__init__()
        self.image_folder = image_folder
        self.interval = interval
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

        self.setWindowTitle('PNG Animation')
        self.setGeometry(40, 40, 40, 40)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    image_folder = "image"  # 替换为你的PNG图像文件夹路径
    player = GifPlayer(image_folder, interval=100)  # interval以毫秒为单位
    player.show()

    sys.exit(app.exec())
