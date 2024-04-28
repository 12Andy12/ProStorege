from PySide6.QtWidgets import *
from src.forms.DirectoryForm import Ui_DirectoryForm
import src.DBconector
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class FolderWindow(QtWidgets.QWidget, Ui_DirectoryForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.ui = Ui_AddDirectoryForm()
        self.setupUi(self)
        self.move(300, 300)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.mode = "add"
        self.parent = parent
        self.current_folder: QTreeWidgetItem

        # self.le_folder_name.editingFinished.connect(lambda: self.hide())
        self.old_pos = None
        self.hide()

        self.le_folder_name.returnPressed.connect(lambda: self.selector())
        self.btn_ok.clicked.connect(lambda: self.selector())

        self.btn_cancel.clicked.connect(lambda: self.hide())

    def selector(self):
        if self.mode == "add":
            self.add_folder()
        elif self.mode == "rename":
            self.rename_folder()
        else:
            print("неверный мод")

    def rename_folder(self):
        new_name = self.le_folder_name.text()
        if not self.is_correct_name(new_name):
            return
        self.parent.data_base_connector.request(
            f"UPDATE folders SET name = '{new_name}' WHERE name = '{self.parent.ui.folders_tree.currentItem().text(0)}'")

        self.parent.ui.folders_tree.currentItem().setText(0, new_name)
        self.hide()

    def add_folder(self):
        new_folder = self.le_folder_name.text()
        if not self.is_correct_name(new_folder):
            return
        self.parent.data_base_connector.request(
            f"INSERT INTO folders(name, parent_name) VALUES('{new_folder}', '{self.parent.ui.folders_tree.currentItem().text(0)}')")
        self.hide()
        child = QTreeWidgetItem(self.parent.ui.folders_tree.currentItem())
        child.setText(0, new_folder)
        child.setIcon(0, QIcon("images/iconFolder.png"))

    def is_correct_name(self, name):
        if name == "":
            self.close()
            return False
        check = self.parent.data_base_connector.request(
            f"SELECT * FROM folders WHERE name = '{name}';")
        print(check)
        if len(check) != 0:
            print("mb")
            msg = QMessageBox()
            msg.setWindowTitle("Внимание")
            msg.setText("Категория с таким именем уже существует!")
            msg.setIcon(QMessageBox.Warning)
            returnValue = msg.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')
            return False
        return True

    # вызывается при нажатии кнопки мыши
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

    def focusInEvent(self, e):
        self.le_folder_name.setFocus()



