# -*- coding: utf-8 -*-
"""
@author: RabiSiddique
"""

from PyQt5 import QtWidgets

from ProjectUI import Ui_MainWindow  
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
from FileScanner import FileScanner
from DisplayContent import DisplayContent
from tkinter import filedialog
from tkinter import *
import os
from Table import Table


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.setFixedSize(600, 500)
        self.ui.setupUi(self)
        self.ButtonsCustomization()
        self.setIcons()
        self.ui.b1.clicked.connect(self.clicked1)
        self.ui.b2.clicked.connect(self.clicked2)
        self.ui.b3.clicked.connect(self.clicked3)
        self.ui.bj1.clicked.connect(self.Select_File)
        self.ui.bj2.clicked.connect(self.Select_Project)
        self.ui.bc1.clicked.connect(self.Select_File)
        self.ui.bc2.clicked.connect(self.Select_Project)
        self.ui.bcs1.clicked.connect(self.Select_File)
        self.ui.bcs2.clicked.connect(self.Select_Project)
        self.ui.homeButton.clicked.connect(self.clicked4)
        self.ui.ExitButton.clicked.connect(self.close)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.iconA = QtGui.QIcon()
        self.iconA.addPixmap(QtGui.QPixmap("photos/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msg.setWindowIcon(self.iconA)
        self.msg.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color:#663399;}\n")
        self.extensionfile = ''
        self.fp = ''
       
        
        
    
        
    
    def clicked1(self):
        self.ui.stack.setCurrentWidget(self.ui.p1)
        self.extensionfile = '*.java'
        self.fp = 'Java'
    
        
    def clicked2(self):
        self.ui.stack.setCurrentWidget(self.ui.p3)
        self.extensionfile = '*.cs'
        self.fp = 'C#'
        
        
    def clicked3(self):
        self.ui.stack.setCurrentWidget(self.ui.p2)  
        self.extensionfile = '*.cpp'
        self.fp = 'C++'
        
    def clicked4(self):
        self.ui.stack.setCurrentWidget(self.ui.p0)   
        
        
    
    def Select_File(self):
        root = Tk()
        root.withdraw()
        self.filename = filedialog.askopenfilenames(initialdir='/', title='Select a File', 
                                                   filetype=((self.fp,self.extensionfile),))
        if self.filename:
            self.scanner = FileScanner()
            self.data = self.scanner.Project_Scanner(self.filename)
            self.Display(self.data)
        else:
            self.msg.setText("No File Selected")
            self.msg.setInformativeText('Please Select a File to Proceed')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
     
    
    def Select_Project(self):
        root = Tk()
        root.withdraw()
        self.folder_selected = filedialog.askdirectory(initialdir='/', title='Select Folder')
        if self.folder_selected:
            self.files = self.get_Files(self.folder_selected)
         
            file_extension = os.path.splitext(self.files[0])
            #print(file_extension[1])
            print(self.extensionfile[1:len(self.extensionfile)])
            if file_extension[1] == self.extensionfile[1:len(self.extensionfile)]:
                self.scanner = FileScanner()
                self.data = self.scanner.Project_Scanner(self.files)
                self.Display(self.data)
            else:
                self.msg.setText("Select appropraite Folder")
                self.msg.setInformativeText("Please Select a Folder Containing "+self.fp+" files.")
                self.msg.setWindowTitle("Error")
                self.msg.exec_()
                
            
            
            
        else:
            self.msg.setText("No Folder Selected")
            self.msg.setInformativeText('Please Select a Folder to Proceed')
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
        
        
    def get_Files(self,f):
        self.filenames = os.listdir(f)
        self.files = [] 
        for filename in self.filenames:
            self.files.append(os.path.join(f, filename))
        return self.files
    
    def Display(self,data):
        displayer = DisplayContent()
        
        if data[1] == '.java' or data[1] == '.cpp' or data[1] == '.cs':
            extension = data[1]
            displayer.display_A(data[0])
            mylist = data[0]
            self.table = Table(mylist,data[1])
            self.table.show()
            '''    
        else:
            extension = '.cs'
            mylist=data[0]
            clist = data[2]
            l = data[3]
            interfaces = []
            for classes in clist:
     
                if 'Interface' in classes:
                    interfaces.append(classes.split(' ',1)[0])
            
    
            count = 0
            var = ''
    
             
            for e in l:
                if e != [] and e[0] not in interfaces:
                    var = e[0]
                    e.remove(e[0])
                    mylist[count][3] = var
                    mylist[count][4] = l[count]
                count = count + 1
            #displayer.display_A(data[0])
            self.table = Table(mylist,extension)
            self.table.show() '''
            
    def ButtonsCustomization(self):
    
        self.ui.b1.setIconSize(QSize(16, 16))
        self.ui.b2.setIconSize(QSize(16, 16))
        self.ui.b3.setIconSize(QSize(16,16))
        self.ui.homeButton.setIconSize(QSize(16, 16))
        self.ui.ExitButton.setIconSize(QSize(16, 16))
        #self.ui.HelpButton.setIconSize(QSize(16, 16))
        
        self.ui.homeButton.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color:#663399;}\n" 
    "QPushButton:hover {background-color:#7A63FF ;}\n" 
    "QPushButton:focus {background-color:#7A63FF;}"
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
        
        self.ui.b1.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color:#663399;}\n" 
    "QPushButton:hover {background-color:#7A63FF ;}\n" 
    "QPushButton:focus {background-color:#7A63FF;}"
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
        
      
        self.ui.b2.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color:#663399;}\n" 
    "QPushButton:hover {background-color:#7A63FF ;}\n" 
    "QPushButton:focus {background-color:#7A63FF;}"
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
        
        self.ui.b3.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color:#663399;}\n" 
    "QPushButton:hover {background-color:#7A63FF ;}\n" 
    "QPushButton:focus {background-color:#7A63FF;}"
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
       
        
        self.ui.ExitButton.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color:#663399;}\n" 
    "QPushButton:hover {background-color:#7A63FF ;}\n" 
    "QPushButton:focus {background-color:#7A63FF;}\n"
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
        
        '''self.ui.HelpButton.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color:#663399;}\n" 
    "QPushButton:hover {background-color:#7A63FF ;}\n" 
    "QPushButton:focus {background-color:#7A63FF;}"
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
    '''
            
        self.ui.bj1.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color: #663399;}\n" 
    "QPushButton:hover:!pressed {background-color:#7A63FF;}\n"
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
        
        self.ui.bj2.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color: #663399;}\n" 
    "QPushButton:hover {background-color:#7A63FF;}\n"  
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
        
        self.ui.bc1.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color: #663399;}\n" 
    "QPushButton:hover:!pressed {background-color:#7A63FF;}\n"
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
        
        self.ui.bc2.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color: #663399;}\n" 
    "QPushButton:hover {background-color:#7A63FF;}\n"  
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
        
        self.ui.bcs1.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color:#663399;}\n" 
    "QPushButton:hover:!pressed {background-color:#7A63FF;}\n"
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
        
        self.ui.bcs2.setStyleSheet("QPushButton { color: rgb(255,255,255);}\n" "QPushButton { background-color: #663399;}\n" 
    "QPushButton:hover {background-color:#7A63FF;}\n"  
    "QPushButton:pressed {background-color: rgb(224, 0, 0);}")
        
        
        
    def setIcons(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photos/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.b1.setIcon(icon)
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("photos/C#.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.b2.setIcon(icon1)
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("photos/c++.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.b3.setIcon(icon2)
        
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("photos/ho.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.homeButton.setIcon(icon3)
        
       # icon4 = QtGui.QIcon()
       # icon4.addPixmap(QtGui.QPixmap("photos/HelpButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.ui.HelpButton.setIcon(icon4)
        
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("photos/exitButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.ExitButton.setIcon(icon5)
        
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("photos/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.bj1.setIcon(icon6)
        
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("photos/Folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.bj2.setIcon(icon7)
        
        self.ui.bc1.setIcon(icon6)
        self.ui.bc2.setIcon(icon7)
        self.ui.bcs1.setIcon(icon6)
        self.ui.bcs2.setIcon(icon7)
    

            

app = QtWidgets.QApplication([])

style = """
  
     QPushButton{
  border: 1px;
  border-radius : 4px; 
  color :white;
  font-weight:bold;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
    
    }
     
  

"""   
app.setStyleSheet(style)
application = MyWindow()

application.show()

sys.exit(app.exec())