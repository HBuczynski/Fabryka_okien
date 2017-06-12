"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o clientDialog.py clientDialog.ui
"""
from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import *

from ui.clientDialog import Ui_clientDialog
from PyQt5.QtCore import *
import Database


class ClientDialog(QDialog, Ui_clientDialog):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)
        self.db = Database.db
        # Setting up additional options (apart from generated, ex: PushButton  action):
        self.companyWidget.close()
        # Buttons actions
        self.clientCancelButton.clicked.connect(self.close)
        self.clientOkButton.clicked.connect(self.clicked_client_ok_button)
        self.clientTypeComboBox.currentIndexChanged.connect(self.set_client_type)

    def clear_parameters(self):
        self.cmpAddressLineEdit.clear()
        self.cmpNIPLineEdit.clear()
        self.cmpNameLineEdit.clear()
        self.prvAddressLineEdit.clear()
        self.prvPESELLineEdit.clear()
        self.prvSurnameLineEdit.clear()
        self.prvNameLineEdit.clear()

    def check_fields(self):
        if self.clientTypeComboBox.currentText() == "Osoba prywatna":
            if (self.prvNameLineEdit.text() == "" or self.prvAddressLineEdit.text() == "" or
            self.prvSurnameLineEdit.text() == "" or self.prvPESELLineEdit.text() == ""):
                return False
        else:
            print("False")
            if(self.cmpAddressLineEdit.text() == "" or self.cmpNameLineEdit.text() == "" or
            self.cmpNIPLineEdit.text() == ""):
                return False
        return True

    def clicked_client_ok_button(self):
        if self.check_fields():
            if self.clientTypeComboBox.currentText() == "Osoba prywatna":
                name = self.prvNameLineEdit.text()
                surname = self.prvSurnameLineEdit.text()
                pesel = self.prvPESELLineEdit.text()
                address = self.prvAddressLineEdit.text()
                self.db.add_client_person(name, surname, pesel, address)
                self.db.commit()
            else:
                cmp_name = self.cmpNameLineEdit.text()
                cmp_nip = self.cmpNIPLineEdit.text()
                cmp_address = self.cmpAddressLineEdit.text()
                self.db.add_client_company(cmp_name, cmp_nip, cmp_address)
                self.db.commit()
            self.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Uzupełnij wszystkie pola !!")
            msg.exec()

    def set_client_type(self):
        if self.clientTypeComboBox.currentText() == "Osoba prywatna" :
            self.companyWidget.close()
            self.prvPersonWidget.show()
        else:
            self.prvPersonWidget.close()
            self.companyWidget.show()
