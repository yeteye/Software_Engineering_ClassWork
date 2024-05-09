# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddTask.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QTimeEdit, QVBoxLayout, QWidget)

class Ui_AddTask(object):
    def setupUi(self, AddTask):
        if not AddTask.objectName():
            AddTask.setObjectName(u"AddTask")
        AddTask.resize(305, 203)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddTask.sizePolicy().hasHeightForWidth())
        AddTask.setSizePolicy(sizePolicy)
        AddTask.setBaseSize(QSize(280, 180))
        icon = QIcon()
        icon.addFile(u"image/f3006b49c9f1fc1519d2bf688fc52e70.ico", QSize(), QIcon.Normal, QIcon.Off)
        AddTask.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(AddTask)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(AddTask)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(AddTask)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(2, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(AddTask)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.timeEdit = QTimeEdit(AddTask)
        self.timeEdit.setObjectName(u"timeEdit")

        self.horizontalLayout.addWidget(self.timeEdit)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(2, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(AddTask)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(AddTask)
        self.buttonBox.rejected.connect(AddTask.reject)


        #self.buttonBox.accepted.connect(AddTask.accept)

        QMetaObject.connectSlotsByName(AddTask)
    # setupUi

    def retranslateUi(self, AddTask):
        AddTask.setWindowTitle(QCoreApplication.translate("AddTask", u"Let's make a new task", None))
        self.label.setText(QCoreApplication.translate("AddTask", u"New Task Name", None))
        self.label_2.setText(QCoreApplication.translate("AddTask", u"The Lasting Time", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("AddTask", u"mm:ss", None))
    # retranslateUi

