from PySide6.QtWidgets import *
from src.forms.OperationForm import Ui_OperationForm
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import src.styles as styles


class OperationWindow(QtWidgets.QWidget, Ui_OperationForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.old_pos = None
        self.hide()
        self.setupUi(self)
        self.setStyleSheet(styles.main_style())
        self.parent = parent
        self.move(300, 300)
        self.btn_ok.clicked.connect(lambda: self.add_operation())
        self.btn_cancel.clicked.connect(lambda: self.close())
        self.btn_ok.setStyleSheet(styles.btn_clicked_style())
        self.btn_cancel.setStyleSheet(styles.btn_clicked_style())
        self.label.setStyleSheet(styles.background_color("alternative_background_color"))
        self.l_name.setStyleSheet(styles.background_color("alternative_background_color"))
        self.l_id.setStyleSheet(styles.background_color("alternative_background_color"))
        self.l_date.setStyleSheet(styles.background_color("alternative_background_color"))
        self.l_count.setStyleSheet(styles.background_color("alternative_background_color"))
        self.l_operation_type.setStyleSheet(styles.background_color("alternative_background_color"))
        self.l_current_count.setStyleSheet(styles.background_color("alternative_background_color"))
        self.cb_operation_type.setStyleSheet(styles.combo_box_style())
        self.de_date.setStyleSheet(styles.date_edit_style())
        self.dsb_count.setStyleSheet(styles.spin_box_style("30", "rgb(65, 65, 65)"))
        self.le_id.setStyleSheet(styles.background_color("alternative_background_color"))
        self.le_name.setStyleSheet(styles.background_color("alternative_background_color"))
        self.le_current_count.setStyleSheet(styles.background_color("alternative_background_color"))

    def add_operation(self):
        self.le_name.text()
        id = self.le_id.text()
        current_count = self.parent.data_base_connector.request(f"SELECT number FROM goods WHERE id = '{id}'")[0][0]
        add_count = float(self.dsb_count.text().replace(",", "."))
        operation = self.cb_operation_type.currentText()
        date = self.de_date.text()
        price = self.parent.data[id]["productionCost"]

        if operation != "Поступление":
            add_count *= -1
            price = self.parent.data[id]["price"]

        if operation == "Списание":
            price = 0

        new_count = current_count + add_count
        self.parent.data_base_connector.request(f"UPDATE goods SET number = {new_count} WHERE id = '{id}'")

        self.parent.data_base_connector.request(
            f"INSERT INTO operations(good_id, operation, date, number, price, result_sum) VALUES('{id}', '{operation}', '{date}', '{abs(add_count)}', '{price}', '{price * abs(add_count)}')"
        )

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
