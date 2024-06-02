import pickle

from src.forms.TraderLoginForm import Ui_TraderLoginForm

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import src.styles as style

USERS_PATH = "users.bin"


class TraderLoginWindow(QtWidgets.QWidget, Ui_TraderLoginForm):
    def __init__(self, admin_name, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.old_pos = None
        self.parent = parent
        self.admin_name = admin_name
        self.btn_save_trader.setStyleSheet(style.btn_clicked_style)
        self.btn_cancel.setStyleSheet(style.btn_clicked_style)
        self.btn_cancel.clicked.connect(lambda: self.close())
        self.btn_save_trader.clicked.connect(lambda: self.on_save())
        self.users = []
        self.load_users()
        self.show()
        print(f"TraderLoginWindow init with {self.users}")

    def on_save(self):
        trader_name = self.le_trader_name.text()
        trader_password = self.le_trader_password.text()
        for user in self.users:
            if trader_name == user["name"]:
                self.l_error.setText("Логин уже занят")
                return
                for trader in user["traders"]:
                    if trader_name == trader:
                        self.l_error.setText("Логин уже занят")
                        return
        if trader_password == "":
            self.l_error.setText("Пароль не может быть пустым")
        self.l_error.setText("")
        new_trader = {
            "name": trader_name,
            "password": trader_password
        }
        for user in self.users:
            if user["name"] == self.admin_name:
                user["traders"].append(new_trader)
        self.parent.add_in_table(self.parent.traders_table, [trader_name, trader_password])
        self.save_users()
        self.close()

    def load_users(self):
        try:
            with open(USERS_PATH, "rb") as file:
                self.users = pickle.load(file)
        except FileNotFoundError:
            self.save_users()
        except Exception as err:
            print(f"Exception on loading events from path = {USERS_PATH}. {err}")

    def save_users(self):
        try:
            with open(USERS_PATH, "wb") as file:
                pickle.dump(self.users, file)
        except Exception as err:
            print(f"Exception on saving events to path = {USERS_PATH}. {err}")

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