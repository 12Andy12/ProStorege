# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainForm.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(701, 401)
        MainWindow.setStyleSheet(u"font: 12pt \"Times New Roman\";\n"
"background-color: rgb(50, 50, 50);\n"
"color: #b1b1b1;")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_Exel = QAction(MainWindow)
        self.action_Exel.setObjectName(u"action_Exel")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchLine = QLineEdit(self.centralwidget)
        self.searchLine.setObjectName(u"searchLine")

        self.horizontalLayout_3.addWidget(self.searchLine)

        self.btnSearch = QPushButton(self.centralwidget)
        self.btnSearch.setObjectName(u"btnSearch")

        self.horizontalLayout_3.addWidget(self.btnSearch)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.folders_tree = QTreeWidget(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.folders_tree.setHeaderItem(__qtreewidgetitem)
        self.folders_tree.setObjectName(u"folders_tree")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.folders_tree.setFont(font)
        self.folders_tree.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.folders_tree)

        self.items_table = QTableWidget(self.centralwidget)
        self.items_table.setObjectName(u"items_table")
        self.items_table.setStyleSheet(u"")
        self.items_table.setFrameShape(QFrame.NoFrame)
        self.items_table.horizontalHeader().setMinimumSectionSize(40)
        self.items_table.verticalHeader().setDefaultSectionSize(40)

        self.horizontalLayout_5.addWidget(self.items_table)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.btnAdd = QPushButton(self.centralwidget)
        self.btnAdd.setObjectName(u"btnAdd")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)
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

        self.verticalLayout_2.addWidget(self.btnAdd)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 701, 25))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_Exel)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProStorage", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_Exel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c Exel \u0444\u0430\u0439\u043b", None))
        self.btnSearch.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0438\u0441\u043a", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Add Item", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u043f\u043e\u0440\u0442", None))
    # retranslateUi

