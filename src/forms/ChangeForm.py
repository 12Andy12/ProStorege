# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChangeForm.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ChangeWindow(object):
    def setupUi(self, ChangeWindow):
        if not ChangeWindow.objectName():
            ChangeWindow.setObjectName(u"ChangeWindow")
        ChangeWindow.resize(700, 483)
        ChangeWindow.setStyleSheet(u"font: 12pt \"Times New Roman\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: #b1b1b1;")
        self.centralwidget = QWidget(ChangeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(190, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_7.addWidget(self.label)

        self.itemName = QLineEdit(self.centralwidget)
        self.itemName.setObjectName(u"itemName")

        self.horizontalLayout_7.addWidget(self.itemName)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.price = QLineEdit(self.centralwidget)
        self.price.setObjectName(u"price")

        self.horizontalLayout_6.addWidget(self.price)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.originalPrice = QLineEdit(self.centralwidget)
        self.originalPrice.setObjectName(u"originalPrice")

        self.horizontalLayout_5.addWidget(self.originalPrice)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.count = QLineEdit(self.centralwidget)
        self.count.setObjectName(u"count")

        self.horizontalLayout_3.addWidget(self.count)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.type = QLineEdit(self.centralwidget)
        self.type.setObjectName(u"type")

        self.horizontalLayout_2.addWidget(self.type)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.btnAddTags = QPushButton(self.centralwidget)
        self.btnAddTags.setObjectName(u"btnAddTags")
        self.btnAddTags.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(75, 75, 75);\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"     background-color: rgb(80,80, 80);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,120,120);\n"
"}")

        self.verticalLayout_2.addWidget(self.btnAddTags)

        self.tagsTable = QTableWidget(self.centralwidget)
        self.tagsTable.setObjectName(u"tagsTable")

        self.verticalLayout_2.addWidget(self.tagsTable)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.btnAdd = QPushButton(self.centralwidget)
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

        self.btnCancel = QPushButton(self.centralwidget)
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

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 5)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 5)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)

        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 1)
        ChangeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ChangeWindow)
        self.statusbar.setObjectName(u"statusbar")
        ChangeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChangeWindow)

        QMetaObject.connectSlotsByName(ChangeWindow)
    # setupUi

    def retranslateUi(self, ChangeWindow):
        ChangeWindow.setWindowTitle(QCoreApplication.translate("ChangeWindow", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("ChangeWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("ChangeWindow", u"\u0426\u0435\u043d\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u044b", None))
        self.price.setText("")
        self.label_4.setText(QCoreApplication.translate("ChangeWindow", u"\u0426\u0435\u043d\u0430 \u0437\u0430\u043a\u0443\u043f\u043a\u0438", None))
        self.originalPrice.setText("")
        self.label_6.setText(QCoreApplication.translate("ChangeWindow", u"\u041a\u043e\u043b-\u0432\u043e", None))
        self.count.setText("")
        self.label_7.setText(QCoreApplication.translate("ChangeWindow", u"\u0435\u0434. \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.type.setText("")
        self.btnAddTags.setText(QCoreApplication.translate("ChangeWindow", u"addTag", None))
        self.btnAdd.setText(QCoreApplication.translate("ChangeWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btnCancel.setText(QCoreApplication.translate("ChangeWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

