# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DirectoryForm.ui'
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
        DirectoryForm.resize(531, 111)
        DirectoryForm.setFocusPolicy(Qt.StrongFocus)
        DirectoryForm.setStyleSheet(u"font: 12pt \"Times New Roman\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: #b1b1b1;")
        self.verticalLayout_2 = QVBoxLayout(DirectoryForm)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(DirectoryForm)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"background-color: rgb(93, 93, 93);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.le_folder_name = QLineEdit(DirectoryForm)
        self.le_folder_name.setObjectName(u"le_folder_name")
        self.le_folder_name.setMinimumSize(QSize(0, 30))
        self.le_folder_name.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.le_folder_name.setFrame(False)

        self.verticalLayout.addWidget(self.le_folder_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ok = QPushButton(DirectoryForm)
        self.btn_ok.setObjectName(u"btn_ok")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy1)
        self.btn_ok.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(80,80, 80);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,120,120);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(DirectoryForm)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy1.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy1)
        self.btn_cancel.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(80,80, 80);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,120,120);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_cancel)

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
        self.le_folder_name.setInputMask("")
        self.btn_ok.setText(QCoreApplication.translate("DirectoryForm", u"\u041e\u043a", None))
        self.btn_cancel.setText(QCoreApplication.translate("DirectoryForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

