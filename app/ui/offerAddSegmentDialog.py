# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/offerAddSegmentDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(387, 275)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 230, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 341, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 17))
        self.label.setObjectName("label")
        self.lineEditB = QtWidgets.QLineEdit(Dialog)
        self.lineEditB.setGeometry(QtCore.QRect(20, 90, 341, 27))
        self.lineEditB.setObjectName("lineEditB")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 171, 17))
        self.label_2.setObjectName("label_2")
        self.lineEditC = QtWidgets.QLineEdit(Dialog)
        self.lineEditC.setGeometry(QtCore.QRect(20, 140, 341, 27))
        self.lineEditC.setObjectName("lineEditC")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 171, 17))
        self.label_3.setObjectName("label_3")
        self.lineEditD = QtWidgets.QLineEdit(Dialog)
        self.lineEditD.setGeometry(QtCore.QRect(20, 190, 341, 27))
        self.lineEditD.setObjectName("lineEditD")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 171, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dodawanie segmentu"))
        self.label.setText(_translate("Dialog", "Nazwa segmentu:"))
        self.label_2.setText(_translate("Dialog", "Parametr ceny B:"))
        self.label_3.setText(_translate("Dialog", "Parametr ceny C:"))
        self.label_4.setText(_translate("Dialog", "Parametr ceny D:"))

