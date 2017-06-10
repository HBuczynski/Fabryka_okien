# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientSearchDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_clientSearchDialog(object):
    def setupUi(self, clientSearchDialog):
        clientSearchDialog.setObjectName("clientSearchDialog")
        clientSearchDialog.resize(680, 273)
        self.gridLayout = QtWidgets.QGridLayout(clientSearchDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.clientSearchTable = QtWidgets.QTableWidget(clientSearchDialog)
        self.clientSearchTable.setObjectName("clientSearchTable")
        self.clientSearchTable.setColumnCount(6)
        self.clientSearchTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.clientSearchTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientSearchTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientSearchTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientSearchTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientSearchTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientSearchTable.setHorizontalHeaderItem(5, item)
        self.clientSearchTable.horizontalHeader().setCascadingSectionResizes(True)
        self.clientSearchTable.horizontalHeader().setSortIndicatorShown(True)
        self.clientSearchTable.horizontalHeader().setStretchLastSection(True)
        self.clientSearchTable.verticalHeader().setCascadingSectionResizes(True)
        self.clientSearchTable.verticalHeader().setSortIndicatorShown(True)
        self.clientSearchTable.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.clientSearchTable, 0, 0, 1, 1)
        self.clientSearchDialogButtonsLayout = QtWidgets.QHBoxLayout()
        self.clientSearchDialogButtonsLayout.setObjectName("clientSearchDialogButtonsLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.clientSearchDialogButtonsLayout.addItem(spacerItem)
        self.clientSearchOkButton = QtWidgets.QPushButton(clientSearchDialog)
        self.clientSearchOkButton.setObjectName("clientSearchOkButton")
        self.clientSearchDialogButtonsLayout.addWidget(self.clientSearchOkButton)
        self.clientSearchCancelButton = QtWidgets.QPushButton(clientSearchDialog)
        self.clientSearchCancelButton.setObjectName("clientSearchCancelButton")
        self.clientSearchDialogButtonsLayout.addWidget(self.clientSearchCancelButton)
        self.gridLayout.addLayout(self.clientSearchDialogButtonsLayout, 1, 0, 1, 1)

        self.retranslateUi(clientSearchDialog)
        QtCore.QMetaObject.connectSlotsByName(clientSearchDialog)

    def retranslateUi(self, clientSearchDialog):
        _translate = QtCore.QCoreApplication.translate
        clientSearchDialog.setWindowTitle(_translate("clientSearchDialog", "Dialog"))
        item = self.clientSearchTable.horizontalHeaderItem(0)
        item.setText(_translate("clientSearchDialog", "Imię"))
        item = self.clientSearchTable.horizontalHeaderItem(1)
        item.setText(_translate("clientSearchDialog", "Nazwisko"))
        item = self.clientSearchTable.horizontalHeaderItem(2)
        item.setText(_translate("clientSearchDialog", "Nazwa firmy"))
        item = self.clientSearchTable.horizontalHeaderItem(3)
        item.setText(_translate("clientSearchDialog", "PESEL"))
        item = self.clientSearchTable.horizontalHeaderItem(4)
        item.setText(_translate("clientSearchDialog", "NIP"))
        item = self.clientSearchTable.horizontalHeaderItem(5)
        item.setText(_translate("clientSearchDialog", "Adres"))
        self.clientSearchOkButton.setText(_translate("clientSearchDialog", "Ok"))
        self.clientSearchCancelButton.setText(_translate("clientSearchDialog", "Anuluj"))

