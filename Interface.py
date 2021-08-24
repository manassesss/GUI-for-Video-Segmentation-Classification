'''
Base file for the interface.
'''
import tkinter as tk
from tkinter import filedialog


class MainWindow(root):
    
    def __init__(self):
        pass
    def openFile () :
        window.filename = filedialog.askopenfilename()




window = tk.Tk()
menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open...")
filemenu.add_separator()

menubar.add_cascade(label="File", menu=filemenu)

window.config(menu=menubar)
window.mainloop()