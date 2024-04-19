# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pomodoro.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(600, 400)
        icon = QIcon()
        icon.addFile(u"C:/Users/86199/Pictures/f3006b49c9f1fc1519d2bf688fc52e70.ico", QSize(), QIcon.Normal, QIcon.Off)
        widget.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.verticalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton = QPushButton(widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 3)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 20)
        self.horizontalLayout.setStretch(1, 30)
        self.horizontalLayout.setStretch(2, 30)

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Pomodoro", None))
        self.pushButton.setText(QCoreApplication.translate("widget", u"\u5f00\u59cb\n"
"\u4f60\u7684\u4e0b\u4e00\u6b21\u4e13\u6ce8\u5427\uff01\uff01\uff01", None))
    # retranslateUi

