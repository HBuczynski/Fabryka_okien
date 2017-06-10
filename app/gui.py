"""
Pliki *.ui "kompiluje" się poleceniem:
$ pyuic5 -o mainwindow.py mainwindow.ui
"""
from PyQt5.QtWidgets import QMainWindow

TABLE_WIDGET_COLUMNS_WIDTH = [0.1, 0.3, 0.1, 0.1, 0.2, 0.2]

from PyQt5.QtWidgets import *

from ui.mainwindow import Ui_MainWindow
from PyQt5.QtCore import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)
        # Setting up additional options (apart from generated, ex: PushButton  action):

        # Actions for orders:
        #self.addInvoiceButton.clicked.connect(self.clickedInvoiceButton)
        #self.editInvoiceButton.clicked.connect(self.clickedEditInvoiceButton)
        #self.searchInvoiceButton.clicked.connect(self.clickedInvoiceButton)
        #self.selectInvoiceButton.clicked.connect(self.clickedSelectInvoiceButton)

        # Actions for clients
        #self.addClientButton.clicked.connect(self.clickedAddClientButton)
        #self.editClientButton.clicked.connect(self.clickedEditClientButton)
        #self.searchClientButton.clicked.connect(self.clickedSearchClientButton)

    #Definitions of PushButtons action functions:
    def clickedInvoiceButton(self):
        print("Ddddd")

        # TODO: To nie działa
        # self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.resizeTableWidget()
        # self.pushButton.clicked.connect(self.resizeTableWidget)

    def clickedEditInvoiceButton(self):
        print("Edcyja")

    def clickedSearchInvoiceButton(self):
        print("Lupa")

    def clickedSelectInvoiceButton(self):
        print("Pokaz Zamowienia")

    def clickedAddClientButton(self):
        print("add client")

    def clickedEditClientButton(self):
        print("edit client")

    def clickedSearchClientButton(self):
        print("Search button")

    def resizeTableWidget(self):
        tablewidth = self.verticalLayout_1.contentsRect().width()
        print(tablewidth)
        print(sum(TABLE_WIDGET_COLUMNS_WIDTH))
        for i, width in enumerate(TABLE_WIDGET_COLUMNS_WIDTH):
            self.tableWidget.setColumnWidth(i, width*tablewidth)
