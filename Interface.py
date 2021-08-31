'''
Base file for the interface.
'''
from posixpath import commonpath
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msg
from tkinter import filedialog
from typing import Collection
import cv2
import os
from  PIL import Image, ImageTk

class MainWindow():
    
    PATH = ''
    SIGNS = ("Proíbido Retonar a Esquerda", "Duplo Sentido de Circulação", "Proíbido Ultrapassar", "Proibido estacionar")
    POSITION_CAM = ("Horizontal", "Vertical")
    
    def __init__(self):
        # Building the main window
        self.window = tk.Tk()
        self.window.geometry("1280x720")
        
        self.trafficSigns()
        
        self.frameRight = tk.Frame(self.window,width=280, height=720)
        self.frameRight.pack(side=tk.RIGHT)
        self.frameLeft = tk.Frame(self.window,width=1000, height=720, background='gray40')
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
        
        
        #Setting the Rules part
        self.option_Var1 = StringVar(self.frameRight)
        self.option_Var2 = StringVar(self.frameRight)
        self.option_Var3 = StringVar(self.frameRight)
        
        self.label = Label(self.frameRight, text="Definição das Regras")
        self.label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        
        self.label1 = Label(self.frameRight, text="Posição da câmera")
        self.label1.grid(column=0, row=1, sticky=tk.W, pady=5, padx=5)
        
        self.options1 = OptionMenu(self.frameRight, self.option_Var1, self.POSITION_CAM[0], *self.POSITION_CAM)
        self.options1.grid(column=1, row=1, sticky=tk.W, pady=5, padx=15)
        
        self.label2 = Label(self.frameRight, text="Placas de Trânsito")
        self.label2.grid(column=0, row=2, sticky=tk.W, pady=5, padx=5)
        
        self.options2 = OptionMenu(self.frameRight, self.option_Var2, self.SIGNS[0], *self.SIGNS)
        self.options2.grid(column=1, row=2, sticky=tk.W, pady=5, padx=15)
        
        self.label3 = Label(self.frameRight, text="Fluxo do Tráfego")
        self.label3.grid(column=0, row=3, sticky=tk.W, pady=5, padx=5)
        
        self.options3 = OptionMenu(self.frameRight, self.option_Var3, self.POSITION_CAM[0], *self.POSITION_CAM)
        self.options3.grid(column=1, row=3, sticky=tk.W, pady=5, padx=15)
        
        self.button = Button(self.frameRight, text="Aplicar", background="gray50")
        self.button.grid(column=2, row=4, sticky=tk.W, pady=5, padx=5)
        # Executing application
        self.window.mainloop()
        
    def exit(self):
        quit()
        
    def trafficSigns(self):
        direct = "C:/Users/Manassés/Desktop/UFPI/Iniciação/GUI-for-Video-Segmentation-Classification/Traffic-Signs"
        for root, dirs, files in os.walk(direct, topdown=True):
            for file in files:
                print(file)
                #self.SIGNS.append(PhotoImage(file=root+"/"+file)) 
    
    def openFile(self):
        self.PATH = filedialog.askopenfilename()
    
    def saveFile(self):
        pass
        
if __name__ == "__main__":
    mainwindow = MainWindow()