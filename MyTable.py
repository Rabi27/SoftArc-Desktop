# -*- coding: utf-8 -*-
"""

@author: RabiSiddique
"""

from PyQt5 import *
from PyQt5 import *
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class MyTable(object):
    def setupUi(self, Dialog,mylist,extension):
        Dialog.setObjectName('Dialog')
        Dialog.setFixedSize(1200, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photos/ee.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.layout = QtWidgets.QHBoxLayout(Dialog)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.grid = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)
        modifiers = ['public','protected','private']
        datatype = ['String','int','float','boolean','void','double','long','short','char',
                         'byte','string','String[]','int[]','float[]','boolean[]','void',
                         'double[]','long[]','short[]','char[]','byte[]','string[]']
        
       
        
     
          
        
        for i in range(len(mylist)):
                self.table1 = QTableWidget()
                self.table1.setColumnCount(3)
                self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
                self.table1.setHorizontalHeaderLabels(['Access Modifier', 'Datatype', 'Name'])
                self.table1.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Interactive)
                self.table1.verticalHeader().setVisible(False)
                
                fnt = self.table1.font()
                fnt.setPointSize(12)
                self.table1.setFont(fnt)
                self.verticalLayout = QVBoxLayout()
                self.verticalLayout.setObjectName("verticalLayout")
                self.label = QLabel()
                self.label.setText("")
                self.label.setObjectName("label")
                self.label.setPixmap(QtGui.QPixmap("photos/Variables.PNG"))
                self.label.setStyleSheet("background-color:#000")
                self.label.setAlignment(Qt.AlignCenter) 
                self.label.adjustSize()
                self.verticalLayout.addWidget(self.label)
                self.verticalLayout.addWidget(self.table1)
                
                self.table2 = QTableWidget()
                self.table2.setColumnCount(4)
                self.table2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
                self.table2.setHorizontalHeaderLabels(['Access Modifier', 'Return Type', 'Name','Arguments'])
                #self.table2.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Interactive)
                header = self.table2.horizontalHeader()       
                header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
                header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
                self.table2.verticalHeader().setVisible(False)
                
                
                
                fnt = self.table2.font()
                fnt.setPointSize(12)
                self.table2.setFont(fnt)
                self.verticalLayout2 = QVBoxLayout()
                self.verticalLayout2.setObjectName("verticalLayout2")
                self.label2 = QLabel()
                self.label2.setText("")
                self.label2.setObjectName("label")
                self.label2.setPixmap(QtGui.QPixmap("photos/Methods.PNG"))
                self.label2.setStyleSheet("background-color:#000")
                self.label2.setAlignment(Qt.AlignCenter)
                self.label2.adjustSize()
                self.verticalLayout2.addWidget(self.label2)
                self.verticalLayout2.addWidget(self.table2)
               
  
               
              
                self.table1.horizontalHeader().setStretchLastSection(True)     
                self.table2.horizontalHeader().setStretchLastSection(True) 
                
           
                if mylist[i][1] != []:
                    self.table1.setRowCount(len(mylist[i][1]))
                    self.table1.setStyleSheet("color: rgb(0,0,0);\n"
"hover {background-color:#0277bd};")
                    self.table1.setFixedHeight(260)
                    vlist = mylist[i][1]
                    for j in range(len(vlist)):
                    
                        if '=' in vlist[j]:
                            index = vlist[j].index('=')
                            vlist[j] = vlist[j][0:index].strip()
                        
                    
                        l = list(vlist[j].split(' '))
                        
                        
                       
                        if len(l) == 2 and l[0] in datatype:
                            if extension == '.java':
                                self.table1.setItem(j,0,QTableWidgetItem('protected'))
                                self.table1.setItem(j,1,QTableWidgetItem(l[0]))
                                self.table1.setItem(j,2,QTableWidgetItem(l[1]))
                            else:
                                self.table1.setItem(j,0,QTableWidgetItem('private'))
                                self.table1.setItem(j,1,QTableWidgetItem(l[0]))
                                self.table1.setItem(j,2,QTableWidgetItem(l[1]))
                            
                        elif len(l)>2:
                            if l[0] in modifiers:
                                self.table1.setItem(j,0,QTableWidgetItem(l[0]))
                                self.table1.setItem(j,1,QTableWidgetItem(l[-2]))
                                self.table1.setItem(j,2,QTableWidgetItem(l[-1]))
                            
                            else:
                                if extension == '.java':
                                    self.table1.setItem(j,0,QTableWidgetItem('protected'))
                                else:
                                    self.table1.setItem(j,0,QTableWidgetItem('private'))
                                    
                                self.table1.setItem(j,1,QTableWidgetItem(l[-2]))
                                self.table1.setItem(j,2,QTableWidgetItem(l[-1]))

                          
            
                else:
                    self.table1.setItem(0,0,QTableWidgetItem("Empty"))
                    
                if mylist[i][2] != []:  
                    self.table2.setRowCount(len(mylist[i][2]))
                    self.table2.setStyleSheet("color: rgb(0, 0, 0);\n"
"hover {background-color:#0277bd};")
                    self.table2.setFixedHeight(260)
                    mlist = mylist[i][2]
                    for k in range(len(mlist)):
                        lis = list(mlist[k].split('('))
                        l1 = list(lis[0].split())
                        l2 = lis[1][0:-1]
                        
                        if len(l1) == 2 and l1[0] in datatype:
                            if extension == '.java':
                                self.table2.setItem(k,0,QTableWidgetItem('protected'))
                                self.table2.setItem(k,1,QTableWidgetItem(l1[0]))
                                self.table2.setItem(k,2,QTableWidgetItem(l1[1]))
                            else:
                                self.table2.setItem(k,0,QTableWidgetItem('private'))
                                self.table2.setItem(k,1,QTableWidgetItem(l1[0]))
                                self.table2.setItem(k,2,QTableWidgetItem(l1[1]))
                            
                        elif len(l1)>2:
                            if l1[0] in modifiers:
                                self.table2.setItem(k,0,QTableWidgetItem(l1[0]))
                                self.table2.setItem(k,1,QTableWidgetItem(l1[-2]))
                                self.table2.setItem(k,2,QTableWidgetItem(l1[-1]))
                            
                            else:
                                if extension == '.java':
                                    self.table2.setItem(k,0,QTableWidgetItem('protected'))
                                else:
                                    self.table2.setItem(k,0,QTableWidgetItem('private'))
                                    
                                self.table2.setItem(k,1,QTableWidgetItem(l1[-2]))
                                self.table2.setItem(k,2,QTableWidgetItem(l1[-1]))
                        
                        self.table2.setItem(k,3,QTableWidgetItem(l2))
                        
                      
                else:
                    self.table2.setItem(0,0,QTableWidgetItem("Empty"))
                  
                
                self.vBox = QVBoxLayout()
                self.lbl = QLabel()
                self.lbl.setAlignment(Qt.AlignCenter)
                self.lbl.setFixedHeight(120)
                self.lbl.setStyleSheet( " color: rgb(255,255,255); \
                                       background-color:#7A63FF; \
                                     font-weight:bold;      font-size:50px")
                
                if mylist[i][3] != "":
                    self.lbl.setText(mylist[i][0]+" Extends "+mylist[i][3])
                else:
                    self.lbl.setText(mylist[i][0])
                    
                self.vBox.addWidget(self.lbl)  
                    
                
                
                self.lbl1 = QLabel()
                self.lbl1.setAlignment(Qt.AlignCenter)
                self.lbl1.setFixedHeight(120)
                self.lbl1.setStyleSheet( " color: rgb(255,255,255); \
                                       background-color:#1E1E1E; \
                                     font-weight:bold;      font-size:50px")
                
                
                if mylist[i][4] != []:
                    self.lbl1 = QLabel()
                    self.lbl1.setAlignment(Qt.AlignCenter)
                    self.lbl1.setFixedHeight(120)
                    
                    if extension == '.cpp':
                        self.lbl1.setStyleSheet( " color: rgb(255,255,255); \
                                           background-color:#1E1E1E; \
                                     font-weight:bold;      font-size:50px")
                        string = ",".join(mylist[i][4])
                        self.lbl1.setText("Implements "+string)
                        self.lbl1.setText("Extends "+string)
                        self.vBox.addWidget(self.lbl1) 
                    else:
                        self.lbl1.setStyleSheet( " color: rgb(255,255,255); \
                                           background-color:#1E1E1E; \
                                     font-weight:bold;      font-size:50px")
                                     
                        string = ",".join(mylist[i][4])
                        self.lbl1.setText("Implements "+string)
                        self.vBox.addWidget(self.lbl1)  
                    
                    
                        
                self.hBox = QHBoxLayout()
                self.hBox.addLayout(self.verticalLayout)
                self.hBox.addLayout(self.verticalLayout2)
                self.vBox.addLayout(self.hBox)
                self.grid.addLayout(self.vBox,i,0)
                
                
                
                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)
                
                
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Table"))
        