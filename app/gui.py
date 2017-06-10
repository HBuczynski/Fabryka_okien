"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o mainwindow.py mainwindow.ui
"""
from PyQt5.QtWidgets import QMainWindow

TABLE_WIDGET_COLUMNS_WIDTH = [0.1, 0.3, 0.1, 0.1, 0.2, 0.2]

from PyQt5.QtWidgets import *

from ui.mainwindow import Ui_MainWindow
from orderDialog import OrderDialog
from clientDialog import ClientDialog

from PyQt5.QtCore import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
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
        self.clientAddButton.clicked.connect(self.clickedClientAddButton)
        self.clientEditButton.clicked.connect(self.clickedClientEditButton)
        self.clientSearchButton.clicked.connect(self.clickedClientSearchButton)

        

    #Definitions of PushButtons action functions:
    def clickedOrderAddButton(self):
        self.dialogOrder.mode = "new"
        self.dialogOrder.cleanObjectsInDialog()
        self.dialogOrder.show()
        print("add order")

    def clickedOrderEditButton(self):
        self.dialogOrder.mode = "edit"
        self.dialogOrder.cleanObjectsInDialog()
        self.dialogOrder.loadParameters()
        self.dialogOrder.show()
        print("Edcyja")

    def clickedOrderSearchButton(self):
        print("Lupa")

        searchAccordingTo = str(self.orderSearchComboBox.currentText())
        listStatus = str(self.orderStateComboBox.currentText())
        searchLine = self.orderSerachLineEdit.text()

        dateFrom = self.ordersFromDateEdit.date().toPyDate()
        dateFrom = str(dateFrom.day) + "." + str(dateFrom.month) + "." + str(dateFrom.year)
        dateTo = self.ordersToDateEdit.date().toPyDate()
        dateTo = str(dateTo.day) + "." + str(dateTo.month) + "." + str(dateTo.year)

        #TO DO: polaczenie z baza danych
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

    def clickedClientSearchButton(self):
        print("Search button")

    def resizeTableWidget(self):
        tablewidth = self.verticalLayout_1.contentsRect().width()
        print(tablewidth)
        print(sum(TABLE_WIDGET_COLUMNS_WIDTH))
        for i, width in enumerate(TABLE_WIDGET_COLUMNS_WIDTH):
            self.tableWidget.setColumnWidth(i, width*tablewidth)