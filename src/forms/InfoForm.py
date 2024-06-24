# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InfoForm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_InfoWindow(object):
    def setupUi(self, InfoWindow):
        if not InfoWindow.objectName():
            InfoWindow.setObjectName("InfoWindow")
        InfoWindow.resize(700, 400)
        InfoWindow.setStyleSheet(
            'font: 12pt "Times New Roman";\n' "background-color: rgb(50, 50, 50);\n" "color: #b1b1b1;"
        )
        self.centralwidget = QWidget(InfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet(
            "QPushButton{\n"
            "	background-color: rgb(75, 75, 75);\n"
            "	border-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "     background-color: rgb(80,80, 80);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(120,120,120);\n"
            "}\n"
            ""
        )

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet(
            "QPushButton{\n"
            "	background-color: rgb(75, 75, 75);\n"
            "	border-radius: 10px;\n"
            "}\n"
            "QPushButton:hover {\n"
            "     background-color: rgb(80,80, 80);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    background-color: rgb(120,120,120);\n"
            "}\n"
            ""
        )

        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 6)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3.setStretch(0, 1)
        InfoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(InfoWindow)
        self.statusbar.setObjectName("statusbar")
        InfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InfoWindow)

        QMetaObject.connectSlotsByName(InfoWindow)

    # setupUi

    def retranslateUi(self, InfoWindow):
        InfoWindow.setWindowTitle(
            QCoreApplication.translate(
                "InfoWindow", "\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "InfoWindow",
                "\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f/\u043f\u0440\u043e\u0434\u0430\u0436\u0438 ",
                None,
            )
        )
        self.pushButton_2.setText(
            QCoreApplication.translate(
                "InfoWindow",
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435",
                None,
            )
        )
        self.pushButton.setText(
            QCoreApplication.translate(
                "InfoWindow",
                "\u0414\u043e\u0431\u0430\u0432\u0442\u044c \u043f\u0440\u043e\u0434\u0430\u0436\u0443",
                None,
            )
        )

    # retranslateUi
