"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o positionDialog.py positionDialog.ui
"""
from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import *

from ui.positionDialog import Ui_positionDialog
from orderClientSearch import OrderClientSearch
from PyQt5.QtCore import *

class PositionDialog(QDialog, Ui_positionDialog):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)
        self.mode = "new"
