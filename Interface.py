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
import numpy as np
import os
from  PIL import Image, ImageTk

class MainWindow():
    
    PATH = ''
    SIGNS = ("Proíbido Retornar a Esquerda", "Duplo Sentido de Circulação", "Proíbido Ultrapassar", "Proibido estacionar")
    POSITION_CAM = ("Horizontal", "Vertical")
    ABOUTRULES = "As Regras defenidas levam em consideração a posição em que a camera está, as placas de trânsito que ele deve considerar e o fluxo do tráfego.\nPara cada uma dessas regras são apresentadas as seguintes opções:\n\nPosição da Câmera: \n- Horizontal\n- Vertical\n\nPlacas de Trânsito: \n- Proíbido Retonar a Esquerda\n- Duplo Sentido de Circulação\n- Proíbido Ultrapassar\n- Proibido estacionar\n\nFluxo do tráfego:\n- Horizontal\n- Vertical"
    
    def __init__(self):
        # Building the main window
        self.window = tk.Tk()
        #self.window.geometry("1280x720")
        
        self.trafficSigns()
        
        #self.frameRight = tk.Frame(self.window,width=280, height=720)
        #self.frameRight.pack(side=tk.RIGHT)
        #self.frameLeft = tk.Frame(self.window,width=1000, height=720, background='gray40')
        #self.frameLeft.pack(side=tk.LEFT)
        
        # Defining menubar
        self.menubar = tk.Menu(self.window)

        
        # Defining the FILE part of the manu bar
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.openFile, accelerator="Ctrl+O")
        self.filemenu.add_command(label="Save", command=self.saveFile, accelerator="Ctrl+S")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.exit, accelerator="Ctrl+F")
        
        # Defining the ABOUT part of the manu bar
        self.about = tk.Menu(self.menubar, tearoff=0)
        self.about.add_command(label="Project")
        self.about.add_command(label="Rules", command=self.rulesAbout)
        self.about.add_command(label="Developer")
        
        # Setting the parts of menu bar
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="About", menu=self.about)
        self.window.configure(menu=self.menubar)
        
        
        #Setting the RULES part
        self.option_Var1 = StringVar(self.window)
        self.option_Var2 = StringVar(self.window)
        self.option_Var3 = StringVar(self.window)
        
        self.label = Label(self.window, text="Definição das Regras")
        self.label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        '''
        self.label1 = Label(self.window, text="Posição da câmera")
        self.label1.grid(column=0, row=1, sticky=tk.W, pady=5, padx=5)
        
        self.options1 = OptionMenu(self.window, self.option_Var1, self.POSITION_CAM[0], *self.POSITION_CAM)
        self.options1.grid(column=1, row=1, sticky=tk.W, pady=5, padx=15)
        '''
        self.label2 = Label(self.window, text="Placas de Trânsito")
        self.label2.grid(column=0, row=2, sticky=tk.W, pady=5, padx=5)
        
        self.options2 = OptionMenu(self.window, self.option_Var2, self.SIGNS[0], *self.SIGNS)
        self.options2.grid(column=1, row=2, sticky=tk.W, pady=5, padx=15)
        
        self.label3 = Label(self.window, text="Fluxo do Tráfego")
        self.label3.grid(column=0, row=3, sticky=tk.W, pady=5, padx=5)
        
        self.options3 = OptionMenu(self.window, self.option_Var3, self.POSITION_CAM[0], *self.POSITION_CAM)
        self.options3.grid(column=1, row=3, sticky=tk.W, pady=5, padx=15)
        
        self.button = Button(self.window, text="Aplicar", background="gray50")
        self.button.grid(column=2, row=4, sticky=tk.W, pady=5, padx=5)
        # Executing application
        self.window.mainloop()
        
    def exit(self):
        quit()
        
    def trafficSigns(self):
        direct = "GUI-for-Video-Segmentation-Classification/Traffic-Signs/traffic.jpg"
        #for root, dirs, files in os.walk(direct, topdown=True):
            #for file in files:
                #print(file)
                #self.SIGNS.append(PhotoImage(file=root+"/"+file)) 
    
    def openFile(self):
        path = 'GUI-for-Video-Segmentation-Classification/Traffic-Signs/TrafficSign01.png'
        print(path)
        print(type(path))
        im = cv2.imread(path)
        print(type(im))
        gray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
        cv2.imshow("im", gray)
        cv2.waitKey(0)
        
    def saveFile(self):
        pass
    
    def rulesAbout(self):
        labelAbout = LabelFrame(self.frameLeft, text="Sobre as Regras")
        labelAbout.pack(fill="both", expand="yes")
        
        labelAboutText = Label(self.frameLeft, text=self.ABOUTRULES)
        labelAboutText.pack(fill=X)
    
    def projectAbout(self):
        pass
    
    def developerAbout(self):
        pass
    
if __name__ == "__main__":
    mainwindow = MainWindow()