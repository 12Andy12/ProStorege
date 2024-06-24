# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainForm.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDate, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import (
    QAbstractItemView,
    QAbstractSpinBox,
    QDateEdit,
    QDoubleSpinBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTabWidget,
    QTableWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 621)
        MainWindow.setStyleSheet(
            'font: 14pt "Times New Roman";\n' "background-color: rgb(50, 50, 50);\n" "color: rgb(220, 220, 220);"
        )
        self.action = QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_Exel = QAction(MainWindow)
        self.action_Exel.setObjectName("action_Exel")
        self.a_create_exel_with_result = QAction(MainWindow)
        self.a_create_exel_with_result.setObjectName("a_create_exel_with_result")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_storage = QWidget()
        self.tab_storage.setObjectName("tab_storage")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_storage)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_storage = QVBoxLayout()
        self.verticalLayout_storage.setSpacing(0)
        self.verticalLayout_storage.setObjectName("verticalLayout_storage")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchLine = QLineEdit(self.tab_storage)
        self.searchLine.setObjectName("searchLine")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLine.sizePolicy().hasHeightForWidth())
        self.searchLine.setSizePolicy(sizePolicy)
        self.searchLine.setStyleSheet("background-color: rgb(70, 70, 70);")
        self.searchLine.setFrame(False)

        self.horizontalLayout_3.addWidget(self.searchLine)

        self.btnSearch = QPushButton(self.tab_storage)
        self.btnSearch.setObjectName("btnSearch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnSearch.sizePolicy().hasHeightForWidth())
        self.btnSearch.setSizePolicy(sizePolicy1)
        self.btnSearch.setStyleSheet("background-color: rgb(70, 70, 70);")

        self.horizontalLayout_3.addWidget(self.btnSearch)

        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_storage.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.folders_tree = QTreeWidget(self.tab_storage)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, "1")
        self.folders_tree.setHeaderItem(__qtreewidgetitem)
        self.folders_tree.setObjectName("folders_tree")
        font = QFont()
        font.setFamilies(["Times New Roman"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.folders_tree.setFont(font)
        self.folders_tree.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.folders_tree.setFrameShape(QFrame.NoFrame)
        self.folders_tree.setLineWidth(0)
        self.folders_tree.setMidLineWidth(0)
        self.folders_tree.setAlternatingRowColors(False)
        self.folders_tree.setIconSize(QSize(16, 16))
        self.folders_tree.setAutoExpandDelay(0)
        self.folders_tree.setIndentation(25)
        self.folders_tree.setAnimated(False)
        self.folders_tree.header().setMinimumSectionSize(100)
        self.folders_tree.header().setDefaultSectionSize(200)

        self.horizontalLayout_5.addWidget(self.folders_tree)

        self.items_table = QTableWidget(self.tab_storage)
        self.items_table.setObjectName("items_table")
        self.items_table.setStyleSheet("")
        self.items_table.setFrameShape(QFrame.NoFrame)
        self.items_table.setLineWidth(1)
        self.items_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.items_table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.items_table.horizontalHeader().setMinimumSectionSize(0)
        self.items_table.verticalHeader().setMinimumSectionSize(0)
        self.items_table.verticalHeader().setDefaultSectionSize(40)

        self.horizontalLayout_5.addWidget(self.items_table)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 4)

        self.verticalLayout_storage.addLayout(self.horizontalLayout_5)

        self.verticalLayout_storage.setStretch(0, 1)
        self.verticalLayout_storage.setStretch(1, 10)

        self.horizontalLayout_4.addLayout(self.verticalLayout_storage)

        self.tabWidget.addTab(self.tab_storage, "")
        self.tab_basket = QWidget()
        self.tab_basket.setObjectName("tab_basket")
        self.verticalLayout = QVBoxLayout(self.tab_basket)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.basket_table = QTableWidget(self.tab_basket)
        self.basket_table.setObjectName("basket_table")
        self.basket_table.setFrameShape(QFrame.NoFrame)
        self.basket_table.horizontalHeader().setMinimumSectionSize(0)
        self.basket_table.verticalHeader().setMinimumSectionSize(0)

        self.verticalLayout.addWidget(self.basket_table)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QLabel(self.tab_basket)
        self.label_4.setObjectName("label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.sb_discount_persent = QDoubleSpinBox(self.tab_basket)
        self.sb_discount_persent.setObjectName("sb_discount_persent")
        self.sb_discount_persent.setFrame(False)
        self.sb_discount_persent.setAlignment(Qt.AlignCenter)
        self.sb_discount_persent.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.sb_discount_persent.setMaximum(100.000000000000000)

        self.horizontalLayout_9.addWidget(self.sb_discount_persent)

        self.horizontalLayout_9.setStretch(0, 4)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 4, 10, 4)
        self.label = QLabel(self.tab_basket)
        self.label.setObjectName("label")
        self.label.setStyleSheet("")

        self.horizontalLayout_7.addWidget(self.label)

        self.le_result_sum = QLabel(self.tab_basket)
        self.le_result_sum.setObjectName("le_result_sum")
        self.le_result_sum.setStyleSheet("")
        self.le_result_sum.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.le_result_sum)

        self.label_6 = QLabel(self.tab_basket)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.horizontalLayout_7.setStretch(0, 4)
        self.horizontalLayout_7.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 5, -1, 5)
        self.btn_without_terminal = QPushButton(self.tab_basket)
        self.btn_without_terminal.setObjectName("btn_without_terminal")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_without_terminal.sizePolicy().hasHeightForWidth())
        self.btn_without_terminal.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.btn_without_terminal)

        self.btn_terminal = QPushButton(self.tab_basket)
        self.btn_terminal.setObjectName("btn_terminal")
        sizePolicy2.setHeightForWidth(self.btn_terminal.sizePolicy().hasHeightForWidth())
        self.btn_terminal.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.btn_terminal)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.btn_clear_basket = QPushButton(self.tab_basket)
        self.btn_clear_basket.setObjectName("btn_clear_basket")
        sizePolicy2.setHeightForWidth(self.btn_clear_basket.sizePolicy().hasHeightForWidth())
        self.btn_clear_basket.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.btn_clear_basket)

        self.verticalLayout.setStretch(0, 9)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.tabWidget.addTab(self.tab_basket, "")
        self.tabResultInfo = QWidget()
        self.tabResultInfo.setObjectName("tabResultInfo")
        self.verticalLayout_2 = QVBoxLayout(self.tabResultInfo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QLabel(self.tabResultInfo)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.de_start = QDateEdit(self.tabResultInfo)
        self.de_start.setObjectName("de_start")
        sizePolicy2.setHeightForWidth(self.de_start.sizePolicy().hasHeightForWidth())
        self.de_start.setSizePolicy(sizePolicy2)
        self.de_start.setMaximumSize(QSize(150, 16777215))
        self.de_start.setCalendarPopup(True)
        self.de_start.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_8.addWidget(self.de_start)

        self.label_3 = QLabel(self.tabResultInfo)
        self.label_3.setObjectName("label_3")
        self.label_3.setMaximumSize(QSize(40, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_3)

        self.de_end = QDateEdit(self.tabResultInfo)
        self.de_end.setObjectName("de_end")
        sizePolicy2.setHeightForWidth(self.de_end.sizePolicy().hasHeightForWidth())
        self.de_end.setSizePolicy(sizePolicy2)
        self.de_end.setMaximumSize(QSize(150, 16777215))
        self.de_end.setCalendarPopup(True)
        self.de_end.setDate(QDate(2025, 1, 1))

        self.horizontalLayout_8.addWidget(self.de_end)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 1)
        self.horizontalLayout_8.setStretch(3, 1)
        self.horizontalLayout_8.setStretch(4, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.info_table = QTableWidget(self.tabResultInfo)
        self.info_table.setObjectName("info_table")
        self.info_table.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_2.addWidget(self.info_table)

        self.btn_exel = QPushButton(self.tabResultInfo)
        self.btn_exel.setObjectName("btn_exel")
        sizePolicy2.setHeightForWidth(self.btn_exel.sizePolicy().hasHeightForWidth())
        self.btn_exel.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.btn_exel)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QLabel(self.tabResultInfo)
        self.label_8.setObjectName("label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_13.addWidget(self.label_8)

        self.supply = QLabel(self.tabResultInfo)
        self.supply.setObjectName("supply")
        self.supply.setMaximumSize(QSize(16777215, 30))
        self.supply.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.supply)

        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_7 = QLabel(self.tabResultInfo)
        self.label_7.setObjectName("label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_12.addWidget(self.label_7)

        self.sale = QLabel(self.tabResultInfo)
        self.sale.setObjectName("sale")
        self.sale.setMaximumSize(QSize(16777215, 30))
        self.sale.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.sale)

        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QLabel(self.tabResultInfo)
        self.label_5.setObjectName("label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_11.addWidget(self.label_5)

        self.result = QLabel(self.tabResultInfo)
        self.result.setObjectName("result")
        self.result.setMaximumSize(QSize(16777215, 30))
        self.result.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.result)

        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.tabWidget.addTab(self.tabResultInfo, "")
        self.tab_setings = QWidget()
        self.tab_setings.setObjectName("tab_setings")
        self.verticalLayout_3 = QVBoxLayout(self.tab_setings)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.tab_setings)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2.setTabPosition(QTabWidget.West)
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName("label_10")

        self.horizontalLayout_15.addWidget(self.label_10)

        self.l_user_name = QLabel(self.tab_2)
        self.l_user_name.setObjectName("l_user_name")

        self.horizontalLayout_15.addWidget(self.l_user_name)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.traders_table = QTableWidget(self.tab_2)
        self.traders_table.setObjectName("traders_table")

        self.verticalLayout_4.addWidget(self.traders_table)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 8)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.btn_color = QPushButton(self.tab_3)
        self.btn_color.setObjectName("btn_color")
        self.btn_color.setGeometry(QRect(40, 70, 301, 51))
        self.btn_font = QPushButton(self.tab_3)
        self.btn_font.setObjectName("btn_font")
        self.btn_font.setGeometry(QRect(40, 370, 301, 41))
        self.btn_font_color = QPushButton(self.tab_3)
        self.btn_font_color.setObjectName("btn_font_color")
        self.btn_font_color.setGeometry(QRect(40, 10, 301, 51))
        self.btn_object_color = QPushButton(self.tab_3)
        self.btn_object_color.setObjectName("btn_object_color")
        self.btn_object_color.setGeometry(QRect(40, 130, 301, 51))
        self.btn_object_hover_color = QPushButton(self.tab_3)
        self.btn_object_hover_color.setObjectName("btn_object_hover_color")
        self.btn_object_hover_color.setGeometry(QRect(40, 190, 301, 51))
        self.btn_object_press_color = QPushButton(self.tab_3)
        self.btn_object_press_color.setObjectName("btn_object_press_color")
        self.btn_object_press_color.setGeometry(QRect(40, 250, 301, 51))
        self.btn_alternative_color = QPushButton(self.tab_3)
        self.btn_alternative_color.setObjectName("btn_alternative_color")
        self.btn_alternative_color.setGeometry(QRect(40, 310, 301, 51))
        self.btn_save_config = QPushButton(self.tab_3)
        self.btn_save_config.setObjectName("btn_save_config")
        self.btn_save_config.setGeometry(QRect(40, 420, 301, 51))
        self.le_example_color = QLabel(self.tab_3)
        self.le_example_color.setObjectName("le_example_color")
        self.le_example_color.setGeometry(QRect(350, 70, 91, 51))
        self.le_example_color.setFrameShape(QFrame.Panel)
        self.le_example_object_color = QLabel(self.tab_3)
        self.le_example_object_color.setObjectName("le_example_object_color")
        self.le_example_object_color.setGeometry(QRect(350, 130, 91, 51))
        self.le_example_object_color.setFrameShape(QFrame.Panel)
        self.le_example_object_color.setFrameShadow(QFrame.Plain)
        self.le_example_object_hover_color = QLabel(self.tab_3)
        self.le_example_object_hover_color.setObjectName("le_example_object_hover_color")
        self.le_example_object_hover_color.setGeometry(QRect(350, 190, 91, 51))
        self.le_example_object_hover_color.setFrameShape(QFrame.Panel)
        self.le_example_object_press_color = QLabel(self.tab_3)
        self.le_example_object_press_color.setObjectName("le_example_object_press_color")
        self.le_example_object_press_color.setGeometry(QRect(350, 250, 91, 51))
        self.le_example_object_press_color.setFrameShape(QFrame.Panel)
        self.le_example_object_alternative_color = QLabel(self.tab_3)
        self.le_example_object_alternative_color.setObjectName("le_example_object_alternative_color")
        self.le_example_object_alternative_color.setGeometry(QRect(350, 310, 91, 51))
        self.le_example_object_alternative_color.setFrameShape(QFrame.Panel)
        self.le_example_font_color = QLabel(self.tab_3)
        self.le_example_font_color.setObjectName("le_example_font_color")
        self.le_example_font_color.setGeometry(QRect(350, 10, 91, 51))
        self.le_example_font_color.setFrameShape(QFrame.Panel)
        self.tabWidget_2.addTab(self.tab_3, "")

        self.verticalLayout_3.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab_setings, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "ProStorage", None))
        self.action.setText(
            QCoreApplication.translate("MainWindow", "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None)
        )
        self.action_Exel.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c Exel \u0444\u0430\u0439\u043b",
                None,
            )
        )
        self.a_create_exel_with_result.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0442\u0447\u0435\u0442 \u0432 exel",
                None,
            )
        )
        self.action_2.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u0434\u043b\u044f \u043e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u0438",
                None,
            )
        )
        self.btnSearch.setText(QCoreApplication.translate("MainWindow", "\u043f\u043e\u0438\u0441\u043a", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_storage),
            QCoreApplication.translate("MainWindow", "\u0421\u043a\u043b\u0430\u0434", None),
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043a\u0438\u0434\u043a\u0430 \u0432 \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u0430\u0445",
                None,
            )
        )
        self.label.setText(QCoreApplication.translate("MainWindow", "\u0418\u0442\u043e\u0433\u043e", None))
        self.le_result_sum.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", " \u0440\u0443\u0431\u043b\u0435\u0439", None))
        self.btn_without_terminal.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0411\u0435\u0437 \u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u0430", None
            )
        )
        self.btn_terminal.setText(
            QCoreApplication.translate("MainWindow", "\u0422\u0435\u0440\u043c\u0438\u043d\u0430\u043b", None)
        )
        self.btn_clear_basket.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u043e\u0440\u0437\u0438\u043d\u0443",
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_basket),
            QCoreApplication.translate("MainWindow", "\u041a\u043e\u0440\u0437\u0438\u043d\u0430", None),
        )
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "\u041f\u0435\u0440\u0438\u043e\u0434 \u0441 ", None)
        )
        self.label_3.setText(QCoreApplication.translate("MainWindow", "\u0434\u043e", None))
        self.btn_exel.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 Exel", None
            )
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u043e\u0432\u0430\u0440\u043e\u0432 \u043f\u043e\u0441\u0442\u0443\u043f\u0438\u043b\u043e \u043d\u0430 \u0441\u0443\u043c\u043c\u0443",
                None,
            )
        )
        self.supply.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0422\u043e\u0432\u0430\u0440\u043e\u0432 \u043f\u0440\u043e\u0434\u0430\u043d\u043e \u043d\u0430 \u0441\u0443\u043c\u043c\u0443",
                None,
            )
        )
        self.sale.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "\u0418\u0442\u043e\u0433", None))
        self.result.setText(QCoreApplication.translate("MainWindow", "0", None))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabResultInfo),
            QCoreApplication.translate(
                "MainWindow", "\u041e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u044c", None
            ),
        )
        self.label_10.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f",
                None,
            )
        )
        self.l_user_name.setText(QCoreApplication.translate("MainWindow", "none", None))
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "\u0410\u043a\u043a\u0430\u0443\u043d\u0442", None),
        )
        self.btn_color.setText(
            QCoreApplication.translate("MainWindow", "\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430", None)
        )
        self.btn_font.setText(QCoreApplication.translate("MainWindow", "\u0428\u0440\u0438\u0444\u0442", None))
        self.btn_font_color.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0426\u0432\u0435\u0442 \u0448\u0440\u0438\u0444\u0442\u0430", None
            )
        )
        self.btn_object_color.setText(
            QCoreApplication.translate(
                "MainWindow", "\u0426\u0432\u0435\u0442 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432", None
            )
        )
        self.btn_object_hover_color.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438",
                None,
            )
        )
        self.btn_object_press_color.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0426\u0432\u0435\u0442 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438",
                None,
            )
        )
        self.btn_alternative_color.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0410\u043b\u044c\u0442\u0435\u0440\u043d\u0430\u0442\u0438\u0432\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430",
                None,
            )
        )
        self.btn_save_config.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f",
                None,
            )
        )
        self.le_example_color.setText("")
        self.le_example_object_color.setText("")
        self.le_example_object_hover_color.setText("")
        self.le_example_object_press_color.setText("")
        self.le_example_object_alternative_color.setText("")
        self.le_example_font_color.setText("")
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(self.tab_3),
            QCoreApplication.translate("MainWindow", "\u0421\u0442\u0438\u043b\u044c", None),
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_setings),
            QCoreApplication.translate("MainWindow", "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None),
        )

    # retranslateUi
