# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pomodoro.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from countdownwidget import CountdownWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(532, 413)
        icon = QIcon()
        icon.addFile(u"C:/Users/86199/Pictures/f3006b49c9f1fc1519d2bf688fc52e70.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#MainWindow{background-color: rgb(255, 82, 99)}\n"
"")
        self.horizontalLayout = QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton = QPushButton(MainWindow)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_6.addWidget(self.pushButton)

        self.avatar = QLabel(MainWindow)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setMaximumSize(QSize(115, 115))
        self.avatar.setPixmap(QPixmap(u"image/QQ\u56fe\u724720231118082505.jpg"))
        self.avatar.setScaledContents(True)
        self.avatar.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.avatar)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.addItemButton = QPushButton(MainWindow)
        self.addItemButton.setObjectName(u"addItemButton")

        self.verticalLayout_7.addWidget(self.addItemButton)

        self.listWidget = QListWidget(MainWindow)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_7.addWidget(self.listWidget)


        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 5)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = CountdownWidget(MainWindow)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_5.addWidget(self.widget)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_3.setStretch(0, 4)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_2.setSpacing(-1)
#endif
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 15)
        self.horizontalLayout.setStretch(1, 25)
        self.horizontalLayout.setStretch(2, 30)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pomodoro", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u793e\u533a", None))
        self.avatar.setText("")
        self.addItemButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

