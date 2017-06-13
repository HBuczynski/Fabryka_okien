"""
Pliki *.ui "kompiluje" się poleceniem:
    $ pyuic5 -o positionDialog.py positionDialog.ui
"""
from _operator import le

from PyQt5.QtWidgets import QDialog
import Database

from PyQt5.QtWidgets import *

from ui.positionDialog import Ui_positionDialog
from orderClientSearch import OrderClientSearch
from PyQt5.QtCore import *

class PositionDialog(QDialog, Ui_positionDialog, QObject):

    setData = pyqtSignal()

    def __init__(self):
        QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.setupUi(self)

        # Set database
        self.db = Database.db

        #Setting initial mode
        self.mode = "new"

        #Set connections
        self.modelSelectComboBox.currentIndexChanged.connect(self.addSegments)
        self.positionDialogOkButton.clicked.connect(self.clickedOkButton)
        self.positionDialogCancelButton.clicked.connect(self.clickedCancelButton)

    def setMode(self, mode):
        self.mode = mode

        if self.mode == "new":
            self.segmentStatusComboBox.setDisabled(True)
        else:
            self.segmentStatusComboBox.setDisabled(False)

    def setDataFromDatabase(self):
        #Adding models to combo box
        self.addModels()
        self.addWindows()


    def addModels(self):
        results = self.db.get_models()

        length = len(results)
        i=0;

        self.modelSelectComboBox.clear()
        while i < length:
            self.modelSelectComboBox.insertItem(i,results[i][0])
            i=i+1

    def addWindows(self):
        results = self.db.get_rodzaj_szyby()

        length = len(results)
        i=0

        self.segmentPaneComboBox.clear()
        while i < length:
            self.segmentPaneComboBox.insertItem(i, results[i][0])
            i=i+1

    def addSegments(self):

        if self.modelSelectComboBox.currentText() != "":
            model_name = str(self.modelSelectComboBox.currentText())
            model_id = self.db.get_model_id(model_name)
            results = self.db.get_segments(model_id)

            length = len(results)
            i = 0;

            self.segmentSelectComboBox.clear()
            while i < length:
                self.segmentSelectComboBox.insertItem(i, results[i][0])
                i = i + 1

    def getData(self):
        self.model_name = self.modelSelectComboBox.currentText()
        self.segment_name = self.segmentSelectComboBox.currentText()
        self.ilosc = self.segmentQuantitySpinBox.value()
        self.wymiar_x = self.segmentWidthSpinBox.value()
        self.wymiar_y = self.segmentHeightSpinBox.value()
        self.status = self.segmentStatusComboBox.currentText()
        self.szyba = self.segmentPaneComboBox.currentText()

    def clickedOkButton(self):
            self.setData.emit()
            self.close()

    def clickedCancelButton(self):
        self.modelSelectComboBox.clear()
        self.segmentSelectComboBox.clear()
        self.segmentQuantitySpinBox.setValue(0)
        self.segmentHeightSpinBox.setValue(0)
        self.segmentWidthSpinBox.setValue(0)
        self.segmentPaneComboBox.clear()

        self.close()