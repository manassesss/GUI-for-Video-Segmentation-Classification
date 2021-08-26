'''
Base file for the interface.
'''
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import filedialog
import cv2
import PIL.Image, PIL.ImageTk

class MainWindow():
    
    PATH = ''
    
    def __init__(self):
        # Building the main window
        self.window = tk.Tk()
        self.window.geometry("1280x720")
        
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

    def openFile(self):
        self.PATH = filedialog.askopenfilename()
        print(self.PATH)
        OpenVideo(self.PATH)
        
    
    def saveFile(self):
        pass
        
class OpenVideo():
    def __init__(self, path):
        print(path)
        self.image = cv2.imread(path, 0)
        cv2.imshow("Image", self.image)
        self.heigh, self.width = self.image.shape[:2]
        print(self.heigh, self.width)
        
if __name__ == "__main__":
    mainwindow = MainWindow()