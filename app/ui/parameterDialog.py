# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameterDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_parameterDialog(object):
    def setupUi(self, parameterDialog):
        parameterDialog.setObjectName("parameterDialog")
        parameterDialog.resize(358, 320)
        self.gridLayout = QtWidgets.QGridLayout(parameterDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.parameterNameLayout = QtWidgets.QHBoxLayout()
        self.parameterNameLayout.setObjectName("parameterNameLayout")
        self.parameterNameLabel = QtWidgets.QLabel(parameterDialog)
        self.parameterNameLabel.setObjectName("parameterNameLabel")
        self.parameterNameLayout.addWidget(self.parameterNameLabel)
        self.parameterNameLineEdit = QtWidgets.QLineEdit(parameterDialog)
        self.parameterNameLineEdit.setObjectName("parameterNameLineEdit")
        self.parameterNameLayout.addWidget(self.parameterNameLineEdit)
        self.gridLayout.addLayout(self.parameterNameLayout, 0, 0, 1, 1)
        self.parameterValueListLayout = QtWidgets.QHBoxLayout()
        self.parameterValueListLayout.setObjectName("parameterValueListLayout")
        self.parameterValueListButtonsLayout = QtWidgets.QVBoxLayout()
        self.parameterValueListButtonsLayout.setObjectName("parameterValueListButtonsLayout")
        self.parameterValueListLabel = QtWidgets.QLabel(parameterDialog)
        self.parameterValueListLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.parameterValueListLabel.setObjectName("parameterValueListLabel")
        self.parameterValueListButtonsLayout.addWidget(self.parameterValueListLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.parameterValueListButtonsLayout.addItem(spacerItem)
        self.newParameterValueButton = QtWidgets.QPushButton(parameterDialog)
        self.newParameterValueButton.setObjectName("newParameterValueButton")
        self.parameterValueListButtonsLayout.addWidget(self.newParameterValueButton)
        self.deleteParameterValueButton = QtWidgets.QPushButton(parameterDialog)
        self.deleteParameterValueButton.setObjectName("deleteParameterValueButton")
        self.parameterValueListButtonsLayout.addWidget(self.deleteParameterValueButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.parameterValueListButtonsLayout.addItem(spacerItem1)
        self.parameterValueListLayout.addLayout(self.parameterValueListButtonsLayout)
        self.parametersValueList = QtWidgets.QListView(parameterDialog)
        self.parametersValueList.setObjectName("parametersValueList")
        self.parameterValueListLayout.addWidget(self.parametersValueList)
        self.gridLayout.addLayout(self.parameterValueListLayout, 1, 0, 1, 1)
        self.parameterDialogButtonsLayout = QtWidgets.QHBoxLayout()
        self.parameterDialogButtonsLayout.setObjectName("parameterDialogButtonsLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.parameterDialogButtonsLayout.addItem(spacerItem2)
        self.parameterOkButton = QtWidgets.QPushButton(parameterDialog)
        self.parameterOkButton.setObjectName("parameterOkButton")
        self.parameterDialogButtonsLayout.addWidget(self.parameterOkButton)
        self.parameterCancelButton = QtWidgets.QPushButton(parameterDialog)
        self.parameterCancelButton.setObjectName("parameterCancelButton")
        self.parameterDialogButtonsLayout.addWidget(self.parameterCancelButton)
        self.gridLayout.addLayout(self.parameterDialogButtonsLayout, 2, 0, 1, 1)

        self.retranslateUi(parameterDialog)
        QtCore.QMetaObject.connectSlotsByName(parameterDialog)

    def retranslateUi(self, parameterDialog):
        _translate = QtCore.QCoreApplication.translate
        parameterDialog.setWindowTitle(_translate("parameterDialog", "Dialog"))
        self.parameterNameLabel.setText(_translate("parameterDialog", "Nazwa parametru:"))
        self.parameterValueListLabel.setText(_translate("parameterDialog", "Wartości:"))
        self.newParameterValueButton.setText(_translate("parameterDialog", "Nowy"))
        self.deleteParameterValueButton.setText(_translate("parameterDialog", "Usuń"))
        self.parameterOkButton.setText(_translate("parameterDialog", "OK"))
        self.parameterCancelButton.setText(_translate("parameterDialog", "Anuluj"))

