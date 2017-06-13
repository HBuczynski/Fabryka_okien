"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o clientEditDialog.py clientEditDialog.ui
"""

from PyQt5.QtWidgets import *

from ui.clientEditDialog import Ui_clientEditDialog
from PyQt5.QtCore import *
import Database

class ClientEditDialog(QDialog, Ui_clientEditDialog):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer.
        self.setupUi(self)
        self.db = Database.db
        self.id = None
        self.selector = None
        self.clientEditCancelButton.clicked.connect(self.close)
        self.clientEditOkButton.clicked.connect(self.clicked_client_ok_button)

    def clicked_client_ok_button(self):
        if self.selector == "None":
                  name = self.prvNameLineEdit.text()
                  surname = self.prvSurnameLineEdit.text()
                  pesel = self.prvPESELLineEdit.text()
                  address = self.prvAddressLineEdit.text()
                  if name == '' or surname == '' or pesel == '' or address == '':
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Uzupełnij wszystkie pola !!")
                        msg.exec()
                        return
                  self.db.update_client_person(name, surname, pesel, address, self.id)
                  self.db.commit()
        else:
                  cmp_name = self.cmpNameLineEdit.text()
                  cmp_nip = self.cmpNIPLineEdit.text()
                  cmp_address = self.cmpAddressLineEdit.text()
                  if cmp_name == '' or cmp_nip == '' or cmp_address == '':
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Uzupełnij wszystkie pola !!")
                        msg.exec()
                        return
                  self.db.update_client_company(cmp_name, cmp_nip, cmp_address, self.id)
                  self.db.commit()
        self.close()

    # def check_fields(self):
    #       rowSelected = tableWidget.currentRow()
    #       self.selector = tableWidget.item(rowSelected,6).text()
    #       if self.selector != None:
    #               return False
    #       return True

    def load_parameters(self, tableWidget):
        rowSelected =tableWidget.currentRow()
        self.companyWidget.show()
        self.prvPersonWidget.show()
        if rowSelected != -1:
            self.id = tableWidget.item(rowSelected,0).text()
            self.selector = tableWidget.item(rowSelected,6).text()
            self.cmpNameLineEdit.setText(tableWidget.item(rowSelected,6).text())
            self.cmpNIPLineEdit.setText(tableWidget.item(rowSelected, 4).text())
            self.cmpAddressLineEdit.setText(tableWidget.item(rowSelected, 1).text())
            self.prvNameLineEdit.setText(tableWidget.item(rowSelected, 2).text())
            self.prvSurnameLineEdit.setText(tableWidget.item(rowSelected, 3).text())
            self.prvPESELLineEdit.setText(tableWidget.item(rowSelected, 5).text())
            self.prvAddressLineEdit.setText(tableWidget.item(rowSelected, 1).text())
            if self.selector == "None":
                self.companyWidget.hide()
            else:
                self.prvPersonWidget.hide()
            return 0
        return -1
