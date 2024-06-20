# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ItemForm.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ItemsForm(object):
    def setupUi(self, ItemsForm):
        if not ItemsForm.objectName():
            ItemsForm.setObjectName(u"ItemsForm")
        ItemsForm.resize(603, 369)
        ItemsForm.setStyleSheet(u"font: 12pt \"Times New Roman\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: #b1b1b1;")
        self.verticalLayout_2 = QVBoxLayout(ItemsForm)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_title = QLabel(ItemsForm)
        self.label_title.setObjectName(u"label_title")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setStyleSheet(u"background-color: rgb(93, 93, 93);")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_title)

        self.horizontalLayout_name = QHBoxLayout()
        self.horizontalLayout_name.setSpacing(0)
        self.horizontalLayout_name.setObjectName(u"horizontalLayout_name")
        self.l_name = QLabel(ItemsForm)
        self.l_name.setObjectName(u"l_name")
        self.l_name.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.l_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_name.addWidget(self.l_name)

        self.itemName = QLineEdit(ItemsForm)
        self.itemName.setObjectName(u"itemName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.itemName.sizePolicy().hasHeightForWidth())
        self.itemName.setSizePolicy(sizePolicy1)
        self.itemName.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.itemName.setFrame(False)

        self.horizontalLayout_name.addWidget(self.itemName)

        self.horizontalLayout_name.setStretch(0, 1)
        self.horizontalLayout_name.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_name)

        self.horizontalLayout_origin_price = QHBoxLayout()
        self.horizontalLayout_origin_price.setSpacing(0)
        self.horizontalLayout_origin_price.setObjectName(u"horizontalLayout_origin_price")
        self.l_original_price = QLabel(ItemsForm)
        self.l_original_price.setObjectName(u"l_original_price")
        self.l_original_price.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.l_original_price.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_origin_price.addWidget(self.l_original_price)

        self.originalPrice = QLineEdit(ItemsForm)
        self.originalPrice.setObjectName(u"originalPrice")
        sizePolicy1.setHeightForWidth(self.originalPrice.sizePolicy().hasHeightForWidth())
        self.originalPrice.setSizePolicy(sizePolicy1)
        self.originalPrice.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.originalPrice.setFrame(False)

        self.horizontalLayout_origin_price.addWidget(self.originalPrice)

        self.horizontalLayout_origin_price.setStretch(0, 1)
        self.horizontalLayout_origin_price.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_origin_price)

        self.horizontalLayout_price = QHBoxLayout()
        self.horizontalLayout_price.setSpacing(0)
        self.horizontalLayout_price.setObjectName(u"horizontalLayout_price")
        self.l_price = QLabel(ItemsForm)
        self.l_price.setObjectName(u"l_price")
        self.l_price.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.l_price.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_price.addWidget(self.l_price)

        self.price = QLineEdit(ItemsForm)
        self.price.setObjectName(u"price")
        sizePolicy1.setHeightForWidth(self.price.sizePolicy().hasHeightForWidth())
        self.price.setSizePolicy(sizePolicy1)
        self.price.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.price.setFrame(False)

        self.horizontalLayout_price.addWidget(self.price)

        self.horizontalLayout_price.setStretch(0, 1)
        self.horizontalLayout_price.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_price)

        self.horizontalLayout_type = QHBoxLayout()
        self.horizontalLayout_type.setSpacing(0)
        self.horizontalLayout_type.setObjectName(u"horizontalLayout_type")
        self.l_type = QLabel(ItemsForm)
        self.l_type.setObjectName(u"l_type")
        self.l_type.setStyleSheet(u"background-color: rgb(60, 60, 60);")
        self.l_type.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_type.addWidget(self.l_type)

        self.type = QLineEdit(ItemsForm)
        self.type.setObjectName(u"type")
        sizePolicy1.setHeightForWidth(self.type.sizePolicy().hasHeightForWidth())
        self.type.setSizePolicy(sizePolicy1)
        self.type.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.type.setFrame(False)

        self.horizontalLayout_type.addWidget(self.type)

        self.horizontalLayout_type.setStretch(0, 1)
        self.horizontalLayout_type.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_type)

        self.horizontalLayout_btns = QHBoxLayout()
        self.horizontalLayout_btns.setSpacing(0)
        self.horizontalLayout_btns.setObjectName(u"horizontalLayout_btns")
        self.btn_ok = QPushButton(ItemsForm)
        self.btn_ok.setObjectName(u"btn_ok")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_ok.sizePolicy().hasHeightForWidth())
        self.btn_ok.setSizePolicy(sizePolicy2)
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

        self.horizontalLayout_btns.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(ItemsForm)
        self.btn_cancel.setObjectName(u"btn_cancel")
        sizePolicy2.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy2)
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

        self.horizontalLayout_btns.addWidget(self.btn_cancel)

        self.horizontalLayout_btns.setStretch(0, 1)
        self.horizontalLayout_btns.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_btns)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)

        self.retranslateUi(ItemsForm)

        QMetaObject.connectSlotsByName(ItemsForm)
    # setupUi

    def retranslateUi(self, ItemsForm):
        ItemsForm.setWindowTitle(QCoreApplication.translate("ItemsForm", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("ItemsForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u0442\u043e\u0432\u0430\u0440\u0435", None))
        self.l_name.setText(QCoreApplication.translate("ItemsForm", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435: ", None))
        self.l_original_price.setText(QCoreApplication.translate("ItemsForm", u"\u0426\u0435\u043d\u0430 \u0437\u0430\u043a\u0443\u043f\u043a\u0438: ", None))
        self.originalPrice.setText("")
        self.l_price.setText(QCoreApplication.translate("ItemsForm", u"\u0426\u0435\u043d\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u044b: ", None))
        self.price.setText("")
        self.l_type.setText(QCoreApplication.translate("ItemsForm", u"\u0415\u0434. \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f: ", None))
        self.type.setText("")
        self.btn_ok.setText(QCoreApplication.translate("ItemsForm", u"\u041e\u043a", None))
        self.btn_cancel.setText(QCoreApplication.translate("ItemsForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

