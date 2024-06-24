# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TraderLoginForm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout


class Ui_TraderLoginForm(object):
    def setupUi(self, TraderLoginForm):
        if not TraderLoginForm.objectName():
            TraderLoginForm.setObjectName("TraderLoginForm")
        TraderLoginForm.resize(580, 262)
        TraderLoginForm.setStyleSheet(
            'font: 14pt "Times New Roman";\n' "background-color: rgb(50, 50, 50);\n" "color: rgb(220, 220, 220);"
        )
        self.verticalLayout = QVBoxLayout(TraderLoginForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(TraderLoginForm)
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: rgb(60, 60, 60);")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l1 = QLabel(TraderLoginForm)
        self.l1.setObjectName("l1")

        self.horizontalLayout.addWidget(self.l1)

        self.le_trader_name = QLineEdit(TraderLoginForm)
        self.le_trader_name.setObjectName("le_trader_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_trader_name.sizePolicy().hasHeightForWidth())
        self.le_trader_name.setSizePolicy(sizePolicy)
        self.le_trader_name.setMinimumSize(QSize(0, 0))
        self.le_trader_name.setMaximumSize(QSize(400, 200))
        self.le_trader_name.setStyleSheet("background-color: rgb(55, 55, 55);")
        self.le_trader_name.setFrame(False)

        self.horizontalLayout.addWidget(self.le_trader_name)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l2 = QLabel(TraderLoginForm)
        self.l2.setObjectName("l2")

        self.horizontalLayout_2.addWidget(self.l2)

        self.le_trader_password = QLineEdit(TraderLoginForm)
        self.le_trader_password.setObjectName("le_trader_password")
        sizePolicy.setHeightForWidth(self.le_trader_password.sizePolicy().hasHeightForWidth())
        self.le_trader_password.setSizePolicy(sizePolicy)
        self.le_trader_password.setStyleSheet("background-color: rgb(55, 55, 55);")
        self.le_trader_password.setFrame(False)

        self.horizontalLayout_2.addWidget(self.le_trader_password)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.l_error = QLabel(TraderLoginForm)
        self.l_error.setObjectName("l_error")

        self.verticalLayout.addWidget(self.l_error)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_save_trader = QPushButton(TraderLoginForm)
        self.btn_save_trader.setObjectName("btn_save_trader")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_save_trader.sizePolicy().hasHeightForWidth())
        self.btn_save_trader.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.btn_save_trader)

        self.btn_cancel = QPushButton(TraderLoginForm)
        self.btn_cancel.setObjectName("btn_cancel")
        sizePolicy1.setHeightForWidth(self.btn_cancel.sizePolicy().hasHeightForWidth())
        self.btn_cancel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.btn_cancel)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)

        self.retranslateUi(TraderLoginForm)

        QMetaObject.connectSlotsByName(TraderLoginForm)

    # setupUi

    def retranslateUi(self, TraderLoginForm):
        TraderLoginForm.setWindowTitle(QCoreApplication.translate("TraderLoginForm", "Form", None))
        self.label.setText(
            QCoreApplication.translate(
                "TraderLoginForm",
                "\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u043a\u0430\u0441\u0441\u0438\u0440\u0430",
                None,
            )
        )
        self.l1.setText(QCoreApplication.translate("TraderLoginForm", "\u041b\u043e\u0433\u0438\u043d", None))
        self.l2.setText(QCoreApplication.translate("TraderLoginForm", "\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.l_error.setText("")
        self.btn_save_trader.setText(
            QCoreApplication.translate("TraderLoginForm", "\u0414\u043e\u0431\u0430\u0432\u0442\u044c", None)
        )
        self.btn_cancel.setText(
            QCoreApplication.translate("TraderLoginForm", "\u041e\u0442\u043c\u0435\u043d\u0430", None)
        )

    # retranslateUi
