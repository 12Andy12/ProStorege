# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginForm.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(354, 300)
        LoginWindow.setMinimumSize(QSize(200, 150))
        LoginWindow.setMaximumSize(QSize(400, 300))
        LoginWindow.setStyleSheet(u"font: 14pt \"Times New Roman\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: #b1b1b1;")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.l_name = QLabel(self.centralwidget)
        self.l_name.setObjectName(u"l_name")

        self.horizontalLayout.addWidget(self.l_name)

        self.le_name = QLineEdit(self.centralwidget)
        self.le_name.setObjectName(u"le_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_name.sizePolicy().hasHeightForWidth())
        self.le_name.setSizePolicy(sizePolicy)
        self.le_name.setMinimumSize(QSize(0, 0))
        self.le_name.setMaximumSize(QSize(400, 200))
        self.le_name.setFrame(False)

        self.horizontalLayout.addWidget(self.le_name)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.l_password = QLabel(self.centralwidget)
        self.l_password.setObjectName(u"l_password")

        self.horizontalLayout_2.addWidget(self.l_password)

        self.le_password = QLineEdit(self.centralwidget)
        self.le_password.setObjectName(u"le_password")
        sizePolicy.setHeightForWidth(self.le_password.sizePolicy().hasHeightForWidth())
        self.le_password.setSizePolicy(sizePolicy)
        self.le_password.setFrame(False)

        self.horizontalLayout_2.addWidget(self.le_password)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.l_error = QLabel(self.centralwidget)
        self.l_error.setObjectName(u"l_error")

        self.verticalLayout_2.addWidget(self.l_error)

        self.btn_login = QPushButton(self.centralwidget)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.btn_login)

        self.btn_new_account = QPushButton(self.centralwidget)
        self.btn_new_account.setObjectName(u"btn_new_account")
        sizePolicy1.setHeightForWidth(self.btn_new_account.sizePolicy().hasHeightForWidth())
        self.btn_new_account.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.btn_new_account)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_2.setStretch(4, 2)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.l_name.setText(QCoreApplication.translate("LoginWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.l_password.setText(QCoreApplication.translate("LoginWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.l_error.setText("")
        self.btn_login.setText(QCoreApplication.translate("LoginWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.btn_new_account.setText(QCoreApplication.translate("LoginWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
    # retranslateUi

