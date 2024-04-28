import sys

from src.UiConverter import convert_ui_to_py
from PySide6.QtWidgets import *
from src.MainWindow import MainWindow
import src.DBconector


if __name__ == '__main__':
    convert_ui_to_py()
    app = QApplication()
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())

