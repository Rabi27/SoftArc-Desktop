
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photos/ee.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameMenu = QtWidgets.QFrame(self.centralwidget)
        self.frameMenu.setGeometry(QtCore.QRect(0, 0, 180, 500))
        self.frameMenu.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frameMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.homeButton = QtWidgets.QPushButton(self.frameMenu)
        self.homeButton.setGeometry(QtCore.QRect(0, 190, 180, 40))
        self.homeButton.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        
        self.homeButton.setObjectName("homeButton")
        
        
        self.frameMenu.setObjectName("frameMenu")
        self.b1 = QtWidgets.QPushButton(self.frameMenu)
        self.b1.setGeometry(QtCore.QRect(0, 230, 180, 40))
        
        
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.frameMenu)
        self.b2.setGeometry(QtCore.QRect(0, 270, 180, 40))
       
        
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.frameMenu)
        self.b3.setGeometry(QtCore.QRect(0, 310, 180, 40))
      
        
        self.b3.setObjectName("b3")
        '''
        self.HelpButton = QtWidgets.QPushButton(self.frameMenu)
        self.HelpButton.setGeometry(QtCore.QRect(0, 350, 180, 40))
        self.HelpButton.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        
        self.HelpButton.setObjectName("HelpButton")
        '''
        self.ExitButton = QtWidgets.QPushButton(self.frameMenu)
        self.ExitButton.setGeometry(QtCore.QRect(50, 440, 84, 40))
        self.ExitButton.setStyleSheet("color: rgb(0, 85, 0);\n"
"background-color: rgb(255, 255, 255);")
        
        self.ExitButton.setObjectName("ExitButton")
        self.topLogo = QtWidgets.QLabel(self.frameMenu)
        self.topLogo.setGeometry(QtCore.QRect(20, 20, 141, 141))
        self.topLogo.setStyleSheet("border-radius: 50px;")
        self.topLogo.setText("")
        self.topLogo.setPixmap(QtGui.QPixmap("photos/ee.PNG"))
        self.topLogo.setObjectName("topLogo")
    
        self.stack = QtWidgets.QStackedWidget(self.centralwidget)
        self.stack.setGeometry(QtCore.QRect(180, 0, 421, 500))
        self.stack.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.stack.setObjectName("stack")
        self.p0 = QtWidgets.QWidget()
        self.p0.setObjectName("p0")
        self.label = QtWidgets.QLabel(self.p0)
        self.label.setGeometry(QtCore.QRect(70, 100, 271, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photos/logo2.PNG"))
        self.label.setObjectName("label")
        self.stack.addWidget(self.p0)
        self.p1 = QtWidgets.QWidget()
        self.p1.setObjectName("p1")
        self.frame1 = QtWidgets.QFrame(self.p1)
        self.frame1.setGeometry(QtCore.QRect(0, 0, 411, 500))
        self.frame1.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.bj1 = QtWidgets.QPushButton(self.frame1)
        self.bj1.setGeometry(QtCore.QRect(110, 310, 180, 40))
       
        
        
        self.bj1.setIconSize(QSize(34, 34))
        self.bj1.setObjectName("bj1")
        self.bj2 = QtWidgets.QPushButton(self.frame1)
        self.bj2.setGeometry(QtCore.QRect(110, 390, 180, 40))
        
        
        
        
        self.bj2.setIconSize(QSize(34, 34))
        self.bj2.setObjectName("bj2")
        self.bj = QtWidgets.QLabel(self.frame1)
        self.bj.setGeometry(QtCore.QRect(100, 10, 241, 261))
        self.bj.setText("")
        self.bj.setPixmap(QtGui.QPixmap("photos/download.png"))
        self.bj.setObjectName("bj")
        self.stack.addWidget(self.p1)
        self.p2 = QtWidgets.QWidget()
        self.p2.setObjectName("p2")
        self.frame2 = QtWidgets.QFrame(self.p2)
        self.frame2.setGeometry(QtCore.QRect(0, 0, 411, 500))
        self.frame2.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.bc1 = QtWidgets.QPushButton(self.frame2)
        self.bc1.setGeometry(QtCore.QRect(100, 310, 180, 40))
    
       
        self.bc1.setIconSize(QSize(34, 34))
        self.bc1.setObjectName("bc1")
        self.bc2 = QtWidgets.QPushButton(self.frame2)
        self.bc2.setGeometry(QtCore.QRect(100, 390, 180, 40))
    
    
       
        self.bc2.setIconSize(QSize(34, 34))
        self.bc2.setObjectName("bc2")
        self.bc = QtWidgets.QLabel(self.frame2)
        self.bc.setGeometry(QtCore.QRect(100, 10, 251, 231))
        self.bc.setText("")
        self.bc.setPixmap(QtGui.QPixmap("photos/c++.png"))
        self.bc.setObjectName("bc")
        self.stack.addWidget(self.p2)
        self.p3 = QtWidgets.QWidget()
        self.p3.setObjectName("p3")
        self.frame3 = QtWidgets.QFrame(self.p3)
        self.frame3.setGeometry(QtCore.QRect(0, 0, 411, 500))
        self.frame3.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        self.bcs1 = QtWidgets.QPushButton(self.frame3)
        self.bcs1.setGeometry(QtCore.QRect(100, 310, 180, 40))
        
        
       
        self.bcs1.setIconSize(QSize(34, 34))
        self.bcs1.setObjectName("bcs1")
        self.bcs2 = QtWidgets.QPushButton(self.frame3)
        self.bcs2.setGeometry(QtCore.QRect(100, 390, 180,40))
      
        
        self.bcs2.setIconSize(QSize(34, 34))
        self.bcs2.setObjectName("bcs2")
        self.bcs = QtWidgets.QLabel(self.frame3)
        self.bcs.setGeometry(QtCore.QRect(100, 10, 251, 231))
        self.bcs.setText("")
        self.bcs.setPixmap(QtGui.QPixmap("photos/C#.png"))
        self.bcs.setObjectName("bcs")
        self.stack.addWidget(self.p3)
      
        
     
        MainWindow.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(MainWindow)
        self.stack.setCurrentWidget(self.p0)
    
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SoftArc Project"))
        self.b1.setText(_translate("MainWindow", "Select Java File/Project"))
        self.b2.setText(_translate("MainWindow", "Select C# File/Project"))
        self.b3.setText(_translate("MainWindow", "Select C++ File/Project"))
        self.homeButton.setText(_translate("MainWindow", "Home"))
        #self.HelpButton.setText(_translate("MainWindow", "Help"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))
        self.bj1.setText(_translate("MainWindow", "Choose File(s)"))
        self.bj2.setText(_translate("MainWindow", "Choose Folder"))
        self.bc1.setText(_translate("MainWindow", "Choose File(s)"))
        self.bc2.setText(_translate("MainWindow", "Choose Folder"))
        self.bcs1.setText(_translate("MainWindow", "Choose File(s)"))
        self.bcs2.setText(_translate("MainWindow", "Choose Folder"))
        
        
        