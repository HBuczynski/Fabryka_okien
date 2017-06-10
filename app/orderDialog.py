"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o invoiceDialog.py invoiceDialog.ui
"""
from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import *

from ui.invoiceDialog import Ui_invoiceDialog
from PyQt5.QtCore import *

class OrderDialog(QDialog, Ui_invoiceDialog):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)
        # Setting up additional options (apart from generated, ex: PushButton  action):

    def loadParameters(self):
        print("sciagamy parametry z bazy")