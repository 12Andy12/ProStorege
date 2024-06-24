import sys

from PySide6.QtWidgets import QApplication
from src.LoginWindow import LoginWindow

# python -m nuitka --windows-disable-console --follow-imports --windows-icon-from-ico=main_icon.ico main.py
if __name__ == "__main__":
    app = QApplication()
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec())
