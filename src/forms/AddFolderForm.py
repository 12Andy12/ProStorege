# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddFolderForm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class Ui_AddFolderWindow(object):
    def setupUi(self, AddFolderWindow):
        if not AddFolderWindow.objectName():
            AddFolderWindow.setObjectName("AddFolderWindow")
        AddFolderWindow.resize(307, 116)
        AddFolderWindow.setStyleSheet(
            'font: 12pt "Times New Roman";\n' "background-color: rgb(50, 50, 50);\n" "color: #b1b1b1;"
        )
        self.centralwidget = QWidget(AddFolderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.le_folder_name = QLineEdit(self.centralwidget)
        self.le_folder_name.setObjectName("le_folder_name")

        self.horizontalLayout_2.addWidget(self.le_folder_name)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName("btnAdd")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setMaximumSize(QSize(16777215, 40))
        self.btnAdd.setStyleSheet(
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

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnCancel = QPushButton(self.centralwidget)
        self.btnCancel.setObjectName("btnCancel")
        sizePolicy.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy)
        self.btnCancel.setMaximumSize(QSize(16777215, 40))
        self.btnCancel.setStyleSheet(
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

        self.horizontalLayout.addWidget(self.btnCancel)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_3.setStretch(0, 2)
        AddFolderWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(AddFolderWindow)
        self.statusbar.setObjectName("statusbar")
        AddFolderWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddFolderWindow)

        QMetaObject.connectSlotsByName(AddFolderWindow)

    # setupUi

    def retranslateUi(self, AddFolderWindow):
        AddFolderWindow.setWindowTitle(QCoreApplication.translate("AddFolderWindow", "MainWindow", None))
        self.btnAdd.setText(
            QCoreApplication.translate("AddFolderWindow", "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None)
        )
        self.btnCancel.setText(
            QCoreApplication.translate("AddFolderWindow", "\u041e\u0442\u043c\u0435\u043d\u0430", None)
        )

    # retranslateUi
