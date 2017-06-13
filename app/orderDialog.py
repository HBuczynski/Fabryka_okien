"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o invoiceDialog.py invoiceDialog.ui
"""
from PyQt5 import QtCore
import Database
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

        # Set database
        self.db = Database.db

        # Setting up additional dialogs
        self.searchClientDialog = OrderClientSearch()
        self.positionDialog = PositionDialog()

        # Setting up additional options (apart from generated, ex: PushButton  action):
        self.selectClientButton.clicked.connect(self.clickedSelectClientButton)
        self.newPositionButton.clicked.connect(self.clickedNewPositionButton)
        self.editPositionButton.clicked.connect(self.clickedEditPositionButton)
        self.deletePositionButton.clicked.connect(self.clickedDeletePositionButton)
        self.invoiceCancelButton.clicked.connect(self.clickedInvoiceCancelButton)
        self.invoiceOkButton.clicked.connect(self.clickedInvoiceOkButton)

        # Setting connections between signals and slots
        self.searchClientDialog.rowWasSet.connect(self.setClientParameters)

        self.invoiceTable.verticalHeader().setVisible(False)

    def setMode(self, mode):
        self.mode = mode
        if mode == "new":
            self.invoiceStatusComboBox.setEnabled(False)
            self.selectClientButton.setDisabled(False)

    def loadParametersFromDatabase(self, orderList):
        self.selectClientButton.setDisabled(True)
        self.invoiceStatusComboBox.setEnabled(True)

        self.invoiceNumberLineEdit.setText(orderList[0])
        self.invoiceAddDateLineEdit.setText(orderList[3])
        self.invoiceEndDateLineEdit.setText(orderList[4])
        index = self.invoiceStatusComboBox.findText(orderList[5])
        self.invoiceStatusComboBox.setCurrentIndex(index)
        self.invoiceTotalCostLineEdit.setText(orderList[6])
        self.table_insert_positions(orderList[0])

        client = self.db.get_clients("klient_id", orderList[1])
        if str(client[0][4]) == "None":
            name = str(client[0][2] + " " + client[0][3])
            self.clientNameLabel.setText(name)
            self.clientAddressLabel.setText(client[0][1])
            self.clientCodeLabel.setText(client[0][5])
        else:
            self.clientNameLabel.setText(client[0][6])
            self.clientAddressLabel.setText(client[0][1])
            self.clientCodeLabel.setText(client[0][4])

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
        self.invoiceTable.clearContents()

        self.clientNameLabel.setText("Imię i Nazwisko")
        self.clientAddressLabel.setText("Adres")
        self.clientCodeLabel.setText("Numer identyfikacyjny")

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


    def getDataFromLabels(self):
        self.invoiceId = self.invoiceNumberLineEdit.text()
        self.status = self.invoiceStatusComboBox.currentText()
        self.addDate = self.invoiceAddDateLineEdit.text()
        self.endDate = self.invoiceEndDateLineEdit.text()
        self.totalCost = self.invoiceTotalCostLineEdit.text()

        fieldsAreEmpty = (self.invoiceId == "") or (self.status == "") or (self.addDate == "") or (self.endDate == "") or (self.totalCost == "")

        print(fieldsAreEmpty)
        return fieldsAreEmpty

    def table_insert_positions(self, invoice_id):
        positions = self.db.get_positions_from_invoice(invoice_id)
        pc = len(positions)
        i=0
        self.invoiceTable.setRowCount(pc)
        while i < pc:
            segment_name = self.db.get_segment_name_and_modelid(positions[i][1])
            model_name = self.db.get_model_name(segment_name[0][1])
            self.invoiceTable.setItem(i, 0, QTableWidgetItem(str(positions[i][0])))
            self.invoiceTable.setItem(i, 1, QTableWidgetItem(str(segment_name[0][0])))
            self.invoiceTable.setItem(i, 2, QTableWidgetItem(str(model_name)))
            self.invoiceTable.setItem(i, 3, QTableWidgetItem(str(positions[i][5])))
            self.invoiceTable.setItem(i, 4, QTableWidgetItem(str(positions[i][6])))
            self.invoiceTable.setItem(i, 5, QTableWidgetItem(str(positions[i][2])))
            i=i+1
