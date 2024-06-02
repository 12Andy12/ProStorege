from PySide6.QtWidgets import *
from src.forms.DirectoryForm import Ui_DirectoryForm
import src.DBconector
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys

import src.APIconector


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
        elif self.mode == "replace_folder":
            self.replace_folder()
        elif self.mode == "replace_item":
            self.replace_item()
        else:
            print("неверный мод")

        self.hide()

    def replace_item(self):
        new_folder_name = self.le_folder_name.text()
        current_row = self.parent.items_table.currentRow()
        current_id = self.parent.items_table.item(current_row, 0).text()
        new_folder = None
        for folder in self.parent.folders:
            if folder["name"] == new_folder_name:
                new_folder = folder
                break

        if new_folder is None:
            return

        for item_id in self.parent.data:
            if item_id == current_id:
                self.parent.data[item_id]["group_id"] = new_folder["id"]
                self.parent.data[item_id]["paymentMethodType"] = 4
                self.parent.data[item_id]["subject"] = 1
                src.APIconector.update_good(self.parent.data[item_id])
                self.parent.on_dir_changed()
                break

    def replace_folder(self):
        new_parent_name = self.le_folder_name.text()
        name = self.parent.folders_tree.currentItem().text(0)
        new_parent = None
        for folder in self.parent.folders:
            if folder["name"] == new_parent_name:
                new_parent = folder
                break

        if new_parent is None:
            return

        for folder in self.parent.folders:
            if folder["name"] == name:
                folder["parent"] = new_parent["id"]
                src.APIconector.update_dir(folder)
                break

        self.parent.load_folders()
        self.parent.draw_folders()
        self.parent.old_selection_name = name



    def rename_folder(self):
        new_name = self.le_folder_name.text()
        old_name = self.parent.folders_tree.currentItem().text(0)
        if not self.is_correct_name(new_name):
            return

        for folder in self.parent.folders:
            if folder["name"] == old_name:
                folder["name"] = new_name
                src.APIconector.update_dir(folder)
                break

        self.parent.folders_tree.currentItem().setText(0, new_name)


    def add_folder(self):
        new_id = src.APIconector.generate_id()
        new_folder_name = self.le_folder_name.text()
        parent_name = self.parent.folders_tree.currentItem().text(0)
        if not self.is_correct_name(new_folder_name):
            return
        parent_id = None
        if self.parent.folders_tree.currentItem().text(0) == "Все категории":
            parent_id = None
        else:
            # parent_id = self.parent.data_base_connector.request(
            #     f"SELECT id FROM folders WHERE name = '{self.parent.folders_tree.currentItem().text(0)}'")
            for folder in self.parent.folders:
                if folder["name"] == parent_name:
                    # print(f"Add {folder['name']}")
                    parent_id = folder["id"]

        new_folder = src.APIconector.add_folder(new_id, new_folder_name, parent_id)

        # self.parent.data_base_connector.request(
        #     f"INSERT INTO folders(id, name, parent_name) VALUES('{new_id}', '{new_folder}', '{parent_id}')")

        child = QTreeWidgetItem(self.parent.folders_tree.currentItem())
        child.setText(0, new_folder_name)
        child.setIcon(0, QIcon("images/iconFolder.png"))
        self.parent.count_parent[new_folder_name] = self.parent.count_parent[parent_name] + 1
        self.parent.load_folders()

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



