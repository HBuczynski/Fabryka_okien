"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o clientSearchDialog.py clientSearchDialog.ui
"""
from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import *

from ui.clientSearchDialog import Ui_clientSearchDialog
from PyQt5.QtCore import *


class OrderClientSearch(QDialog, Ui_clientSearchDialog):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)

        self.clientSearchOkButton.clicked.connect(self.clickedOkButton)
        self.clientSearchCancelButton.clicked.connect(self.clickedCancelButton)
        self.clientSearchTable.clicked.connect(self.getRow)

        self.rowIsSelected = False;

    def setDataFromDatabase(self):
        print("Set data in tabel")

    def getRow(self):
        self.rowIsSelected = True;
        #TO DO: set param to variables

    def clickedOkButton(self):
        if self.rowIsSelected :
            print("getData")
            #return client paramters
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Wybierz klienta !!")
            msg.exec()

    def clickedCancelButton(self):
        self.close()