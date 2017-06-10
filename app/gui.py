"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o mainwindow.py mainwindow.ui
"""
#from PyQt5.QtWidgets import QMainWindow
#from generator.main import db
from reportlab.pdfbase._fontdata_widths_symbol import widths

TABLE_WIDGET_COLUMNS_WIDTH = [0.1, 0.3, 0.1, 0.1, 0.2, 0.2]

from PyQt5.QtWidgets import *
import Database


from ui.mainwindow import Ui_MainWindow
from orderDialog import OrderDialog
from clientDialog import ClientDialog
from dialogEditClient import ClientEditDialog


from PyQt5.QtCore import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.db = Database.Database()
        QMainWindow.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)

        # Initialize dialogs
        self.dialogOrder = OrderDialog()
        self.dialogClient = ClientDialog()
        self.dialogEditClient = ClientEditDialog()

        # Actions for orders:
        self.orderAddButton.clicked.connect(self.clickedOrderAddButton)
        self.orderEditButton.clicked.connect(self.clickedOrderEditButton)
        self.orderSearchButton.clicked.connect(self.clickedOrderSearchButton)

        # Actions for clients tab
        self.clientSearchButton.clicked.connect(self.clickedClientSearchButton)
        self.clientAddButton.clicked.connect(self.clickedClientAddButton)
        self.clientEditButton.clicked.connect(self.clickedClientEditButton)

        # Actions for reports
        self.monthReportShowButton.clicked.connect(self.clickedMonthReportButton)
        self.clientReportShowButton.clicked.connect(self.clickedClientShowButton)

    def clickedOrderAddButton(self):
        self.dialogOrder.mode = "new"
        self.dialogOrder.cleanObjectsInDialog()
        self.dialogOrder.show()
        #DONE: print("add order")

    def clickedOrderEditButton(self):
        self.dialogOrder.mode = "edit"
        self.dialogOrder.cleanObjectsInDialog()
        self.dialogOrder.loadParametersFromDatabase()
        self.dialogOrder.show()
        #DONE: print("Edycja")

    def clickedOrderSearchButton(self):
        searchAccordingTo = str(self.orderSearchComboBox.currentText())
        invoiceStatus = str(self.orderStateComboBox.currentText())
        searchLine = str(self.orderSerachLineEdit.text())
        dateFrom = self.ordersFromDateEdit.date().toPyDate()
        dateFrom = str(dateFrom.day) + "." + str(dateFrom.month) + "." + str(dateFrom.year)
        dateTo = self.ordersToDateEdit.date().toPyDate()
        dateTo = str(dateTo.day) + "." + str(dateTo.month) + "." + str(dateTo.year)

        
        result = self.db.get_invoices()
        self.table_widget_insert(result, self.orderTableView)
        print("Lupa")

    def clickedClientSearchButton(self):
        searchAccordingTo = str(self.clientStatusComboBox.currentText())
        #listStatus = str(self.clientStateComboBox.currentText())
        searchLine = str(self.clientSearchLineEdit.text())
        # dateFrom = self.ordersFromDateEdit.date().toPyDate()
        # dateFrom = str(dateFrom.day) + "." + str(dateFrom.month) + "." + str(dateFrom.year)
        # dateTo = self.ordersToDateEdit.date().toPyDate()
        # dateTo = str(dateTo.day) + "." + str(dateTo.month) + "." + str(dateTo.year)

        #TO DO: polaczenie z baza danych i wyswietlenie w tabeli
        if searchAccordingTo == "ID Klienta":
            result = self.db.get_clients("klient_id", searchLine)
            self.table_widget_insert(result, self.clientTableView)
        elif searchAccordingTo == "Imię i nazwisko":
            result = self.db.get_clients("Imię i nazwisko", searchLine)
            self.table_widget_insert(result, self.clientTableView)
        elif searchAccordingTo == "Nazwa firmy":
            result = self.db.get_clients("nazwa", searchLine)
            self.table_widget_insert(result, self.clientTableView)
        elif searchAccordingTo == "PESEL":
            result = self.db.get_clients("pesel", searchLine)
            self.table_widget_insert(result, self.clientTableView)
        elif searchAccordingTo == "NIP":
            result = self.db.get_clients("nip", searchLine)
            self.table_widget_insert(result, self.clientTableView)



    def clickedClientAddButton(self):
        self.dialogClient.clear_parameters()
        self.dialogClient.show()
        print("add client")

    def clickedClientEditButton(self):
        self.dialogEditClient.load_parameters()
        self.dialogEditClient.show()
        print("edit client")

    def clickedMonthReportButton(self):
        dateFrom = self.monthReportStartDateEdit.date().toPyDate()
        dateFrom = str(dateFrom.day) + "." + str(dateFrom.month) + "." + str(dateFrom.year)
        dateTo = self.monthReportEndDateEdit.date().toPyDate()
        dateTo = str(dateTo.day) + "." + str(dateTo.month) + "." + str(dateTo.year)

        #TO DO: add data to table

    def clickedClientShowButton(self):
        dateFrom = self.clientReportStartDateEdit.date().toPyDate()
        dateFrom = str(dateFrom.day) + "." + str(dateFrom.month) + "." + str(dateFrom.year)
        dateTo = self.clientReportEndDateEdit.date().toPyDate()
        dateTo = str(dateTo.day) + "." + str(dateTo.month) + "." + str(dateTo.year)

        searchAccordingTo = str(self.clientReportSearchComboBox.currentText())
        searchLine = self.clientReportSearchLineEdit.text()

        #TO DO: get data from database

    def resizeTableWidget(self):
        tablewidth = self.verticalLayout_1.contentsRect().width()
        print(tablewidth)
        print(sum(TABLE_WIDGET_COLUMNS_WIDTH))
        for i, width in enumerate(TABLE_WIDGET_COLUMNS_WIDTH):
            self.tableWidget.setColumnWidth(i, width*tablewidth)


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
