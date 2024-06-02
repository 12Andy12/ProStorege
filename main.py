import sys

from src.UiConverter import convert_ui_to_py
from PySide6.QtWidgets import *
from src.MainWindow import MainWindow
import src.APIconector

if __name__ == '__main__':
    # print(src.APIconector.time_now())
    # src.APIconector.get_all_orders()
    # convert_ui_to_py()

    #
    app = QApplication()
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
