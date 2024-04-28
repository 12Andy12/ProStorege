from PySide6.QtWidgets import *
from src.forms.InfoForm import Ui_InfoWindow


class InfoWindow(QMainWindow):
    def __init__(self, parent=None):
        super(InfoWindow, self).__init__(parent)
        self.ui = Ui_InfoWindow()
        self.ui.setupUi(self)