# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabZamowienia = QtWidgets.QWidget()
        self.tabZamowienia.setObjectName("tabZamowienia")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabZamowienia)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.pushButton_DodajFakture = QtWidgets.QPushButton(self.tabZamowienia)
        self.pushButton_DodajFakture.setObjectName("pushButton_DodajFakture")
        self.horizontalLayout_1.addWidget(self.pushButton_DodajFakture)
        self.pushButton_3 = QtWidgets.QPushButton(self.tabZamowienia)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_1.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem)
        self.verticalLayout_1.addLayout(self.horizontalLayout_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.tabZamowienia)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.tabZamowienia)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.tabZamowienia)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.tabZamowienia)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.tabZamowienia)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.tabZamowienia)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.dateEdit = QtWidgets.QDateEdit(self.tabZamowienia)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.label_4 = QtWidgets.QLabel(self.tabZamowienia)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tabZamowienia)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.tabZamowienia)
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_1.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.tabZamowienia)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(700, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_1.addWidget(self.tableWidget)
        self.verticalLayout_1.setStretch(2, 1)
        self.gridLayout_2.addLayout(self.verticalLayout_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabZamowienia, "")
        self.tabKlienci = QtWidgets.QWidget()
        self.tabKlienci.setObjectName("tabKlienci")
        self.tabWidget.addTab(self.tabKlienci, "")
        self.tabOferta = QtWidgets.QWidget()
        self.tabOferta.setObjectName("tabOferta")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tabOferta)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.tabOferta)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.listView = QtWidgets.QListView(self.tabOferta)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.tabOferta)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.treeView = QtWidgets.QTreeView(self.tabOferta)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabOferta, "")
        self.tabRaporty = QtWidgets.QWidget()
        self.tabRaporty.setObjectName("tabRaporty")
        self.tabWidget.addTab(self.tabRaporty, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_DodajFakture.setText(_translate("MainWindow", "Nowe zamówienie"))
        self.pushButton_3.setText(_translate("MainWindow", "Edycja  zamówienia"))
        self.label_2.setText(_translate("MainWindow", "Wyszukiwanie:"))
        self.pushButton.setText(_translate("MainWindow", "LUPA"))
        self.label.setText(_translate("MainWindow", "Pokaż zamówienia:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "wszystkie"))
        self.comboBox.setItemText(1, _translate("MainWindow", "zakończone"))
        self.comboBox.setItemText(2, _translate("MainWindow", "anulowane"))
        self.comboBox.setItemText(3, _translate("MainWindow", "w trakcie realizacji"))
        self.comboBox.setItemText(4, _translate("MainWindow", "gotowe"))
        self.comboBox.setItemText(5, _translate("MainWindow", "złożone"))
        self.label_3.setText(_translate("MainWindow", "Okres od:"))
        self.label_4.setText(_translate("MainWindow", "do:"))
        self.pushButton_2.setText(_translate("MainWindow", "->"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nazwa klienta"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Data złożenia"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Data zakończenia"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Kwota"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabZamowienia), _translate("MainWindow", "Zamówienia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabKlienci), _translate("MainWindow", "Klienci"))
        self.label_5.setText(_translate("MainWindow", "Dostępne modele:"))
        self.label_6.setText(_translate("MainWindow", "Segmenty dostępne w ramach wybranego modelu:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOferta), _translate("MainWindow", "Oferta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRaporty), _translate("MainWindow", "Raporty"))

