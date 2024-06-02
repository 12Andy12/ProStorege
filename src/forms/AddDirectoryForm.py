# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddDirectoryForm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_DirectoryForm(object):
    def setupUi(self, DirectoryForm):
        if not DirectoryForm.objectName():
            DirectoryForm.setObjectName(u"DirectoryForm")
        DirectoryForm.resize(354, 123)
        DirectoryForm.setStyleSheet(u"font: 12pt \"Times New Roman\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: #b1b1b1;")
        self.verticalLayout_2 = QVBoxLayout(DirectoryForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DirectoryForm)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.le_folder_name = QLineEdit(DirectoryForm)
        self.le_folder_name.setObjectName(u"le_folder_name")

        self.horizontalLayout_2.addWidget(self.le_folder_name)

        self.horizontalLayout_2.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.btnAdd = QPushButton(DirectoryForm)
        self.btnAdd.setObjectName(u"btnAdd")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
        self.btnAdd.setMaximumSize(QSize(16777215, 40))
        self.btnAdd.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(80,80, 80);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,120,120);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnCancel = QPushButton(DirectoryForm)
        self.btnCancel.setObjectName(u"btnCancel")
        sizePolicy.setHeightForWidth(self.btnCancel.sizePolicy().hasHeightForWidth())
        self.btnCancel.setSizePolicy(sizePolicy)
        self.btnCancel.setMaximumSize(QSize(16777215, 40))
        self.btnCancel.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(80,80, 80);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,120,120);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(DirectoryForm)

        QMetaObject.connectSlotsByName(DirectoryForm)
    # setupUi

    def retranslateUi(self, DirectoryForm):
        DirectoryForm.setWindowTitle(QCoreApplication.translate("DirectoryForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("DirectoryForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438", None))
        self.btnAdd.setText(QCoreApplication.translate("DirectoryForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btnCancel.setText(QCoreApplication.translate("DirectoryForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

