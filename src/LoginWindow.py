from src.forms.LoginForm import Ui_LoginWindow
from src.MainWindow import MainWindow
from src.UserController import save_users, load_users
from PySide6 import QtWidgets
import src.styles as style


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        style.load_config()
        self.parent = parent
        self.setStyleSheet(style.main_style())
        self.l_name.setStyleSheet(style.background_color("main_background_color"))
        self.l_password.setStyleSheet(style.background_color("main_background_color"))
        self.le_password.setStyleSheet(style.background_color("main_background_color"))
        self.le_name.setStyleSheet(style.background_color("main_background_color"))
        self.btn_login.setStyleSheet(style.btn_clicked_style())
        self.btn_new_account.setStyleSheet(style.btn_clicked_style())
        self.btn_login.clicked.connect(lambda: self.login())
        self.btn_new_account.clicked.connect(lambda: self.new_user())
        self.users = []
        self.users = load_users(self.users)

    def new_user(self):
        new_user_name: str = self.le_name.text()
        new_user_password: str = self.le_password.text()
        if new_user_name == "":
            self.l_error.setText("логин не может быть пустым")
            return
        if new_user_password == "":
            self.l_error.setText("пароль не может быть пустым")
            return
        self.l_error.setText("")
        for user in self.users:
            if new_user_name == user["name"]:
                self.l_error.setText("логин уже существует")
                return

        new_user = {"name": new_user_name, "password": new_user_password, "traders": []}
        self.users.append(new_user)
        save_users(self.users)

    def login(self):
        print(f"all users = {self.users}")
        user_name = self.le_name.text()
        user_password = self.le_password.text()
        for user in self.users:
            if user_name == user["name"]:
                self.l_error.setText("")
                if user_password == user["password"]:
                    self.l_error.setText("")
                    window = MainWindow(user["name"])
                    window.add_in_traders_table(user["traders"])
                    window.showMaximized()
                    self.close()
                else:
                    self.l_error.setText("Неверный пароль")
            else:
                self.l_error.setText("Неверный логин")

            for trader in user["traders"]:
                if user_name == trader["name"]:
                    if user_password == trader["password"]:
                        self.l_error.setText("")
                        window = MainWindow(trader["name"], False)
                        window.showMaximized()
                        self.close()
                    else:
                        self.l_error.setText("Неверный пароль")

        self.l_error.setText("Неверный логин")
