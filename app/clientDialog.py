"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o clientDialog.py clientDialog.ui
"""
from PyQt5.QtWidgets import QDialog

from PyQt5.QtWidgets import *

from ui.clientDialog import Ui_clientDialog
from PyQt5.QtCore import *

class ClientDialog(QDialog, Ui_clientDialog):
    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)
        # Setting up additional options (apart from generated, ex: PushButton  action):

    def loadParameters(self):
        print("sciagamy parametry z bazy")