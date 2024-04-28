from PySide6.QtWidgets import *
from src.forms.MainForm import Ui_MainWindow
from src.AddWindow import AddWindow
from src.AddFolderWindow import FolderWindow
from src.ChangeWindow import ChangeWindow
from src.InfoWindow import InfoWindow
from src.ItemWindow import ItemWindow
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from src.DBconector import DataBaseConnector


class PushButton(QtWidgets.QPushButton):
    doubleClick = QtCore.Signal()

    def __init__(self):
        super().__init__()

    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.doubleClick.emit()
            print('doubleClick')

        QtWidgets.QPushButton.mousePressEvent(self, event)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.data_base_connector = DataBaseConnector()

        self.tableStyle = "QTableWidget{\ngridline-color: #666666}"
        self.headerStyle = "::section:pressed {background-color: #323232;\nborder: none;}\n::section {background-color: #323232;\nborder: none;}"
        self.btnCloseStyle = ":hover{\nbackground-color: darkred;\n}\n:pressed{\nbackground-color: red;\n}\nQPushButton{border:none}"
        self.btnChangeStyle = ":hover{\nbackground-color: darkorange;\n}\n:pressed{\nbackground-color: orange;\n}\nQPushButton{border:none}"
        self.btnOpenStyle = ':hover{\nbackground-color: darkgreen;\n}\n:pressed{\nbackground-color: green;\n}\nQPushButton{border:none} '
        self.btnFolderStyle = ':hover{\nbackground-color: darkgreen;\n}\n:pressed{\nbackground-color: green;\n}\nQPushButton{border:none;\ntext-align: left;\nfont: 20px;} '
        self.treeStyle = "QHeaderView::section {background-color: rgb(50, 50, 50);\ncolor: #b1b1b1;\npadding-left: 4px;\nborder: 1px solid #6c6c6c;\n}\n" \
                         "QHeaderView::section:hover{background-color: rgb(50, 50, 50);\nborder: 2px solid #ca8ad8;\ncolor: #fff;\n}\n" \
                         "QTreeView{show-decoration-selected: 1;\noutline: 0;\n}\n" \
                         "QTreeView::item {\ncolor: #b1b1b1;\n}\n" \
                         "QTreeView::item:hover{background: rgba(80, 120, 242, 100);\nborder-top: 1px solid #002cf2;\nborder-bottom: 1px solid #002cf2;\n}\n" \
                         "QTreeView::item:selected {background: rgb(80, 120, 242)}"

        self.add_window = AddWindow(self)
        self.folder_window = FolderWindow(self)
        self.item_window = ItemWindow(self)
        self.change_window = ChangeWindow(self)
        self.info_window = InfoWindow(self)

        self.folder_window.hide()
        # self.ui.tableWidget.horizontalHeader().setStyleSheet(self.headerStyle)
        # self.ui.tableWidget.setStyleSheet(self.tableStyle)
        # self.ui.tableWidget.verticalHeader().hide()


        self.ui.folders_tree.currentItemChanged.connect(lambda: self.on_dir_changed())
        # self.ui.btnAddFolder.clicked.connect(lambda: self.open_window(self.folder_window))
        # self.ui.btnSearch.clicked.connect(lambda: self.search())
        # self.ui.btnBack.clicked.connect(self.fackGoBack)

        self.lastRow = None
        self.currentFolder = "root"
        self.path = []
        self.data = []
        self.folders = []
        self.path.append(self.currentFolder)
        self.freeId = list(range(0, 10000))
        # self.fillUsedId()
        # self.ui.items_table.
        self.init_table()
        self.openFolder("root")

    def on_dir_changed(self):
        current_folder = self.ui.folders_tree.currentItem().text(0)
        items = self.data_base_connector.request(
            f"SELECT * FROM items WHERE folder = '{current_folder}';")
        self.ui.items_table.setRowCount(0)
        for item in items:
            self.add_item(item)

    def add_item(self, item):
        self.ui.items_table.setRowCount(self.ui.items_table.rowCount() + 1)
        for i in range(self.ui.items_table.columnCount() - 1):
            self.ui.items_table.setItem(self.ui.items_table.rowCount() - 1, i, QtWidgets.QTableWidgetItem(str(item[i])))
        self.ui.items_table.setItem(self.ui.items_table.rowCount() - 1, self.ui.items_table.columnCount() - 1,
                                    QtWidgets.QTableWidgetItem(
                                        f"{item[self.ui.items_table.columnCount() - 1]}  {item[self.ui.items_table.columnCount()]}"))

    def init_table(self):
        self.ui.items_table.horizontalHeader().setStyleSheet(self.headerStyle)
        self.ui.items_table.setStyleSheet(self.tableStyle)
        self.ui.items_table.verticalHeader().hide()
        self.ui.items_table.setColumnCount(5)

        self.ui.items_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Fixed)
        self.ui.items_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.ui.items_table.setColumnWidth(0, 60)
        self.ui.items_table.setColumnWidth(2, 100)
        self.ui.items_table.setColumnWidth(3, 100)
        self.ui.items_table.setColumnWidth(4, 100)

        self.ui.items_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger(0))

        self.ui.items_table.setHorizontalHeaderLabels(
            ['id', 'Наименование', 'Цена', 'Закуп. цена', 'Кол-во'])
        self.ui.items_table.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        # self.tableWidget.horizontalHeaderItem(1).setAligment(Qt.AlignmentFlag.AlignCenter)
        self.ui.items_table.horizontalHeaderItem(1).setTextAlignment(
            QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.ui.items_table.setRowCount(0)
        self.ui.items_table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.items_table.customContextMenuRequested.connect(self.table_right_clicked)

    def open_window(self, window):
        window.show()

    def openFolder(self, newFolder):

        self.data = []
        self.folders = []
        self.loadDB()
        self.load_folders()
        # self.loadTable()

    def table_right_clicked(self, pos):
        item = self.ui.items_table.itemAt(pos)
        menu = QtWidgets.QMenu()
        if item is None:
            add_action = QAction("Создать новый товар")
            add_action.triggered.connect(lambda: self.open_item_window(mode="add"))
            menu.addAction(add_action)
        else:
            rename_action = QAction("Изменить")
            rename_action.triggered.connect(lambda: self.open_item_window(mode="change"))
            delete_action = QAction("Удалить")
            delete_action.triggered.connect(lambda: self.del_item(self.ui.items_table.currentRow()))
            menu.addAction(rename_action)
            menu.addAction(delete_action)
        menu.exec_(self.ui.items_table.viewport().mapToGlobal(pos))

    def folder_right_clicked(self, pos):
        item = self.ui.folders_tree.itemAt(pos)
        if item is None:
            return
        folder_name = self.ui.folders_tree.currentItem().text(0)
        menu = QtWidgets.QMenu()

        add_action = QAction("Создать новую категорию")
        add_action.triggered.connect(lambda: self.open_folder_window(mode="add"))
        menu.addAction(add_action)
        if folder_name != "root":
            rename_action = QAction("Переименовать")
            rename_action.triggered.connect(lambda: self.open_folder_window(mode="rename"))
            delete_action = QAction("Удалить")
            delete_action.triggered.connect(lambda: self.del_folder(self.ui.folders_tree.currentItem().text(0)))
            menu.addAction(rename_action)
            menu.addAction(delete_action)
        menu.exec_(self.ui.folders_tree.viewport().mapToGlobal(pos))

    def open_folder_window(self, mode):
        # folder_window = AddFolderWindow(self)
        self.folder_window.mode = mode
        self.folder_window.current_folder = self.ui.folders_tree.currentItem()
        self.folder_window.le_folder_name.setFocus()
        self.folder_window.show()

    def open_item_window(self, mode):
        # folder_window = AddFolderWindow(self)
        self.item_window.mode = mode
        self.item_window.show()

    def del_folder(self, deleting_folder):
        parent = self.ui.folders_tree.currentItem()
        for i in range(parent.childCount()):
            parent.removeChild(parent.child(i))

        parent.parent().removeChild(parent)
        self.del_folder_db(deleting_folder)

    def del_item(self, del_item):
        self.del_item_db(self.ui.items_table.item(del_item, 0).text())
        self.ui.items_table.removeRow(del_item)

    def del_item_db(self, del_item_id):
        self.data_base_connector.request(
            f"DELETE FROM items WHERE id = '{del_item_id}';")


    def del_folder_db(self, deleting_folder):
        self.data_base_connector.request(
            f"DELETE FROM folders WHERE name = '{deleting_folder}';")
        children = self.data_base_connector.request(
            f"SELECT name FROM folders WHERE parent_name = '{deleting_folder}';")
        for child in children:
            self.del_folder_db(child[0])

        # self.load_folders()

    def load_folders(self):
        self.ui.folders_tree.clear()
        self.ui.folders_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.folders_tree.customContextMenuRequested.connect(self.folder_right_clicked)
        # self.ui.folders_tree.selectionModel().selectionChanged.connect(self.onSelectionChanged)
        self.folders = self.data_base_connector.request(f"SELECT name, parent_name FROM folders")

        self.ui.folders_tree.setColumnCount(1)
        self.ui.folders_tree.setHeaderLabels(['Категории'])
        # self.ui.folders_tree.header().hide()
        self.ui.folders_tree.setStyleSheet(self.treeStyle)
        root = QTreeWidgetItem(self.ui.folders_tree)
        root.setText(0, "root")
        root.setIcon(0, QIcon("images/iconFolder.png"))
        self.ui.folders_tree.setCurrentItem(root)
        self.set_child(root)

    def onSelectionChanged(self):
        print("изменение")

    def set_child(self, node):

        for folder in self.folders:
            if folder[1] == node.text(0):
                child = QTreeWidgetItem(node)
                child.setText(0, folder[0])
                child.setIcon(0, QIcon("images/iconFolder.png"))
                self.set_child(child)

    def loadDB(self):
        actual_folders = self.data_base_connector.request(
            f"SELECT name FROM folders WHERE parent_name = '{self.currentFolder}';")
        self.folders.extend(actual_folders)
        actual_items = self.data_base_connector.request(
            f"SELECT id, name, price, original_price, count, type FROM items WHERE folder = '{self.currentFolder}';")
        self.data.extend(actual_items)
        # connection = sqlite3.connect("ItemDataBase.db")
        # cur = connection.cursor()
        #
        # for row in cur.execute("SELECT * FROM FolderControl WHERE parentName = ?", (self.currentFolder,)):
        #     self.folders.append(row[0])
        #
        # for row in cur.execute("SELECT * FROM ItemControl WHERE folder = ?", (self.currentFolder,)):
        #     thisData = []
        #     for i in range(6):
        #         thisData.append(row[i])
        #     self.data.append(thisData)
