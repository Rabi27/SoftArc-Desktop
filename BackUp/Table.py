# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:08:43 2020

@author: RabiSiddique
"""

from PyQt5 import *
from PyQt5 import *
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class Table(QtWidgets.QDialog):
    def __init__(self, mylist,parent=None):
        super(Table, self).__init__(parent=parent)
        self.setObjectName(Dialog)
        self.setFixedSize(600, 500)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.grid = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)
        
        for i in range(len(mylist)):
                self.table1 = QTableWidget()
                self.table2 = QTableWidget()
                self.table3 = QTableWidget()
                
                
                if mylist[i][1] != []:
                    self.table1.setColumnCount(1)
                    self.table1.setRowCount(len(mylist[i][1]))
                    self.table1.setStyleSheet("color: rgb(0,0,0);\n"
"hover {background-color:#0277bd};")
                    self.table1.setFixedHeight(260)
                    for j in range(len(mylist[i][1])):
                        self.table1.setItem(j,0,QTableWidgetItem(mylist[i][1][j]))
                        
                else:
                    self.table1.setItem(0,0,QTableWidgetItem("Empty"))
                    
                if mylist[i][2] != []:  
                    self.table2.setColumnCount(1)
                    self.table2.setRowCount(len(mylist[i][2]))
                    self.table2.setStyleSheet("color: rgb(0, 0, 0);\n"
"hover {background-color:#0277bd};")
                    self.table2.setFixedHeight(260)
                    for k in range(len(mylist[i][2])):
                        self.table2.setItem(k,0,QTableWidgetItem(mylist[i][2][k]))
                else:
                    self.table2.setItem(0,0,QTableWidgetItem("Empty"))
                  
                if mylist[i][4] != []:    
                    self.table3.setColumnCount(1)
                    self.table3.setRowCount(len(mylist[i][4]))
                    self.table3.setStyleSheet("color: rgb(0, 0, 0);\n"
"hover {background-color:#0277bd};")
                    self.table3.setFixedHeight(260)
                    for l in range(len(mylist[i][4])):
                        self.table3.setItem(l,0,QTableWidgetItem(mylist[i][4][l]))
                else:
                    self.table3.setItem(0,0,QTableWidgetItem("Empty"))
                    
                self.lbl = QLabel()
                self.lbl.setAlignment(Qt.AlignCenter)
                
                if mylist[i][3] != "":
                    self.lbl.setText(mylist[i][0]+" Extends "+mylist[i][3])
                else:
                    self.lbl.setText(mylist[i][0])
                    
                        
                self.hBox = QHBoxLayout()
                self.hBox.addWidget(self.table1)
                self.hBox.addWidget(self.table2)
                self.hBox.addWidget(self.table3)
                self.vBox = QVBoxLayout()
                self.vBox.addWidget(self.lbl)
                self.vBox.addLayout(self.hBox)
                self.grid.addLayout(self.vBox,i,0)
                
                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)
                
                
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl.setText(_translate("Dialog", "ClassName Extends ClassName"))
        item = self.table1.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Variables"))
        item = self.table2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Methods"))
        item = self.table3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Interfaces"))