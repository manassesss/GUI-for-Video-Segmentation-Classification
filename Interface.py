'''
Base file for the interface.
'''
from posixpath import commonpath
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msg
from tkinter import filedialog
import cv2
import os
from  PIL import Image, ImageTk

class MainWindow():
    
    PATH = ''
    SIGNS = []
    
    def __init__(self):
        # Building the main window
        self.window = tk.Tk()
        self.window.geometry("1280x720")
        
        self.trafficSigns()
        
        self.frameRight = tk.Frame(self.window,width=280, height=720, background='gray20')
        self.frameRight.pack(side=tk.RIGHT)
        self.frameLeft = tk.Frame(self.window,width=1000, height=720, background='gray7')
        self.frameLeft.pack(side=tk.LEFT)
        
        # Defining menubar
        self.menubar = tk.Menu(self.window)

        
        # Defining the file part of the manu bar
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.openFile, accelerator="Ctrl+O")
        self.filemenu.add_command(label="Save", command=self.saveFile, accelerator="Ctrl+S")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit, accelerator="Ctrl+F")
        
        # Defining the about part of the manu bar
        self.about = tk.Menu(self.menubar, tearoff=0)
        self.about.add_command(label="Project")
        self.about.add_command(label="Rules")
        self.about.add_command(label="Developer")
        
        # Setting the parts of menu bar
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="About", menu=self.about)
        self.window.configure(menu=self.menubar)
        
        # Executing application
        self.window.mainloop()
        
    def exit(self):
        quit()
        
    def trafficSigns(self):
        direct = "C:/Users/Manassés/Desktop/UFPI/Iniciação/GUI-for-Video-Segmentation-Classification/Traffic-Signs"
        for root, dirs, files in os.walk(direct, topdown=True):
            for file in files:
                print(file)
                self.SIGNS.append(PhotoImage(file=root+"/"+file))
    
    def openFile(self):
        self.PATH = filedialog.askopenfilename()
    
    def saveFile(self):
        pass
        
if __name__ == "__main__":
    mainwindow = MainWindow()