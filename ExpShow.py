from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QSizePolicy, QLabel, QVBoxLayout, QWidget, QProgressBar
from PySide6.QtGui import QFont
import json

class ExpShow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.filename = "profile.json"
        self.data = self.load_data()

        self.display_text = ("""
            <br><br><span style="color: blue;">LV: </span>
            <span style="color: green;">""" + f"{self.data['level']}" + """</span>
            <br><span style="color: blue;">Exp：</span>
            <span style="color: green;">""" + f"{self.data['exp']}/{self.data['level']*100}" + """</span>
                """)

        layout = QVBoxLayout(self)

        #显示文本
        self.label = QLabel(self.display_text)
        #文本左对齐
        self.label.setAlignment(Qt.AlignLeft)
        #设置字体大小
        font = QFont()
        font.setPointSize(20)  # 设置字体大小为 20

        #设置字体外观

        #self.label.setStyleSheet("color: green;")
        font.setFamily('Comic Sans MS')
        font.setBold(True)  # 设置字体粗细
        font.setItalic(True)  # 设置斜体
        font.setUnderline(False)  # 添加下划线
        font.setLetterSpacing(QFont.AbsoluteSpacing, 2)  # 设置字间距

        self.label.setFont(font)

        # 创建一个进度条对象
        self.progress_bar = QProgressBar()
        # 设置进度条的范围和初始值
        self.SetProgressBar()
        #进度条外观设置

        #可根据属性更改
        self.setStyleSheet("""
                    QProgressBar {
                        border: 3px solid #FFD700;  /* 金色边框 */
                        border-radius: 10px;  /* 圆角 */
                        background-color: #FFA07A;  /* 浅橙色背景 */
                        height: 15px;  /* 高度 */
                        text-align: center;  /* 文本居中 */
                        font-size: 18px;  /* 字体大小 */
                        color: white;  /* 字体颜色 */
                        padding: 5px;  /* 内边距 */
                        box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);  /* 阴影效果 */
                    }
                    QProgressBar::chunk {
                        background-color: qlineargradient(
                            x1: 0, y1: 0, x2: 1, y2: 1,
                            stop: 0 #FF4500,  /* 橙红色 */
                            stop: 1 #32CD32  /* 黄绿色 */
                        );
                        border-radius: 10px;  /* 圆角 */
                        margin: 1px;  /* 间距 */
                    }
                """)
        #对文本大小进行设置
        self.label.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )

        # 显示的大小策略为尽可能扩展
        layout.addWidget(self.label)
        layout.addWidget(self.progress_bar)

        # 顶靠
        verticalSpacer = QtWidgets.QSpacerItem(
            10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        layout.addItem(verticalSpacer)

    def update_labels(self):
        # 获取等级和经验值
        self.data = self.load_data()

        # 更新 QLabel 显示的文本


        self.display_text = ("""
    <br><br><span style="color: blue;">LV: </span>
    <span style="color: green;">"""+f"{self.data['level']}"+"""</span>
    <br><span style="color: blue;">Exp：</span>
    <span style="color: green;">"""+f"{self.data['exp']}"+"""</span>
        """)
        self.label.setText(self.display_text)
        self.SetProgressBar()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def SetProgressBar(self):
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(self.data['level'] * 100)
        self.progress_bar.setValue(self.data['exp'])  # 设置初始值
        self.progress_bar.setFormat(f"{(self.data['exp'] / self.data['level']):.2f}%")
