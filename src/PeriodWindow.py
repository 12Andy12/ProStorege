from PySide6.QtWidgets import *
from src.forms.PeriodForm import Ui_PeriodForm
import src.DBconector
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys
import pandas as pd
import src.APIconector
import os
import openpyxl
from datetime import datetime
import src.styles


class PeriodWindow(QtWidgets.QWidget, Ui_PeriodForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.ui = Ui_AddDirectoryForm()
        self.setupUi(self)
        self.move(300, 300)
        self.parent = parent
        self.old_pos = None
        self.btn_ok.clicked.connect(lambda: self.generate_exel_with_result())
        self.btn_cancel.clicked.connect(lambda: self.close())
        self.date_start.setStyleSheet(src.styles.date_edit_style)
        self.date_end.setStyleSheet(src.styles.date_edit_style)
        self.show()

    def generate_exel_with_result(self):
        start_date = self.date_start.text()
        end_date = self.date_end.text()
        exel_name = f"отчет за период c {start_date} по {end_date}.xlsx"
        data_from_db = self.parent.data_base_connector.request(
            f"SELECT goods.name, operations.date, operations.operation, operations.number, operations.price\
                FROM operations\
                JOIN goods ON goods.id = operations.good_id;")
        result_data = []
        count_supply = 0
        count_sale = 0
        count_miss = 0
        for row in data_from_db:
            print(row)
            current_datetime = datetime.strptime(row[1], "%d.%m.%Y").date()
            start_datetime = datetime.strptime(start_date, "%d.%m.%Y").date()
            end_datetime = datetime.strptime(end_date, "%d.%m.%Y").date()
            if start_datetime <= current_datetime <= end_datetime:
                result_data.append(row)
                if row[2] == "Поступление":
                    count_supply += row[3] * row[4]
                elif row[2] == "Продажа":
                    count_sale += row[3] * row[4]

        row_supply = ['Товаров поступило на сумму', count_supply]
        row_sale = ['Товаров проданно на сумму', count_sale]
        row_result = ['Итого', count_sale - count_supply]
        result_data.append(row_supply)
        result_data.append(row_sale)
        result_data.append(row_result)
        data = pd.DataFrame(data=result_data, columns=['Наименование товара', 'Дата', 'Тип операции', 'Кол-во', 'Цена'])
        path = os.path.dirname(__file__) + "\\" + exel_name
        data.to_excel(path, index=False)
        self.close()

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
