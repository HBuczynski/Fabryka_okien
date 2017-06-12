"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o clientEditDialog.py clientEditDialog.ui
"""
from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import *

from ui.clientEditDialog import Ui_clientEditDialog
from PyQt5.QtCore import *


class ClientEditDialog(QDialog, Ui_clientEditDialog):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)

        self.clientEditCancelButton.clicked.connect(self.close)
        self.clientEditOkButton.clicked.connect(self.clicked_client_ok_button)

    def clicked_client_ok_button(self):
        if self.check_fields():
            if self.clientTypeComboBox.currentText() == "Osoba prywatna":
                  name = self.prvNameLineEdit.text()
                  surname = self.prvSurnameLineEdit.text()
                  pesel = self.prvPESELLineEdit.text()
                  address = self.prvAddressLineEdit.text()
                  db.add_client_person(name, surname, pesel, address)
            else:
                  cmp_name = self.cmpNameLineEdit.text()
                  cmp_nip = self.cmpNIPLineEdit.text()
                  cmp_address = self.cmpAddressLineEdit.text()
                  db.add_client_company(cmp_name, cmp_nip, cmp_address)
              self.close()
        else:
              msg = QMessageBox()
              msg.setIcon(QMessageBox.Warning)
              msg.setText("Uzupełnij wszystkie pola !!")
              msg.exec()

    def check_fields(self):
          if self.clientTypeComboBox.currentText() == "Osoba prywatna":
              if (self.prvNameLineEdit.text() == "None" or self.prvAddressLineEdit.text() == "None" or
              self.prvSurnameLineEdit.text() == "None" or self.prvPESELLineEdit.text() == "None"):
                  return False
          else:
              if (self.cmpAddressLineEdit == "None" or self.cmpNameLineEdit == "None" or self.cmpNIPLineEdit == "None"):
                  return False
          return True

    def load_parameters(self, tableWidget):
        rowSelected =tableWidget.currentRow()
        if rowSelected != -1:
            self.cmpNameLineEdit.setText(tableWidget.item(rowSelected,6).text())
            self.cmpNIPLineEdit.setText(tableWidget.item(rowSelected, 4).text())
            self.cmpAddressLineEdit.setText(tableWidget.item(rowSelected, 1).text())
            self.prvNameLineEdit.setText(tableWidget.item(rowSelected, 2).text())
            self.prvSurnameLineEdit.setText(tableWidget.item(rowSelected, 3).text())
            self.prvPESELLineEdit.setText(tableWidget.item(rowSelected, 5).text())
            self.prvAddressLineEdit.setText(tableWidget.item(rowSelected, 1).text())
            return 0
        return -1
