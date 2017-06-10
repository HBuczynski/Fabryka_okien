# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segmentDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_segmentDialog(object):
    def setupUi(self, segmentDialog):
        segmentDialog.setObjectName("segmentDialog")
        segmentDialog.resize(565, 472)
        self.gridLayout = QtWidgets.QGridLayout(segmentDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.segmentDialogButtonsLayout = QtWidgets.QHBoxLayout()
        self.segmentDialogButtonsLayout.setObjectName("segmentDialogButtonsLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.segmentDialogButtonsLayout.addItem(spacerItem)
        self.segmentOkButton = QtWidgets.QPushButton(segmentDialog)
        self.segmentOkButton.setObjectName("segmentOkButton")
        self.segmentDialogButtonsLayout.addWidget(self.segmentOkButton)
        self.segmentCancelButton = QtWidgets.QPushButton(segmentDialog)
        self.segmentCancelButton.setObjectName("segmentCancelButton")
        self.segmentDialogButtonsLayout.addWidget(self.segmentCancelButton)
        self.gridLayout.addLayout(self.segmentDialogButtonsLayout, 5, 0, 1, 1)
        self.segmentNameLayout = QtWidgets.QHBoxLayout()
        self.segmentNameLayout.setObjectName("segmentNameLayout")
        self.segmentNameLabel = QtWidgets.QLabel(segmentDialog)
        self.segmentNameLabel.setObjectName("segmentNameLabel")
        self.segmentNameLayout.addWidget(self.segmentNameLabel)
        self.segmentNameLineEdit = QtWidgets.QLineEdit(segmentDialog)
        self.segmentNameLineEdit.setObjectName("segmentNameLineEdit")
        self.segmentNameLayout.addWidget(self.segmentNameLineEdit)
        self.gridLayout.addLayout(self.segmentNameLayout, 2, 0, 1, 1)
        self.parameterListLayout = QtWidgets.QGridLayout()
        self.parameterListLayout.setObjectName("parameterListLayout")
        self.parameterListLabel = QtWidgets.QLabel(segmentDialog)
        self.parameterListLabel.setObjectName("parameterListLabel")
        self.parameterListLayout.addWidget(self.parameterListLabel, 0, 0, 1, 1)
        self.parameterList = QtWidgets.QListView(segmentDialog)
        self.parameterList.setObjectName("parameterList")
        self.parameterListLayout.addWidget(self.parameterList, 1, 0, 1, 1)
        self.parameterListButtonsLayout = QtWidgets.QVBoxLayout()
        self.parameterListButtonsLayout.setObjectName("parameterListButtonsLayout")
        self.newParameterButton = QtWidgets.QPushButton(segmentDialog)
        self.newParameterButton.setObjectName("newParameterButton")
        self.parameterListButtonsLayout.addWidget(self.newParameterButton)
        self.editParameterButton = QtWidgets.QPushButton(segmentDialog)
        self.editParameterButton.setObjectName("editParameterButton")
        self.parameterListButtonsLayout.addWidget(self.editParameterButton)
        self.deleteParameterButton = QtWidgets.QPushButton(segmentDialog)
        self.deleteParameterButton.setObjectName("deleteParameterButton")
        self.parameterListButtonsLayout.addWidget(self.deleteParameterButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.parameterListButtonsLayout.addItem(spacerItem1)
        self.parameterListLayout.addLayout(self.parameterListButtonsLayout, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.parameterListLayout, 4, 0, 1, 1)
        self.segmentDescriptionLayout = QtWidgets.QGridLayout()
        self.segmentDescriptionLayout.setObjectName("segmentDescriptionLayout")
        self.segmentDescriptionLabel = QtWidgets.QLabel(segmentDialog)
        self.segmentDescriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.segmentDescriptionLabel.setObjectName("segmentDescriptionLabel")
        self.segmentDescriptionLayout.addWidget(self.segmentDescriptionLabel, 0, 0, 1, 1)
        self.segmentDescriptionTextEdit = QtWidgets.QTextEdit(segmentDialog)
        self.segmentDescriptionTextEdit.setMaximumSize(QtCore.QSize(16777215, 150))
        self.segmentDescriptionTextEdit.setObjectName("segmentDescriptionTextEdit")
        self.segmentDescriptionLayout.addWidget(self.segmentDescriptionTextEdit, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.segmentDescriptionLayout, 3, 0, 1, 1)

        self.retranslateUi(segmentDialog)
        QtCore.QMetaObject.connectSlotsByName(segmentDialog)

    def retranslateUi(self, segmentDialog):
        _translate = QtCore.QCoreApplication.translate
        segmentDialog.setWindowTitle(_translate("segmentDialog", "Dialog"))
        self.segmentOkButton.setText(_translate("segmentDialog", "OK"))
        self.segmentCancelButton.setText(_translate("segmentDialog", "Anuluj"))
        self.segmentNameLabel.setText(_translate("segmentDialog", "Nazwa segmentu:"))
        self.parameterListLabel.setText(_translate("segmentDialog", "Parametry"))
        self.newParameterButton.setText(_translate("segmentDialog", "Nowy"))
        self.editParameterButton.setText(_translate("segmentDialog", "Edytuj"))
        self.deleteParameterButton.setText(_translate("segmentDialog", "Usuń"))
        self.segmentDescriptionLabel.setText(_translate("segmentDialog", "Opis:"))

