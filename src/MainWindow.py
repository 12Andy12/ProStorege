from PySide6.QtWidgets import *
from src.forms.MainForm import Ui_MainWindow
from src.AddWindow import AddWindow
from src.AddFolderWindow import FolderWindow
from src.ChangeWindow import ChangeWindow
from src.InfoWindow import InfoWindow
from src.ItemWindow import ItemWindow
from src.PeriodWindow import PeriodWindow
from src.TraderLoginWindow import TraderLoginWindow
from src.OperationWindows import OperationWindow
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from src.DBconector import DataBaseConnector
import pandas
import src.APIconector
import src.resources
import src.styles
from datetime import datetime
import pandas as pd
import os


class PushButton(QtWidgets.QPushButton):
    doubleClick = QtCore.Signal()

    def __init__(self):
        super().__init__()

    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.doubleClick.emit()
            print('doubleClick')

        QtWidgets.QPushButton.mousePressEvent(self, event)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, name="none", admin=True, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        print("Main Window created")
        self.admin = admin
        self.name = name
        self.l_user_name.setText(name)
        if not admin:
            self.tab_setings.setEnabled(False)
            self.tabResultInfo.setEnabled(False)

        self.data_base_connector = DataBaseConnector()
        print("data base connector created")

        self.add_window = AddWindow(self)
        self.folder_window = FolderWindow(self)
        self.item_window = ItemWindow(self)
        self.change_window = ChangeWindow(self)
        self.info_window = InfoWindow(self)

        self.folder_window.hide()
        self.sb_discount_persent.setStyleSheet(src.styles.spin_box_style("30", "rgb(50, 50, 50)"))
        self.sb_discount_persent.valueChanged.connect(lambda: self.on_sum_changed())
        self.tabWidget.setStyleSheet(src.styles.tab_style)
        self.btn_without_terminal.setStyleSheet(src.styles.btn_clicked_style)
        self.btn_clear_basket.setStyleSheet(src.styles.btn_clicked_style)
        self.btn_terminal.setStyleSheet(src.styles.btn_clicked_style)
        self.de_end.setStyleSheet(src.styles.date_edit_style)
        self.de_start.setStyleSheet(src.styles.date_edit_style)
        self.btn_exel.setStyleSheet(src.styles.btn_clicked_style)
        self.btnSearch.setStyleSheet(src.styles.btn_clicked_style)
        self.a_create_exel_with_result.triggered.connect(lambda: PeriodWindow(self))
        self.folders_tree.currentItemChanged.connect(lambda: self.on_dir_changed())
        self.btnSearch.clicked.connect(lambda: self.search(self.searchLine.text()))
        self.btn_clear_basket.clicked.connect(lambda: self.clear_basket())
        self.btn_without_terminal.clicked.connect(lambda: self.pay())
        self.btn_terminal.clicked.connect(lambda: self.pay(pay_with_terminal=True))
        self.de_end.dateChanged.connect(lambda: self.info_table_change())
        self.de_start.dateChanged.connect(lambda: self.info_table_change())
        self.btn_exel.clicked.connect(lambda: self.generate_exel_with_result())

        self.count_parent = {}
        self.root_folder = None
        self.lastRow = None
        self.currentFolder = "root"
        self.path = []
        self.data = src.APIconector.get_all_goods()
        self.folders = []
        self.path.append(self.currentFolder)
        self.freeId = list(range(0, 10000))
        self.old_selectoin_name = "Все категории"
        # self.fillUsedId()
        # self.items_table.
        self.init_table(self.items_table, ['', 'Наименование', 'Цена', 'Закуп. цена', 'Кол-во', ''], [1],
                        [0, 0, 100, 100, 100, 100], self.table_right_clicked)
        self.init_table(self.basket_table, ['', 'Наименование', 'Цена', 'Кол-во'], [1],
                        [0, 0, 200, 300], self.basket_right_clicked)
        if admin:
            self.init_table(self.info_table,
                            ['дата', 'Наименование', 'операция', 'кол-во', 'цена', 'Скидка, %', 'Скидка, руб', 'сумма'],
                            [1],
                            [100, 0, 200, 100, 100, 150, 150, 150], self.info_right_clicked)

            self.init_table(self.traders_table,
                            ['Логин', 'Пароль'],
                            [0, 1],
                            [], self.traders_right_clicked)
        self.de_end.setDate(QDate.currentDate())
        self.load_folders()
        self.draw_folders()
        print("all draw")

    def generate_exel_with_result(self):
        start_date = self.de_start.text()
        end_date = self.de_end.text()
        exel_name = f"отчет за период c {start_date} по {end_date}.xlsx"

        file_path = QFileDialog.getSaveFileName(self, "Open Address book", exel_name, "Exel (*.xlsx)")[0]
        # print(file_path)
        result_data = []
        for i in range(self.info_table.rowCount()):
            line = []
            for j in range(8):
                line.append(self.info_table.item(i, j).text())
            result_data.append(line)

        result_data.append(['Товаров поступило на сумму', self.supply.text()])
        result_data.append(['Товаров проданно на сумму', self.sale.text()])
        result_data.append(['Итого', self.result.text()])
        # print(result_data)
        data = pd.DataFrame(data=result_data,
                            columns=['дата', 'Наименование', 'операция', 'кол-во', 'цена', 'Скидка, %', 'Скидка, руб',
                                     'сумма'])
        data.to_excel(file_path, index=False)

    def info_table_change(self):
        if not self.admin:
            return
        self.info_table.setRowCount(0)
        start_date = self.de_start.text()
        end_date = self.de_end.text()
        data_from_db = self.data_base_connector.request(
            f"SELECT operations.date, goods.name, operations.operation, operations.number, operations.price,\
                     operations.discount_percent, operations.discount_money, operations.result_sum\
                        FROM operations\
                        JOIN goods ON goods.id = operations.good_id;")
        # print(f"data_from_db = {data_from_db}")
        count_supply = 0
        count_sale = 0
        for row in data_from_db:
            # print(row)
            current_datetime = datetime.strptime(row[0], "%d.%m.%Y").date()
            start_datetime = datetime.strptime(start_date, "%d.%m.%Y").date()
            end_datetime = datetime.strptime(end_date, "%d.%m.%Y").date()
            if start_datetime <= current_datetime <= end_datetime:
                self.add_in_table(self.info_table,
                                  [row[0], row[1], row[2], str(row[3]), str(row[4]), str(row[5]), str(row[6]),
                                   str(row[7])])
                if row[2] == "Поступление":
                    count_supply += row[3] * row[4]
                elif row[2] == "Продажа":
                    count_sale += row[3] * row[4]

        self.supply.setText(str(count_supply))
        self.sale.setText(str(count_sale))
        self.result.setText(str(count_sale - count_supply))

    def clear_basket(self):
        self.basket_table.setRowCount(0)
        self.sb_discount_persent.setValue(0)

    def pay(self, pay_with_terminal=False):
        row_count = self.basket_table.rowCount()
        result_positions = []
        for row in range(row_count):
            id = self.basket_table.item(row, 0).text()
            new_position = {}
            for item_id in self.data:
                if item_id == id:
                    new_position = self.data[item_id]
                    break

            name = self.basket_table.item(row, 1).text()
            price = float(self.basket_table.item(row, 2).text())
            count = self.basket_table.cellWidget(row, 3).value()
            discount_percent = self.sb_discount_persent.value()
            all_price = price * count
            sum = all_price * (100 - discount_percent) / 100
            discount_money = round(all_price - sum, 2)
            new_position["quantity"] = count
            new_position["discountPercent"] = discount_percent
            new_position["discountMoney"] = discount_money
            current_count = self.data_base_connector.request(
                f"SELECT number FROM goods WHERE id = '{id}'")[0][0]
            new_count = current_count - count
            self.data_base_connector.request(
                f"UPDATE goods SET number = {new_count} WHERE id = '{id}'")
            date = f"{datetime.now().day:02}.{datetime.now().month:02}.{datetime.now().year}"
            # result_sum = abs(count) * price
            self.data_base_connector.request(
                f"""INSERT INTO operations(good_id, operation, date, number, price, discount_money, discount_percent, result_sum) 
                    VALUES('{id}', 'Продажа', '{date}', '{abs(count)}', '{price}', '{discount_money}', '{discount_percent}', '{sum}')""")

            result_positions.append(new_position)

        self.on_dir_changed()
        if pay_with_terminal:
            src.APIconector.create_order(result_positions)
        self.clear_basket()

    def on_sum_changed(self):
        result_sum = 0
        row_count = self.basket_table.rowCount()
        for row in range(row_count):
            price = self.basket_table.item(row, 2).text()
            count = self.basket_table.cellWidget(row, 3).value()
            result_sum += float(price) * count
        discount_percent = self.sb_discount_persent.value()
        result_sum *= (100 - discount_percent) / 100
        self.le_result_sum.setText(f"{round(result_sum, 2)}")

    def on_dir_changed(self):
        current_dir_name = self.folders_tree.currentItem().text(0)
        current_folder = None
        self.items_table.setRowCount(0)
        for folder in self.folders:
            if folder["name"] == current_dir_name:
                current_folder = folder
                break

        if current_folder is None:
            return

        for item_id in self.data:
            if self.data[item_id]["group_id"] == current_folder['id']:
                self.add_in_item_table(self.data[item_id])

    def add_in_info_table(self, item):
        pass

    def add_in_item_table(self, item):
        count = self.data_base_connector.request(f"SELECT number FROM goods WHERE id = '{item['id']}'")
        if len(count) == 0:
            self.data_base_connector.request(
                f"INSERT INTO goods(id, name, number) VALUES('{item['id']}', '{item['name']}', '0')")
            count = [(0.0,)]

        btn_basket = QPushButton()
        btn_basket.setIcon(QIcon(":iconShoppingCart"))
        btn_basket.setIconSize(QSize(20, 20))
        btn_basket.setStyleSheet(src.styles.btn_basket_style)
        btn_basket.clicked.connect(lambda: self.add_in_basket_table(item))
        self.add_in_table(self.items_table, [item["id"], item["name"], str(item["price"]), str(item["productionCost"]),
                                             str(count[0][0]) + " " + item["unit"], btn_basket])

    def add_in_traders_table(self, traders):
        for trader in traders:
            self.add_in_table(self.traders_table, [trader["name"], trader["password"]])

    def add_in_basket_table(self, item):
        sb_count = QDoubleSpinBox()
        sb_count.setStyleSheet(src.styles.spin_box_style("30", "rgb(50, 50, 50)"))
        sb_count.valueChanged.connect(lambda: self.on_sum_changed())
        self.add_in_table(self.basket_table, [item["id"], item["name"], str(item["price"]), sb_count])

    def add_in_table(self, table, item):
        table.setRowCount(table.rowCount() + 1)
        for i in range(len(item)):
            if isinstance(item[i], str):
                table.setItem(table.rowCount() - 1, i, QtWidgets.QTableWidgetItem(item[i]))
            else:
                table.setCellWidget(table.rowCount() - 1, i, item[i])

    def init_table(self, table, header, stretch_columns, column_width, context_menu):
        table.horizontalHeader().setStyleSheet(src.styles.header_style)
        table.setStyleSheet(src.styles.table_style)
        table.verticalHeader().hide()
        table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger(0))
        table.setColumnCount(len(header))
        table.setRowCount(0)

        table.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        table.setHorizontalHeaderLabels(header)
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Fixed)

        table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        table.customContextMenuRequested.connect(context_menu)

        for i in range(len(header)):
            if i in stretch_columns:
                table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
                table.horizontalHeaderItem(i).setTextAlignment(
                    QtCore.Qt.AlignmentFlag.AlignVCenter | QtCore.Qt.AlignmentFlag.AlignHCenter)
            else:
                table.setColumnWidth(i, column_width[i])

    def info_right_clicked(self, pos):
        pass

    def basket_right_clicked(self, pos):
        item = self.items_table.itemAt(pos)
        menu = QtWidgets.QMenu()
        if item is None:
            return
        else:
            delete_action = QAction("Удалить")
            delete_action.triggered.connect(lambda: self.del_item_from_basket(self.basket_table.currentRow()))
            menu.addAction(delete_action)
        menu.exec_(self.basket_table.viewport().mapToGlobal(pos))

    def table_right_clicked(self, pos):
        if not self.admin:
            return
        item = self.items_table.itemAt(pos)
        menu = QtWidgets.QMenu()
        if item is None:
            add_action = QAction("Создать новый товар")
            add_action.triggered.connect(lambda: self.open_item_window(mode="add"))
            menu.addAction(add_action)
        else:
            operation_action = QAction("Добавить операцию")
            operation_action.triggered.connect(lambda: self.open_operation_window())
            rename_action = QAction("Изменить")
            rename_action.triggered.connect(lambda: self.open_item_window(mode="change"))
            delete_action = QAction("Удалить")
            delete_action.triggered.connect(lambda: self.del_item(self.items_table.currentRow()))
            replace_action = QAction("Переместить в ...")
            replace_action.triggered.connect(lambda: self.open_folder_window(mode="replace_item"))
            menu.addAction(operation_action)
            menu.addAction(rename_action)
            menu.addAction(replace_action)
            menu.addAction(delete_action)
        menu.exec_(self.items_table.viewport().mapToGlobal(pos))

    def traders_right_clicked(self, pos):
        # print("traders right clicked")
        item = self.traders_table.itemAt(pos)
        menu = QtWidgets.QMenu()
        add_action = QAction("Добавить нового кассира")
        add_action.triggered.connect(lambda: self.open_trader_login_window())
        delete_action = QAction("Удалить")
        delete_action.triggered.connect(lambda: print("del trader"))
        if item is None:
            menu.addAction(add_action)
        else:
            menu.addAction(delete_action)
            menu.addAction(add_action)
        menu.exec_(self.traders_table.viewport().mapToGlobal(pos))

    def folder_right_clicked(self, pos):
        item = self.folders_tree.itemAt(pos)
        if item is None or not self.admin:
            return
        folder_name = self.folders_tree.currentItem().text(0)
        menu = QtWidgets.QMenu()
        if self.count_parent[folder_name] < 3:
            add_action = QAction("Создать новую категорию")
            add_action.triggered.connect(lambda: self.open_folder_window(mode="add"))
            menu.addAction(add_action)
        if folder_name != "Все категории":
            rename_action = QAction("Переименовать")
            rename_action.triggered.connect(lambda: self.open_folder_window(mode="rename"))
            delete_action = QAction("Удалить")
            delete_action.triggered.connect(lambda: self.del_folder(self.folders_tree.currentItem().text(0)))
            replace_action = QAction("Переместить в ...")
            replace_action.triggered.connect(lambda: self.open_folder_window(mode="replace_folder"))
            menu.addAction(rename_action)
            menu.addAction(replace_action)
            menu.addAction(delete_action)
        menu.exec_(self.folders_tree.viewport().mapToGlobal(pos))

    def search(self, search_item):
        if search_item == "":
            return
        self.items_table.setRowCount(0)
        result = []
        self.folders_tree.setCurrentItem(self.root_folder)
        for item_id in self.data:
            if search_item.casefold() in self.data[item_id]["name"].casefold():
                result.append(self.data[item_id])
                self.add_in_item_table(self.data[item_id])
        print(f"search result = {result}")

    def open_folder_window(self, mode):
        # folder_window = AddFolderWindow(self)
        self.folder_window.mode = mode
        self.folder_window.current_folder = self.folders_tree.currentItem()
        self.folder_window.le_folder_name.setFocus()
        self.folder_window.show()

    def open_trader_login_window(self):
        trader_login_window = TraderLoginWindow(admin_name=self.name, parent=self)
        # trader_login_window.show()

    def open_item_window(self, mode):
        # folder_window = AddFolderWindow(self)
        self.item_window.mode = mode
        self.item_window.show()

    def open_operation_window(self):
        operation_window = OperationWindow(self)
        current_row = self.items_table.currentRow()
        current_count = self.items_table.item(current_row, 4).text()
        current_name = self.items_table.item(current_row, 1).text()
        current_id = self.items_table.item(current_row, 0).text()
        operation_window.le_current_count.setText(current_count)
        operation_window.le_name.setText(current_name)
        operation_window.le_id.setText(current_id)
        operation_window.show()

    def del_folder(self, deleting_folder):
        parent = self.folders_tree.currentItem()
        for i in range(parent.childCount()):
            parent.removeChild(parent.child(i))

        parent.parent().removeChild(parent)
        self.del_folder_from_API(deleting_folder)

    def del_folder_from_API(self, current_folder_name):
        del_folder = None
        for folder in self.folders:
            if folder["name"] == current_folder_name:
                del_folder = folder
                break

        if del_folder is None:
            return

        src.APIconector.del_folder(del_folder)
        # self.folders = src.APIconector.get_directories()

    def del_item(self, del_item):
        del_item_id = self.items_table.item(del_item, 0).text()
        src.APIconector.del_good(del_item_id)
        self.items_table.removeRow(del_item)

    def del_item_from_basket(self, del_item):
        self.basket_table.removeRow(del_item)

    def load_folders(self):
        self.folders = src.APIconector.get_directories()
        for folder in self.folders:
            for child in folder["children"]:
                self.load_children(child)

    def load_children(self, parent_folder):
        if parent_folder not in self.folders:
            self.folders.append(parent_folder)
        for child in parent_folder["children"]:
            self.load_children(child)

    def draw_folders(self):
        self.folders_tree.clear()
        self.folders_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.folders_tree.customContextMenuRequested.connect(self.folder_right_clicked)

        self.folders_tree.setColumnCount(1)
        self.folders_tree.setHeaderLabels(['Категории'])
        self.folders_tree.setStyleSheet(src.styles.tree_style)

        is_current_item_set = False
        root = QTreeWidgetItem(self.folders_tree)
        root.setText(0, "Все категории")
        root.setIcon(0, QIcon(":/iconFolder.png"))
        self.root_folder = root
        self.count_parent["Все категории"] = 0
        self.folders_tree.setCurrentItem(self.root_folder)
        for folder in self.folders:
            if folder['parent'] is None:
                current_dir = QTreeWidgetItem(root)
                current_dir.setText(0, folder["name"])
                current_dir.setIcon(0, QIcon("images/iconFolder.png"))
                self.count_parent[folder["name"]] = self.count_parent["Все категории"] + 1

                if self.old_selectoin_name == folder["name"]:
                    self.folders_tree.setCurrentItem(current_dir)

                # Устанавливаем все дочерние котегории для текущей
                for child in folder["children"]:
                    self.draw_children(current_dir, child)

    def draw_children(self, parent_node, current_dir):
        current_node = QTreeWidgetItem(parent_node)
        current_node.setText(0, current_dir["name"])
        current_node.setIcon(0, QIcon("images/iconFolder.png"))
        self.count_parent[current_dir["name"]] = self.count_parent[parent_node.text(0)] + 1
        for child in current_dir["children"]:
            self.draw_children(current_node, child)
