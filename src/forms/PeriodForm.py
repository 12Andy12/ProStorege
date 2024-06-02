# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PeriodForm.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_PeriodForm(object):
    def setupUi(self, PeriodForm):
        if not PeriodForm.objectName():
            PeriodForm.setObjectName(u"PeriodForm")
        PeriodForm.resize(433, 211)
        PeriodForm.setStyleSheet(u"font: 12pt \"Times New Roman\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: #b1b1b1;")
        self.verticalLayout_2 = QVBoxLayout(PeriodForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(PeriodForm)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"background-color: rgb(93, 93, 93);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(PeriodForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.date_start = QDateEdit(PeriodForm)
        self.date_start.setObjectName(u"date_start")
        sizePolicy.setHeightForWidth(self.date_start.sizePolicy().hasHeightForWidth())
        self.date_start.setSizePolicy(sizePolicy)
        self.date_start.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.date_start.setMinimumDate(QDate(2000, 1, 1))
        self.date_start.setCalendarPopup(True)
        self.date_start.setDate(QDate(2023, 10, 27))

        self.horizontalLayout_2.addWidget(self.date_start)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(PeriodForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.date_end = QDateEdit(PeriodForm)
        self.date_end.setObjectName(u"date_end")
        sizePolicy.setHeightForWidth(self.date_end.sizePolicy().hasHeightForWidth())
        self.date_end.setSizePolicy(sizePolicy)
        self.date_end.setStyleSheet(u"background-color: rgb(68, 68, 68);")
        self.date_end.setMinimumDate(QDate(2000, 1, 1))
        self.date_end.setCalendarPopup(True)
        self.date_end.setDate(QDate(2023, 10, 27))

        self.horizontalLayout_3.addWidget(self.date_end)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ok = QPushButton(PeriodForm)
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

        self.btn_cancel = QPushButton(PeriodForm)
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
        self.verticalLayout.setStretch(3, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(PeriodForm)

        QMetaObject.connectSlotsByName(PeriodForm)
    # setupUi

    def retranslateUi(self, PeriodForm):
        PeriodForm.setWindowTitle(QCoreApplication.translate("PeriodForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("PeriodForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0435\u0440\u0438\u043e\u0434", None))
        self.label_2.setText(QCoreApplication.translate("PeriodForm", u"\u041d\u0430\u0447\u0430\u043b\u043e", None))
        self.label_3.setText(QCoreApplication.translate("PeriodForm", u"\u041a\u043e\u043d\u0435\u0446", None))
        self.btn_ok.setText(QCoreApplication.translate("PeriodForm", u"\u041e\u043a", None))
        self.btn_cancel.setText(QCoreApplication.translate("PeriodForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

