# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OperationForm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_OperationForm(object):
    def setupUi(self, OperationForm):
        if not OperationForm.objectName():
            OperationForm.setObjectName(u"OperationForm")
        OperationForm.resize(792, 450)
        OperationForm.setStyleSheet(u"font: 14pt \"Times New Roman\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: #b1b1b1;")
        self.verticalLayout_2 = QVBoxLayout(OperationForm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(OperationForm)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"background-color: rgb(93, 93, 93);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(OperationForm)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.le_name = QLabel(OperationForm)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_7.addWidget(self.le_name)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(OperationForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.le_id = QLabel(OperationForm)
        self.le_id.setObjectName(u"le_id")
        self.le_id.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_6.addWidget(self.le_id)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(OperationForm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.le_current_count = QLabel(OperationForm)
        self.le_current_count.setObjectName(u"le_current_count")
        self.le_current_count.setStyleSheet(u"background-color: rgb(65, 65, 65);")

        self.horizontalLayout_5.addWidget(self.le_current_count)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(OperationForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cb_operation_type = QComboBox(OperationForm)
        self.cb_operation_type.addItem("")
        self.cb_operation_type.addItem("")
        self.cb_operation_type.addItem("")
        self.cb_operation_type.setObjectName(u"cb_operation_type")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_operation_type.sizePolicy().hasHeightForWidth())
        self.cb_operation_type.setSizePolicy(sizePolicy1)
        self.cb_operation_type.setFocusPolicy(Qt.NoFocus)
        self.cb_operation_type.setStyleSheet(u"QComboBox\n"
"{\n"
"	background-color: rgb(65, 65, 65);\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color: rgb(70, 70, 70);\n"
"}\n"
"QComboBox:focus {\n"
"    \n"
"}\n"
"QComboBox::item {\n"
"    background: rgb(1, 1, 1);\n"
"}\n"
"QComboBox::item:hover {\n"
"    background: rgb(1, 1, 1);\n"
"}\n"
"QComboBox::item:selected {\n"
"    background: rgb(1, 1, 1);\n"
"}\n"
"QComboBox::drop-down \n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: 0px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(250, 250, 250);    \n"
"    background-color: rgb(100, 100, 100);\n"
"    padding: 10px;\n"
"    border: 2px solid rgb(10, 10, 10);\n"
"    border-radius: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    selection-background: rgb(120, 120, 120);\n"
"}")
        self.cb_operation_type.setEditable(False)
        self.cb_operation_type.setFrame(False)

        self.horizontalLayout_2.addWidget(self.cb_operation_type)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(OperationForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.de_date = QDateEdit(OperationForm)
        self.de_date.setObjectName(u"de_date")
        sizePolicy.setHeightForWidth(self.de_date.sizePolicy().hasHeightForWidth())
        self.de_date.setSizePolicy(sizePolicy)
        self.de_date.setStyleSheet(u"QDateEdit{\n"
"    background-color: rgb(65, 65, 65);\n"
"	border: none\n"
"}\n"
"QDateEdit:hover{\n"
"    background-color: rgb(70, 70, 70);\n"
"}\n"
"QDateEdit::drop-down{\n"
"	background-color: rgb(75, 75, 75);\n"
"} \n"
"QDateEdit::drop-down:hover {\n"
"	bbackground-color: rgb(80, 80, 80);\n"
"}\n"
"QDateEdit::drop-down:pressed {\n"
"	bbackground-color: rgb(120, 120, 120);\n"
"}")
        self.de_date.setWrapping(False)
        self.de_date.setFrame(False)
        self.de_date.setAccelerated(False)
        self.de_date.setKeyboardTracking(True)
        self.de_date.setProperty("showGroupSeparator", False)
        self.de_date.setCalendarPopup(True)
        self.de_date.setDate(QDate(2012, 3, 5))

        self.horizontalLayout_3.addWidget(self.de_date)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(OperationForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(60, 60, 60);")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.dsb_count = QDoubleSpinBox(OperationForm)
        self.dsb_count.setObjectName(u"dsb_count")
        sizePolicy.setHeightForWidth(self.dsb_count.sizePolicy().hasHeightForWidth())
        self.dsb_count.setSizePolicy(sizePolicy)
        self.dsb_count.setStyleSheet(u"background-color: rgb(65, 65, 65);")
        self.dsb_count.setFrame(False)
        self.dsb_count.setMaximum(99999.990000000005239)

        self.horizontalLayout_4.addWidget(self.dsb_count)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_ok = QPushButton(OperationForm)
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

        self.horizontalLayout.addWidget(self.btn_ok)

        self.btn_cancel = QPushButton(OperationForm)
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

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(OperationForm)

        QMetaObject.connectSlotsByName(OperationForm)
    # setupUi

    def retranslateUi(self, OperationForm):
        OperationForm.setWindowTitle(QCoreApplication.translate("OperationForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("OperationForm", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.label_7.setText(QCoreApplication.translate("OperationForm", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.le_name.setText(QCoreApplication.translate("OperationForm", u"\u0418\u043c\u044f", None))
        self.label_6.setText(QCoreApplication.translate("OperationForm", u"id \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.le_id.setText(QCoreApplication.translate("OperationForm", u"id", None))
        self.label_5.setText(QCoreApplication.translate("OperationForm", u"\u0421\u0435\u0439\u0447\u0430\u0441 \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435:", None))
        self.le_current_count.setText(QCoreApplication.translate("OperationForm", u"0", None))
        self.label_2.setText(QCoreApplication.translate("OperationForm", u"\u0422\u0438\u043f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.cb_operation_type.setItemText(0, QCoreApplication.translate("OperationForm", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.cb_operation_type.setItemText(1, QCoreApplication.translate("OperationForm", u"\u041f\u0440\u043e\u0434\u0430\u0436\u0430", None))
        self.cb_operation_type.setItemText(2, QCoreApplication.translate("OperationForm", u"\u0421\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))

        self.cb_operation_type.setCurrentText(QCoreApplication.translate("OperationForm", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("OperationForm", u"\u0414\u0430\u0442\u0430 ", None))
        self.label_4.setText(QCoreApplication.translate("OperationForm", u"\u041a\u043e\u043b-\u0432\u043e", None))
        self.btn_ok.setText(QCoreApplication.translate("OperationForm", u"\u041e\u043a", None))
        self.btn_cancel.setText(QCoreApplication.translate("OperationForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

