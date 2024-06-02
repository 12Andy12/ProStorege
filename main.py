import sys

from src.UiConverter import convert_ui_to_py
from PySide6.QtWidgets import *
from src.MainWindow import MainWindow
from src.LoginWindow import LoginWindow
import src.APIconector
#python -m nuitka --windows-disable-console --follow-imports --windows-icon-from-ico=main_icon.ico main.py
if __name__ == '__main__':
    # print(src.APIconector.time_now())
    # src.APIconector.get_all_orders()
    # convert_ui_to_py()

    #
    app = QApplication()
    # window = MainWindow()
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec())
