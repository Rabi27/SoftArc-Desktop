# -*- coding: utf-8 -*-
"""

@author: RabiSiddique
"""

import sys

from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys 
from MyTable import MyTable


class Table(QDialog):
    def __init__(self,mylist,extension):
        super(Table, self).__init__()
        self.ui = MyTable()
        self.ui.setupUi(self,mylist,extension)
      
        
     
        
        

            
            