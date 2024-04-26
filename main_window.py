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
        icon.addFile(u"image/f3006b49c9f1fc1519d2bf688fc52e70.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#MainWindow{background-color: rgb(255, 82, 99)}\n"
"")
        self.horizontalLayout = QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.User_Profile = QVBoxLayout()
        self.User_Profile.setObjectName(u"User_Profile")
        self.community = QPushButton(MainWindow)
        self.community.setObjectName(u"community")

        self.User_Profile.addWidget(self.community)

        self.avatar = QLabel(MainWindow)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setMaximumSize(QSize(115, 115))
        self.avatar.setPixmap(QPixmap(u"image/QQ\u56fe\u724720231118082505.jpg"))
        self.avatar.setScaledContents(True)
        self.avatar.setWordWrap(False)


        self.User_Profile.addWidget(self.avatar)


        self.verticalLayout.addLayout(self.User_Profile)

        self.TaskPlace = QVBoxLayout()
        self.TaskPlace.setSpacing(1)
        self.TaskPlace.setObjectName(u"TaskPlace")
        self.TaskCreator = QPushButton(MainWindow)
        self.TaskCreator.setObjectName(u"TaskCreator")

        self.TaskPlace.addWidget(self.TaskCreator)

        self.TaskList = QListWidget(MainWindow)
        self.TaskList.setObjectName(u"TaskList")

        self.TaskPlace.addWidget(self.TaskList)


        self.verticalLayout.addLayout(self.TaskPlace)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 5)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.clock = CountdownWidget(MainWindow)
        self.clock.setObjectName(u"clock")

        self.verticalLayout_5.addWidget(self.clock)


        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_3.setStretch(0, 4)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.pet = QVBoxLayout()
        self.pet.setSpacing(6)
        self.pet.setObjectName(u"pet")

        self.horizontalLayout.addLayout(self.pet)

        self.horizontalLayout.setStretch(0, 15)
        self.horizontalLayout.setStretch(1, 25)
        self.horizontalLayout.setStretch(2, 30)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pomodoro", None))
        self.community.setText(QCoreApplication.translate("MainWindow", u"\u793e\u533a", None))
        self.avatar.setText("")
        self.TaskCreator.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi



