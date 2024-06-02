from PySide6.QtWidgets import *
from src.forms.ItemForm import Ui_ItemsForm
import src.DBconector
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import src.APIconector


class ItemWindow(QtWidgets.QWidget, Ui_ItemsForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mode = "add"
        self.parent = parent
        self.old_pos = None

        self.hide()
        self.move(300, 300)
        self.setupUi(self)
        self.btn_ok.clicked.connect(lambda: self.selector())
        self.btn_cancel.clicked.connect(lambda: self.hide())

    def selector(self):
        if not self.is_correct():
            return
        current_folder_name = self.parent.folders_tree.currentItem().text(0)

        current_folder_id = None
        for folder in self.parent.folders:
            if folder["name"] == current_folder_name:
                current_folder_id = folder["id"]
                break
        if current_folder_id is None:
            return

        if self.mode == "add":
            new_id = src.APIconector.generate_id()
            name = self.itemName.text()
            original_price = self.originalPrice.text()
            price = self.price.text()
            # count = self.count.text()
            type = self.type.text()
            src.APIconector.add_good(new_id, name, original_price, price, type, current_folder_id)
            self.parent.data = src.APIconector.get_all_goods()
        elif self.mode == "change":
            name = self.itemName.text()
            original_price = self.originalPrice.text()
            price = self.price.text()
            # count = self.count.text()
            type = self.type.text()
            current_row = self.parent.items_table.currentRow()
            change_item_id = self.parent.items_table.item(current_row, 0).text()
            for item_id in self.parent.data:
                if item_id == change_item_id:
                    self.parent.data[item_id]["name"] = name
                    self.parent.data[item_id]["price"] = price
                    self.parent.data[item_id]["unit"] = type
                    self.parent.data[item_id]["productionCost"] = original_price
                    self.parent.data[item_id]["paymentMethodType"] = 4
                    self.parent.data[item_id]["subject"] = 1
                    src.APIconector.update_good(self.parent.data[item_id])

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
