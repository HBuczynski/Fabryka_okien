"""
Pliki *.ui "kompiluje" się poleceniem:
$ pyuic5 -o mainwindow.py mainwindow.ui
"""

TABLE_WIDGET_COLUMNS_WIDTH = [0.1, 0.3, 0.1, 0.1, 0.2, 0.2]

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.setupUi(self)

        # TODO: To nie działa
        # self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.resizeTableWidget()
        # self.pushButton.clicked.connect(self.resizeTableWidget)

    def resizeTableWidget(self):
        tablewidth = self.verticalLayout_1.contentsRect().width()
        print(tablewidth)
        print(sum(TABLE_WIDGET_COLUMNS_WIDTH))
        for i, width in enumerate(TABLE_WIDGET_COLUMNS_WIDTH):
            self.tableWidget.setColumnWidth(i, width*tablewidth)