"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o mainwindow.py mainwindow.ui
"""
#from PyQt5.QtWidgets import QMainWindow
#from generator.main import db
from reportlab.pdfbase._fontdata_widths_symbol import widths

TABLE_WIDGET_COLUMNS_WIDTH = [0.1, 0.3, 0.1, 0.1, 0.2, 0.2]

from PyQt5.QtWidgets import *
<<<<<<< HEAD
from generator import Database
from app.ui.mainwindow import Ui_MainWindow
=======

from ui.mainwindow import Ui_MainWindow
from orderDialog import OrderDialog
from clientDialog import ClientDialog

>>>>>>> 02c6eb9d6f0c7bc972038627269fdf327587c9c0
from PyQt5.QtCore import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.db = Database.Database()
        QMainWindow.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)

        #Initialize dialogs
        self.dialogOrder = OrderDialog()
        self.dialogClient = ClientDialog()

        # Actions for orders:
        self.orderAddButton.clicked.connect(self.clickedOrderAddButton)
        self.orderEditButton.clicked.connect(self.clickedOrderEditButton)
        self.orderSearchButton.clicked.connect(self.clickedOrderSearchButton)

        # Actions for clients

        self.clientSearchButton.clicked.connect(self.clickedClientSearchButton)
        self.clientAddButton.clicked.connect(self.clickedClientAddButton)
        self.clientEditButton.clicked.connect(self.clickedClientEditButton)

    #Definitions of PushButtons action functions:
    def clickedOrderAddButton(self):
        self.dialogOrder.show()
        print("add order")

    def clickedOrderEditButton(self):
        self.dialogOrder.loadParameters()
        self.dialogOrder.show()
        print("Edcyja")

    def clickedOrderSearchButton(self):
        print("Lupa")

<<<<<<< HEAD
    def clickedClientSearchButton(self):
        result = self.db.get_clients()
        self.table_widget_insert(result)
        searchAccordingTo = str(self.orderSearchComboBox.currentText())
        searchLine = self.orderSerachLineEdit.text()
        dateFrom = str(self.ordersFromDateEdit.date())
        print(dateFrom)
        
        if searchAccordingTo == 'ID klienta':
            print(searchLine)
        elif searchAccordingTo == 'Imię':
            print(searchLine)
        elif searchAccordingTo == 'Nazwisko':
            print(searchLine)
        elif searchAccordingTo == 'Nazwa Firmy':
            print(searchLine)
        elif searchAccordingTo == 'Pesel':
            print(searchLine)
        elif searchAccordingTo == 'NIP':
            print(searchLine)

    def clickedClientAddButton(self):
        self.dialogClient.show()
        print("add client")

    def clickedClientEditButton(self):
        self.dialogClient.loadParameters()
        self.dialogClient.show()
        print("edit client")

    def resizeTableWidget(self):
        tablewidth = self.verticalLayout_1.contentsRect().width()
        print(tablewidth)
        print(sum(TABLE_WIDGET_COLUMNS_WIDTH))
        for i, width in enumerate(TABLE_WIDGET_COLUMNS_WIDTH):
            self.tableWidget.setColumnWidth(i, width*tablewidth)


    #Appending data to tables:
    def table_widget_insert(self,query_result):
        pc = len(query_result)
        ic = len(query_result[0])
        i = 0
        j = 0
        self.clientTableWidget.setRowCount(pc)
        while i < pc:
            while j < ic:
                self.clientTableWidget.setItem(i, j, QTableWidgetItem(str(query_result[i][j])))
                j += 1
            j = 0
            i += 1

