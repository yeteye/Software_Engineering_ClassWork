# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pomodoro.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from CountDownWidget import CountdownWidget
from ExpShow import ExpShow
from PetShow import PetShow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(532, 413)
        icon = QIcon()
        icon.addFile(u"image/f3006b49c9f1fc1519d2bf688fc52e70.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)

       #主窗口调整

        MainWindow.setStyleSheet("""
            #MainWindow {
                background-color: rgb(255, 82, 99);
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)




        self.horizontalLayout = QHBoxLayout(MainWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.User_Profile = QVBoxLayout()
        self.User_Profile.setObjectName(u"User_Profile")
        self.community = QPushButton(MainWindow)
        self.community.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.community.setObjectName(u"community")

        self.User_Profile.addWidget(self.community)

        self.avatar = QLabel(MainWindow)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setMaximumSize(QSize(115, 115))
        self.avatar.setScaledContents(True)
        self.avatar.setWordWrap(False)
        self.avatar.setAlignment(Qt.AlignCenter)
        self.User_Profile.addWidget(self.avatar)


        self.verticalLayout.addLayout(self.User_Profile)

        self.TaskCreator = QPushButton(MainWindow)
        self.TaskCreator.setObjectName(u"TaskCreator")

        self.verticalLayout.addWidget(self.TaskCreator)

        self.TaskPlace = QVBoxLayout()
        self.TaskPlace.setSpacing(1)
        self.TaskPlace.setObjectName(u"TaskPlace")

        self.TaskList = QGroupBox(MainWindow)
        self.TaskList.setObjectName(u"TASKLIST")
        self.TaskListContainer = QVBoxLayout()
        self.TaskListContainer.setSpacing(1)
        self.TaskListContainer.setObjectName(u"TaskListContainer")
        self.TaskListContainer.setSpacing(1)
        self.TaskList.setLayout(self.TaskListContainer)
        self.TaskPlace.addWidget(self.TaskList)
        self.verticalLayout.addLayout(self.TaskPlace)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(2, 5)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.ClockPlace = QVBoxLayout()
        self.ClockPlace.setObjectName(u"ClockPlace")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.clock = CountdownWidget(MainWindow)
        self.clock.setObjectName(u"clock")

        self.verticalLayout_5.addWidget(self.clock)


        self.ClockPlace.addLayout(self.verticalLayout_5)

        self.ClockPlace.setStretch(0, 4)

        self.horizontalLayout.addLayout(self.ClockPlace)

        self.pet = QVBoxLayout()
        self.pet.setSpacing(6)
        self.pet.setObjectName(u"pet")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = PetShow(MainWindow)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = ExpShow(MainWindow)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_2.addWidget(self.widget_2)


        self.pet.addLayout(self.verticalLayout_2)


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
        self.TaskList.setTitle(QCoreApplication.translate("MainWindow", u"TASKLIST", None))
    # retranslateUi

