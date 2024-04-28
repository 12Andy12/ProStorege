from PySide6.QtWidgets import *
from src.forms.ChangeForm import Ui_ChangeWindow


class ChangeWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ChangeWindow, self).__init__(parent)
        self.ui = Ui_ChangeWindow()
        self.ui.setupUi(self)