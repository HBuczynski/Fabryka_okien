"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o mainwindow.py mainwindow.ui
"""
#from PyQt5.QtWidgets import QMainWindow
#from generator.main import db
from reportlab.pdfbase._fontdata_widths_symbol import widths

TABLE_WIDGET_COLUMNS_WIDTH = [0.1, 0.3, 0.1, 0.1, 0.2, 0.2]

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Database

from ui.mainwindow import Ui_MainWindow
from orderDialog import OrderDialog
from clientDialog import ClientDialog
from dialogEditClient import ClientEditDialog


from PyQt5.QtCore import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer.
        self.setupUi(self)

        # Connect to the database:
        self.db = Database.db

        # Initialize dialogs
        self.dialogOrder = OrderDialog()
        self.dialogClient = ClientDialog()
        self.dialogEditClient = ClientEditDialog()

        # Actions for orders:
        self.orderAddButton.clicked.connect(self.clickedOrderAddButton)
        self.orderEditButton.clicked.connect(self.clickedOrderEditButton)
        self.orderSearchButton.clicked.connect(self.clickedOrderSearchButton)

        self.displayOrders()

        # Actions for clients tab
        self.clientSearchButton.clicked.connect(self.clickedClientSearchButton)
        self.clientAddButton.clicked.connect(self.clickedClientAddButton)
        self.clientEditButton.clicked.connect(self.clickedClientEditButton)

        self.displayClients()

        # Actions for reports
        self.monthReportShowButton.clicked.connect(self.clickedMonthReportButton)
        self.clientReportShowButton.clicked.connect(self.clickedClientShowButton)

        # Actions for offer tab
        self.offerAddModelButton.clicked.connect(self.clickedOfferAddModelButton)
        self.offerAddSegmentButton.clicked.connect(self.clickedOfferAddSegmentButton)
        self.offerAddValueButton.clicked.connect(self.clickedAddValueButton)
        self.offerAddParamButton.clicked.connect(self.clickedAddParamButton)
        self.offerDeleteSegmentButton.clicked.connect(self.clickedOfferDeleteSegmentButton)
        self.offerDeleteParamButton.clicked.connect(self.clickedDeleteParamButton)

        self.offerModelTree.clicked.connect(self.clickedOfferModelTreeElement)
        self.offerParamTree.clicked.connect(self.clickedOfferParamTreeElement)

        self.displayModels()

    def clickedOfferModelTreeElement(self):
        data = self.offerModelTree.currentItem().data(1, 0)
        if len(data) == 1:
            # model clicked
            print("Model clicked: " + data[0][0])
        else:
            # segment clicked
            print("Segment clicked: " + data[0][0] + " -> " + data[1][0])
            # Update params tree
            self.displayParams(data[1][1])

    def clickedOfferParamTreeElement(self):
        data = self.offerParamTree.currentItem().data(1, 0)
        if len(data) == 1:
            # param clicked
            print("Param clicked: " + data[0][0])
        else:
            # value clicked
            print("Value clicked: " + data[0][0] + " -> " + data[1][0])

    def clickedOfferAddModelButton(self):
        print("TODO")

    def clickedOfferAddModelButton(self):
        print("TODO")

    def clickedOfferAddSegmentButton(self):
        print("TODO")

    def clickedAddValueButton(self):
        print("TODO")

    def clickedAddParamButton(self):
        print("TODO")

    def clickedOfferDeleteSegmentButton(self):
        print("TODO")

    def clickedDeleteParamButton(self):
        print("TODO")

    def displayModels(self):
        models = self.db.get_models()
        for m in models:
            model = QTreeWidgetItem()
            model.setText(0, m[0])
            model.setData(1, 0, [m,])
            segments = self.db.get_segments(m[1])
            for s in segments:
                segment = QTreeWidgetItem()
                segment.setText(0, s[0])
                segment.setData(1, 0, [m, s])
                model.addChild(segment)
            self.offerModelTree.addTopLevelItem(model)

    def displayClients(self):
        clients = self.db.get_clients('','')
        self.table_widget_insert(clients,self.clientTableView)

    def displayOrders(self):
        orders = self.db.get_invoices('','','','','wszystko')
        self.table_widget_insert(orders,self.orderTableView)

    def displayParams(self, segment_id):
        self.offerParamTree.clear()
        params = self.db.get_params(segment_id)
        for p in params:
            param = QTreeWidgetItem()
            param.setText(0, p[0])
            param.setToolTip(0, p[2])
            param.setData(1, 0, [p, ])
            values = self.db.get_vals(p[1])
            for v in values:
                value = QTreeWidgetItem()
                value.setText(0, v[0])
                value.setData(1, 0, [p, v])
                param.addChild(value)
            self.offerParamTree.addTopLevelItem(param)

    def clickedOrderAddButton(self):
        self.dialogOrder.setMode("new")
        self.dialogOrder.cleanObjectsInDialog()
        self.dialogOrder.show()

    def clickedOrderEditButton(self):
        currentRow = self.orderTableView.currentRow()
        if  currentRow != -1:
            self.dialogOrder.setMode("edit")
            self.dialogOrder.cleanObjectsInDialog()
            orderList = [self.orderTableView.item(currentRow, 0).text(),
                         self.orderTableView.item(currentRow, 1).text(),
                         self.orderTableView.item(currentRow, 2).text(),
                         self.orderTableView.item(currentRow, 3).text(),
                         self.orderTableView.item(currentRow, 4).text(),
                         self.orderTableView.item(currentRow, 5).text(),
                         self.orderTableView.item(currentRow, 6).text()]
            self.dialogOrder.loadParametersFromDatabase(orderList)
            self.dialogOrder.show()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Wybierz rekord!!")
            msg.exec()

    def clickedOrderSearchButton(self):
        searchAccordingTo = str(self.orderSearchComboBox.currentText())
        invoiceStatus = str(self.orderStateComboBox.currentText())
        searchLine = str(self.orderSerachLineEdit.text())
        dateFrom = self.ordersFromDateEdit.date().toPyDate()
        dateFrom = str(dateFrom.day) + "." + str(dateFrom.month) + "." + str(dateFrom.year)
        dateTo = self.ordersToDateEdit.date().toPyDate()
        dateTo = str(dateTo.day) + "." + str(dateTo.month) + "." + str(dateTo.year)

        if searchAccordingTo == "ID":
            result = self.db.get_invoices("faktura_id", searchLine, dateFrom, dateTo, invoiceStatus)
            self.table_widget_insert(result, self.orderTableView)
        elif searchAccordingTo == "ID Klienta":
            result = self.db.get_invoices("klient_id", searchLine, dateFrom, dateTo, invoiceStatus)
            self.table_widget_insert(result, self.orderTableView)

    def clickedClientSearchButton(self):
        searchAccordingTo = str(self.clientStatusComboBox.currentText())
        #listStatus = str(self.clientStateComboBox.currentText())
        searchLine = str(self.clientSearchLineEdit.text())

        #polaczenie z baza danych i wyswietlenie w tabeli
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

    def clickedClientEditButton(self):
        status = self.dialogEditClient.load_parameters(self.clientTableView)
        if status == 0:
            self.dialogEditClient.show()


    def clickedMonthReportButton(self):
        dateFrom = self.monthReportStartDateEdit.date().toPyDate()
        dateFromMonth = str(dateFrom.month)
        dateFromYear = str(dateFrom.year)
        dateTo = self.monthReportEndDateEdit.date().toPyDate()
        dateToMonth = str(dateTo.month)
        dateToYear = str(dateTo.year)

        result = self.db.get_month_report(dateFromMonth, dateFromYear, dateToMonth, dateToYear)
        self.table_widget_insert(result, self.monthReportTable)


    def clickedClientShowButton(self):
        dateFrom = self.clientReportStartDateEdit.date().toPyDate()
        dateFromYear = str(dateFrom.year)
        dateFromMonth = str(dateFrom.month)
        dateTo = self.clientReportEndDateEdit.date().toPyDate()
        dateToMonth = str(dateTo.month)
        dateToYear = str(dateTo.year)

        searchAccordingTo = str(self.clientReportSearchComboBox.currentText())
        searchLine = self.clientReportSearchLineEdit.text()

        if searchAccordingTo == "ID Klienta":
            result = self.db.get_client_report("klient_id", searchLine, dateFromYear, dateFromMonth, dateToYear, dateToMonth)
            self.table_widget_insert(result, self.clientTableView)
        elif searchAccordingTo == "Imię i nazwisko":
            result = self.db.get_client_report("Imię i nazwisko", searchLine, dateFromYear, dateFromMonth, dateToYear, dateToMonth)
            self.table_widget_insert(result, self.clientTableView)
        elif searchAccordingTo == "Nazwa firmy":
            result = self.db.get_client_report("nazwa", searchLine, dateFromYear, dateFromMonth, dateToYear, dateToMonth)
            self.table_widget_insert(result, self.clientTableView)
        elif searchAccordingTo == "PESEL":
            result = self.db.get_client_report("pesel", searchLine, dateFromYear, dateFromMonth, dateToYear, dateToMonth)
            self.table_widget_insert(result, self.clientTableView)
        elif searchAccordingTo == "NIP":
            result = self.db.get_client_report("nip", searchLine, dateFromYear, dateFromMonth, dateToYear, dateToMonth)
            self.table_widget_insert(result, self.clientTableView)

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
