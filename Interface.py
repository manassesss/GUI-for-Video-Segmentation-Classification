'''
Base file for the interface.
'''
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import filedialog


class MainWindow(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.geometry("800x600")
        self.window = tk.Tk()
        self.menubar = tk.Menu(self.window)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.openFile, accelerator="Ctrl+O")
        self.filemenu.add_command(label="Save", command=self.saveFile, accelerator="Ctrl+S")
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.configure(menu=self.menubar)
        
    def openFile(self):
        self.window.filename = filedialog.askopenfilename()
    def saveFile(self):
        pass
        
if __name__ == "__main__":
    mainwindow = MainWindow()
    mainwindow.mainloop()