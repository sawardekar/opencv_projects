# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'faceDetectionUI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.startWebcamButton = QPushButton(self.frame)
        self.startWebcamButton.setObjectName(u"startWebcamButton")

        self.gridLayout.addWidget(self.startWebcamButton, 0, 0, 1, 1)

        self.stopWebcamButton = QPushButton(self.frame)
        self.stopWebcamButton.setObjectName(u"stopWebcamButton")

        self.gridLayout.addWidget(self.stopWebcamButton, 0, 1, 1, 1)

        self.faceDetectionButton = QPushButton(self.frame)
        self.faceDetectionButton.setObjectName(u"faceDetectionButton")

        self.gridLayout.addWidget(self.faceDetectionButton, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.webcamFeedLabel = QLabel(self.centralwidget)
        self.webcamFeedLabel.setObjectName(u"webcamFeedLabel")
        self.webcamFeedLabel.setFrameShape(QFrame.Box)

        self.gridLayout_2.addWidget(self.webcamFeedLabel, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Face Detection", None))
        self.startWebcamButton.setText(QCoreApplication.translate("MainWindow", u"Start Webcam", None))
        self.stopWebcamButton.setText(QCoreApplication.translate("MainWindow", u"Stop Webcam", None))
        self.faceDetectionButton.setText(QCoreApplication.translate("MainWindow", u"Start Face Detection", None))
        self.webcamFeedLabel.setText("")
    # retranslateUi

