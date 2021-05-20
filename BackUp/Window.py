# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:17:36 2020

@author: RabiSiddique
"""

from FileScanner import FileScanner
from DisplayContent import DisplayContent
from tkinter import Frame,Button,Tk,Listbox,END,mainloop
from tkinter import *
from tkinter import filedialog
import os

class Window(object):
    
    def __init__(self,master):
        self.master = master
        self.master.title('SDA Project')
        self.master.geometry('600x400')
        self.master.config(bg='#fff')
        self.master.resizable(0,0)
        self.Add_Widgets()
    
    def Add_Widgets(self):
        self.TopFrame = Frame(self.master,bg='#42f498',width=600,height=100)
        self.TopFrame.grid(column=0,row=1)
        
        self.button_1 = Button(self.master,text='Select a File',width=10,height=2,bd=0,bg='#42f498',\
                              activebackground='#fff',activeforeground='#42f498',fg='#fff',command=self.Select_File)
        self.button_1.grid(column=0,row=2,padx=10,pady=10)
        self.button_2 = Button(self.master,text='Select a Project',width=12,height=2,bd=0,bg='#42f498',\
                              activebackground='#fff',activeforeground='#42f498',fg='#fff',command=self.Select_Project)
        self.button_2.grid(column=0,row=4,padx=10,pady=10)
        
    def Select_File(self):
        self.filename = filedialog.askopenfilename(initialdir='/', title='Select a File', filetype=(('Java','*.java'),('C++','*.cpp'),('C#','*.cs')))
        self.scanner = FileScanner()
        self.data = self.scanner.File_Scanner(self.filename)
        self.Display(self.data)
     
    
    def Select_Project(self):
        self.folder_selected = filedialog.askdirectory(initialdir='/', title='Select Folder')
        self.files = self.get_Files(self.folder_selected)
        self.scanner = FileScanner()
        self.data = self.scanner.Project_Scanner(self.files)
        self.Display(self.data)
        
        
    def get_Files(self,f):
        self.filenames = os.listdir(f)
        self.files = [] 
        for filename in self.filenames:
            self.files.append(os.path.join(f, filename))
        return self.files
    
    def Display(self,data):
        displayer = DisplayContent()
        if data[1] == '.java' or data[1] == '.cs':
            displayer.display_A(data[0])
        else:
            displayer.display_B(data[0],data[2],data[3])
            

        
#Create a Tk() object
app = Tk()
#Create a Window Object by Supplying the Tk() object into the Window Class
Window = Window(app)
#Update the Window Everytime
app.mainloop()
            
            
            
            
            
            

               
           







    
    

    

    