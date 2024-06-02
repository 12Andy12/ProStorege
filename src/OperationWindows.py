from PySide6.QtWidgets import *
from src.forms.OperationForm import Ui_OperationForm
import src.DBconector
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import src.APIconector
import src.resources
import src.styles

class OperationWindow(QtWidgets.QWidget, Ui_OperationForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.old_pos = None
        self.hide()
        self.setupUi(self)
        self.parent = parent
        self.move(300, 300)
        self.btn_ok.clicked.connect(lambda: self.add_operation())
        self.btn_cancel.clicked.connect(lambda: self.close())
        self.cb_operation_type.setStyleSheet(src.styles.combo_box_style)
        self.de_date.setStyleSheet(src.styles.date_edit_style)
        self.dsb_count.setStyleSheet(src.styles.spin_box_style("30", "rgb(65, 65, 65)"))

    def add_operation(self):
        name = self.le_name.text()
        id = self.le_id.text()
        current_count = self.parent.data_base_connector.request(
            f"SELECT number FROM goods WHERE id = '{id}'")[0][0]
        add_count = float(self.dsb_count.text().replace(',', '.'))
        operation = self.cb_operation_type.currentText()
        date = self.de_date.text()
        price = self.parent.data[id]["productionCost"]

        if operation != "Поступление":
            add_count *= -1
            price = self.parent.data[id]["price"]

        if operation == "Списание":
            price = 0

        new_count = current_count + add_count
        self.parent.data_base_connector.request(
            f"UPDATE goods SET number = {new_count} WHERE id = '{id}'")

        self.parent.data_base_connector.request(
            f"INSERT INTO operations(good_id, operation, date, number, price) VALUES('{id}', '{operation}', '{date}', '{abs(add_count)}', '{price}')")

        self.parent.on_dir_changed()
        self.close()

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
