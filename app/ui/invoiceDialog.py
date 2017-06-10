# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invoiceDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_invoiceDialog(object):
    def setupUi(self, invoiceDialog):
        invoiceDialog.setObjectName("invoiceDialog")
        invoiceDialog.resize(553, 672)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(invoiceDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.invoiceHeaderLayout = QtWidgets.QHBoxLayout()
        self.invoiceHeaderLayout.setObjectName("invoiceHeaderLayout")
        self.invoiceDataLayout = QtWidgets.QFormLayout()
        self.invoiceDataLayout.setObjectName("invoiceDataLayout")
        self.invoiceNumberLabel = QtWidgets.QLabel(invoiceDialog)
        self.invoiceNumberLabel.setObjectName("invoiceNumberLabel")
        self.invoiceDataLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.invoiceNumberLabel)
        self.invoiceNumberLineEdit = QtWidgets.QLineEdit(invoiceDialog)
        self.invoiceNumberLineEdit.setObjectName("invoiceNumberLineEdit")
        self.invoiceDataLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.invoiceNumberLineEdit)
        self.invoiceStatusLabel = QtWidgets.QLabel(invoiceDialog)
        self.invoiceStatusLabel.setObjectName("invoiceStatusLabel")
        self.invoiceDataLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.invoiceStatusLabel)
        self.invoiceStatusComboBox = QtWidgets.QComboBox(invoiceDialog)
        self.invoiceStatusComboBox.setObjectName("invoiceStatusComboBox")
        self.invoiceDataLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.invoiceStatusComboBox)
        self.invoiceAddDateLabel = QtWidgets.QLabel(invoiceDialog)
        self.invoiceAddDateLabel.setObjectName("invoiceAddDateLabel")
        self.invoiceDataLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.invoiceAddDateLabel)
        self.invoiceEndLabel = QtWidgets.QLabel(invoiceDialog)
        self.invoiceEndLabel.setObjectName("invoiceEndLabel")
        self.invoiceDataLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.invoiceEndLabel)
        self.invoiceAddDateLineEdit = QtWidgets.QLineEdit(invoiceDialog)
        self.invoiceAddDateLineEdit.setObjectName("invoiceAddDateLineEdit")
        self.invoiceDataLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.invoiceAddDateLineEdit)
        self.invoiceEndDateLineEdit = QtWidgets.QLineEdit(invoiceDialog)
        self.invoiceEndDateLineEdit.setObjectName("invoiceEndDateLineEdit")
        self.invoiceDataLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.invoiceEndDateLineEdit)
        self.invoiceTotalCostLabel = QtWidgets.QLabel(invoiceDialog)
        self.invoiceTotalCostLabel.setObjectName("invoiceTotalCostLabel")
        self.invoiceDataLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.invoiceTotalCostLabel)
        self.invoiceTotalCostLineEdit = QtWidgets.QLineEdit(invoiceDialog)
        self.invoiceTotalCostLineEdit.setObjectName("invoiceTotalCostLineEdit")
        self.invoiceDataLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.invoiceTotalCostLineEdit)
        self.invoiceHeaderLayout.addLayout(self.invoiceDataLayout)
        self.clientDataBox = QtWidgets.QGroupBox(invoiceDialog)
        self.clientDataBox.setObjectName("clientDataBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.clientDataBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clientSelectLayout = QtWidgets.QHBoxLayout()
        self.clientSelectLayout.setObjectName("clientSelectLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.clientSelectLayout.addItem(spacerItem)
        self.selectClientButton = QtWidgets.QPushButton(self.clientDataBox)
        self.selectClientButton.setObjectName("selectClientButton")
        self.clientSelectLayout.addWidget(self.selectClientButton)
        self.verticalLayout.addLayout(self.clientSelectLayout)
        self.clientNameLabel = QtWidgets.QLabel(self.clientDataBox)
        self.clientNameLabel.setObjectName("clientNameLabel")
        self.verticalLayout.addWidget(self.clientNameLabel)
        self.clientCodeLabel = QtWidgets.QLabel(self.clientDataBox)
        self.clientCodeLabel.setObjectName("clientCodeLabel")
        self.verticalLayout.addWidget(self.clientCodeLabel)
        self.clientAddressLabel = QtWidgets.QLabel(self.clientDataBox)
        self.clientAddressLabel.setObjectName("clientAddressLabel")
        self.verticalLayout.addWidget(self.clientAddressLabel)
        self.clientNameLabel.raise_()
        self.clientAddressLabel.raise_()
        self.clientCodeLabel.raise_()
        self.invoiceHeaderLayout.addWidget(self.clientDataBox)
        self.verticalLayout_2.addLayout(self.invoiceHeaderLayout)
        self.invoiceTableButtonsLayout = QtWidgets.QHBoxLayout()
        self.invoiceTableButtonsLayout.setObjectName("invoiceTableButtonsLayout")
        self.newPositionButton = QtWidgets.QPushButton(invoiceDialog)
        self.newPositionButton.setObjectName("newPositionButton")
        self.invoiceTableButtonsLayout.addWidget(self.newPositionButton)
        self.editPositionButton = QtWidgets.QPushButton(invoiceDialog)
        self.editPositionButton.setObjectName("editPositionButton")
        self.invoiceTableButtonsLayout.addWidget(self.editPositionButton)
        self.deletePositionButton = QtWidgets.QPushButton(invoiceDialog)
        self.deletePositionButton.setObjectName("deletePositionButton")
        self.invoiceTableButtonsLayout.addWidget(self.deletePositionButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.invoiceTableButtonsLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.invoiceTableButtonsLayout)
        self.invoiceTable = QtWidgets.QTableWidget(invoiceDialog)
        self.invoiceTable.setObjectName("invoiceTable")
        self.invoiceTable.setColumnCount(5)
        self.invoiceTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.invoiceTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.invoiceTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.invoiceTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.invoiceTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.invoiceTable.setHorizontalHeaderItem(4, item)
        self.verticalLayout_2.addWidget(self.invoiceTable)
        self.invoiceDialogButtonsLayout = QtWidgets.QHBoxLayout()
        self.invoiceDialogButtonsLayout.setObjectName("invoiceDialogButtonsLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.invoiceDialogButtonsLayout.addItem(spacerItem2)
        self.invoiceOkButton = QtWidgets.QPushButton(invoiceDialog)
        self.invoiceOkButton.setObjectName("invoiceOkButton")
        self.invoiceDialogButtonsLayout.addWidget(self.invoiceOkButton)
        self.invoiceCancelButton = QtWidgets.QPushButton(invoiceDialog)
        self.invoiceCancelButton.setObjectName("invoiceCancelButton")
        self.invoiceDialogButtonsLayout.addWidget(self.invoiceCancelButton)
        self.verticalLayout_2.addLayout(self.invoiceDialogButtonsLayout)

        self.retranslateUi(invoiceDialog)
        QtCore.QMetaObject.connectSlotsByName(invoiceDialog)

    def retranslateUi(self, invoiceDialog):
        _translate = QtCore.QCoreApplication.translate
        invoiceDialog.setWindowTitle(_translate("invoiceDialog", "Dialog"))
        self.invoiceNumberLabel.setText(_translate("invoiceDialog", "Numer faktury:"))
        self.invoiceStatusLabel.setText(_translate("invoiceDialog", "Status:"))
        self.invoiceAddDateLabel.setText(_translate("invoiceDialog", "Data dodania:"))
        self.invoiceEndLabel.setText(_translate("invoiceDialog", "Data zakończenia:"))
        self.invoiceTotalCostLabel.setText(_translate("invoiceDialog", "Całkowity koszt:"))
        self.clientDataBox.setTitle(_translate("invoiceDialog", "Dane klienta"))
        self.selectClientButton.setText(_translate("invoiceDialog", "Wybierz klienta"))
        self.clientNameLabel.setText(_translate("invoiceDialog", "Imię i Nazwisko"))
        self.clientCodeLabel.setText(_translate("invoiceDialog", "Numer identyfikujacy"))
        self.clientAddressLabel.setText(_translate("invoiceDialog", "Adres"))
        self.newPositionButton.setText(_translate("invoiceDialog", "Nowa pozycja"))
        self.editPositionButton.setText(_translate("invoiceDialog", "Edytuj"))
        self.deletePositionButton.setText(_translate("invoiceDialog", "Usuń"))
        item = self.invoiceTable.horizontalHeaderItem(0)
        item.setText(_translate("invoiceDialog", "ID"))
        item = self.invoiceTable.horizontalHeaderItem(1)
        item.setText(_translate("invoiceDialog", "Nazwa Segmentu"))
        item = self.invoiceTable.horizontalHeaderItem(2)
        item.setText(_translate("invoiceDialog", "Ilość"))
        item = self.invoiceTable.horizontalHeaderItem(3)
        item.setText(_translate("invoiceDialog", "Status"))
        item = self.invoiceTable.horizontalHeaderItem(4)
        item.setText(_translate("invoiceDialog", "Cena"))
        self.invoiceOkButton.setText(_translate("invoiceDialog", "OK"))
        self.invoiceCancelButton.setText(_translate("invoiceDialog", "Anuluj"))

