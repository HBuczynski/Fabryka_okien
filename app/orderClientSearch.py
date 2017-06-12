"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o clientSearchDialog.py clientSearchDialog.ui
"""
from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import *

from ui.clientSearchDialog import Ui_clientSearchDialog
import Database
from PyQt5.QtCore import *


class OrderClientSearch(QDialog, Ui_clientSearchDialog, QObject):
    #Setting signals
    rowWasSet = pyqtSignal()

    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)

        # Database instance
        self.db = Database.Database()

        #Buttons connections
        self.clientSearchOkButton.clicked.connect(self.clickedOkButton)
        self.clientSearchCancelButton.clicked.connect(self.clickedCancelButton)
        self.clientSearchTable.clicked.connect(self.getRow)

        #Local variables
        self.rowIsSelected = False

    def setDataFromDatabase(self):
        result = self.db.get_clients("klient_id", "")
        self.table_widget_insert(result, self.clientSearchTable)

    def getRow(self):
        self.rowIsSelected = True;
        currentRow = self.clientSearchTable.currentRow()

        #Get selected data
        self.id = (self.clientSearchTable.item(currentRow,0)).text()
        self.adres = (self.clientSearchTable.item(currentRow,1)).text()
        self.imie = (self.clientSearchTable.item(currentRow, 2)).text()
        self.nazwisko = (self.clientSearchTable.item(currentRow, 3)).text()
        self.nip = (self.clientSearchTable.item(currentRow, 4)).text()
        self.pesel = (self.clientSearchTable.item(currentRow, 5)).text()
        self.nazwaFirmy = (self.clientSearchTable.item(currentRow, 6)).text()

    def clickedOkButton(self):
        if self.rowIsSelected :
            self.rowWasSet.emit()
            self.close()
            #return client paramters
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Wybierz klienta !!")
            msg.exec()

    def clickedCancelButton(self):
        self.close()

    #Appending data to tables:
    def table_widget_insert(self,query_result,table_widget):
        pc = len(query_result)
        if pc != 0:
            ic = len(query_result[0])
            i = 0
            j = 0
            table_widget.setRowCount(pc)
            while i < pc:
                while j < ic:
                    table_widget.setItem(i, j, QTableWidgetItem(str(query_result[i][j])))
                    j += 1
                j = 0
                i += 1
        else:
            table_widget.setRowCount(0)