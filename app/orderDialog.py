"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o invoiceDialog.py invoiceDialog.ui
"""
from PyQt5 import QtCore

from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import *

from ui.invoiceDialog import Ui_invoiceDialog
from orderClientSearch import OrderClientSearch
from orderPositionDialog import PositionDialog

from PyQt5.QtCore import *

class OrderDialog(QDialog, Ui_invoiceDialog, QObject):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)
        self.mode = "new"

        #Setting up additional dialogs
        self.searchClientDialog = OrderClientSearch()
        self.positionDialog = PositionDialog()

        # Setting up additional options (apart from generated, ex: PushButton  action):
        self.selectClientButton.clicked.connect(self.clickedSelectClientButton)
        self.newPositionButton.clicked.connect(self.clickedNewPositionButton)
        self.editPositionButton.clicked.connect(self.clickedEditPositionButton)
        self.deletePositionButton.clicked.connect(self.clickedDeletePositionButton)
        self.invoiceCancelButton.clicked.connect(self.clickedInvoiceCancelButton)
        self.invoiceOkButton.clicked.connect(self.clickedInvoiceOkButton)

        #Setting connections between signals and slots
        self.searchClientDialog.rowWasSet.connect(self.setClientParameters)

    def setMode(self, mode):
        self.mode = mode


    def loadParametersFromDatabase(self):
        print("sciagamy parametry z bazy")

    def clickedSelectClientButton(self):
        self.searchClientDialog.setDataFromDatabase()
        self.searchClientDialog.show()

    def clickedNewPositionButton(self):
        self.positionDialog.mode = "new"
        self.positionDialog.show()

    def clickedEditPositionButton(self):
        self.positionDialog.mode = "edit"
        self.positionDialog.show()

    def clickedDeletePositionButton(self):
        print("sciagamy parametry z bazy")

    def clickedInvoiceOkButton(self):

        if self.getDataFromLabels() :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Uzupełnij wszystkie pola !!")
            msg.exec()

    def clickedInvoiceCancelButton(self):
        self.cleanObjectsInDialog()
        self.close()

    def cleanObjectsInDialog(self):
        self.invoiceNumberLineEdit.setText("")
        self.invoiceAddDateLineEdit.setText("")
        self.invoiceEndDateLineEdit.setText("")
        self.invoiceTotalCostLineEdit.setText("")

        self.clientNameLabel.setText("Imię i Nazwisko")
        self.clientAddressLabel.setText("Adres")
        self.clientCodeLabel.setText("Numer identyfikacyjny")

        self.invoiceTable.clearContents()

    @QtCore.pyqtSlot()
    def setClientParameters(self):
        if self.searchClientDialog.nip == "None":
            self.clientNameLabel.setText(self.searchClientDialog.imie + " " + self.searchClientDialog.nazwisko)
            self.clientAddressLabel.setText(self.searchClientDialog.adres)
            self.clientCodeLabel.setText(self.searchClientDialog.pesel)
        else:
            self.clientNameLabel.setText(self.searchClientDialog.nazwaFirmy)
            self.clientAddressLabel.setText(self.searchClientDialog.adres)
            self.clientCodeLabel.setText(self.searchClientDialog.nip)



    def getClientsParameters(self):
        print("get parameters")

    def getDataFromLabels(self):
        self.invoiceId = self.invoiceNumberLineEdit.text()
        self.status = self.invoiceStatusComboBox.currentText()
        self.addDate = self.invoiceAddDateLineEdit.text()
        self.endDate = self.invoiceEndDateLineEdit.text()
        self.totalCost = self.invoiceTotalCostLineEdit.text()

        fieldsAreEmpty = (self.invoiceId == "") or (self.status == "") or (self.addDate == "") or (self.endDate == "") or (self.totalCost == "")

        print(fieldsAreEmpty)
        return fieldsAreEmpty

