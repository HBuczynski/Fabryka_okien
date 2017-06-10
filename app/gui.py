"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o mainwindow.py mainwindow.ui
"""
#from PyQt5.QtWidgets import QMainWindow


TABLE_WIDGET_COLUMNS_WIDTH = [0.1, 0.3, 0.1, 0.1, 0.2, 0.2]

from PyQt5.QtWidgets import *
from generator import Database
from app.ui.mainwindow import Ui_MainWindow
from PyQt5.QtCore import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)
        # Setting up additional options (apart from generated, ex: PushButton  action):

        # Actions for orders:
        self.orderAddButton.clicked.connect(self.clickedOrderAddButton)
        self.orderEditButton.clicked.connect(self.clickedOrderEditButton)
        self.orderSearchButton.clicked.connect(self.clickedOrderSearchButton)

        # Actions for clients


        self.clientSearchButton.clicked.connect(self.clickedSearchClientButton);
        self.clientAddButton.clicked.connect(self.clickedClientAddButton)
        self.clientEditButton.clicked.connect(self.clickedClientEditButton)
        self.clientSearchButton.clicked.connect(self.clickedClientSearchButton)

    #Definitions of PushButtons action functions:
    def clickedOrderAddButton(self):
        print("add order")

    def clickedOrderEditButton(self):
        print("Edcyja")

    def clickedOrderSearchButton(self):
        print("Lupa")

    def clickedSearchClientButton(self):
        query = ("SELECT * FROM Faktury")
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print(result)

    def clickedClientAddButton(self):
        print("add client")

    def clickedClientEditButton(self):
        print("edit client")

    def clickedClientSearchButton(self):
        print("Search button")

    def resizeTableWidget(self):
        tablewidth = self.verticalLayout_1.contentsRect().width()
        print(tablewidth)
        print(sum(TABLE_WIDGET_COLUMNS_WIDTH))
        for i, width in enumerate(TABLE_WIDGET_COLUMNS_WIDTH):
            self.tableWidget.setColumnWidth(i, width*tablewidth)
