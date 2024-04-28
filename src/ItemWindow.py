from PySide6.QtWidgets import *
from src.forms.ItemForm import Ui_ItemsForm
import src.DBconector
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class ItemWindow(QtWidgets.QWidget, Ui_ItemsForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mode = "add"
        self.parent = parent
        self.old_pos = None
        self.hide()
        self.setupUi(self)
        self.btn_ok.clicked.connect(lambda: self.selector())
        self.btn_cancel.clicked.connect(lambda: self.hide())

    def selector(self):
        if not self.is_correct():
            return
        dir_name = self.parent.ui.folders_tree.currentItem().text(0)
        print(f"[INFO] ItemWidget ok clicked in folder: {dir_name}")
        if self.mode == "add":
            name = self.itemName.text()
            original_price = self.originalPrice.text()
            price = self.price.text()
            count = self.count.text()
            type = self.type.text()
            self.parent.data_base_connector.request(
                f"INSERT INTO items(name, price, original_price, count, folder, type) "
                f"VALUES('{name}', '{price}', '{original_price}', '{count}', '{dir_name}', '{type}')")
            self.parent.data_base_connector.request(f"CREATE INDEX id ON items({name})")

        elif self.mode == "change":
            name = self.itemName.text()
            original_price = self.originalPrice.text()
            price = self.price.text()
            count = self.count.text()
            type = self.type.text()
            self.parent.data_base_connector.request(
                f"UPDATE items SET "
                f"name = '{name}', "
                f"price = '{price}', "
                f"original_price = '{original_price}', "
                f"count = '{count}', "
                f"folder = '{dir_name}', "
                f"type = '{type}' "
                f"WHERE "
                f"id = {self.parent.ui.items_table.item(self.parent.ui.items_table.currentRow(), 0).text()}")

        self.parent.on_dir_changed()
        self.hide()

    def is_correct(self):
        error_msg = "no error"
        if self.itemName.text() == "":
            error_msg = "Поле с наименованием товара не может быть пустым"
        if self.originalPrice.text() == "":
            error_msg = "Поле с ценой закупки не может быть пустым"
        if self.price.text() == "":
            error_msg = "Поле с ценой товара не может быть пустым"
        if self.count.text() == "":
            error_msg = "Поле с кол-вом товара не может быть пустым"
        if self.type.text() == "":
            error_msg = "Поле с ед. измерения количества товара не может быть пустым"
        if error_msg == "no error":
            return True
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Внимание")
            msg.setText(error_msg)
            msg.setIcon(QMessageBox.Warning)
            returnValue = msg.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')
            return False

    # вызывается при нажатии кнопки мыши
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = event.pos()
            # self.setFocus()

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None
            # self.setFocus()

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)
