"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o invoiceDialog.py invoiceDialog.ui
"""
from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import *

from ui.invoiceDialog import Ui_invoiceDialog
from PyQt5.QtCore import *

class OrderDialog(QDialog, Ui_invoiceDialog):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)

        # Setting up additional options (apart from generated, ex: PushButton  action):
        self.selectClientButton.clicked.connect(self.clickedSelectClientButton)
        self.newPositionButton.clicked.connect(self.clickedNewPositionButton)
        self.editPositionButton.clicked.connect(self.clickedEditPositionButton)
        self.deletePositionButton.clicked.connect(self.clickedDeletePositionButton)

    def loadParameters(self):
        print("sciagamy parametry z bazy")

    def clickedSelectClientButton(self):
        print("sciagamy parametry z bazy")

    def clickedNewPositionButton(self):
        print("sciagamy parametry z bazy")

    def clickedEditPositionButton(self):
        print("sciagamy parametry z bazy")

    def clickedDeletePositionButton(self):
        print("sciagamy parametry z bazy")

    def setClientParameters(self):
        print("set labels")

    def getDataFromLabels(self):
        self.invoiceId = self.invoiceNumberLineEdit.text()
        self.status = self.invoiceStatusComboBox.currentText()
        self.addDate = self.invoiceAddDateLineEdit.text()
        self.endDate = self.invoiceEndDateLineEdit.text()
        self.totalCost = self.invoiceTotalCostLineEdit.text()