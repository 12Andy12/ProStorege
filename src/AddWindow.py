from PySide6.QtWidgets import *
from src.forms.AddForm import Ui_AddWindow
import src.DBconector


class AddWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AddWindow, self).__init__(parent)
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self)
