import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sys
import os


def initHelpMenu(menuBar):
    helpMenu = tk.Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About", command=helpPopup)
    helpMenu.add_separator()
    helpMenu.add_command(label="Reset Application", command=lambda: resetApp())
    menuBar.add_cascade(label="Help", menu=helpMenu)


def helpPopup():
    win = tk.Toplevel()
    win.title("About")

    size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
    positionRight = int(win.winfo_screenwidth() / 2 - size[0] / 2)
    positionDown = int(win.winfo_screenheight() / 2 - size[1] / 2)
    win.geometry("+{}+{}".format(positionRight, positionDown))

    l = tk.Label(win, text="St. Louis School ICT SBA by Lo Yung Sum")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Okay", command=win.destroy)
    b.grid(row=1, column=0)


def resetApp():
    MsgBox = tk.messagebox.askquestion('Reset Application', 'Are you sure you want to reset the application',
                                       icon='warning')
    if MsgBox == 'yes':
        def deleteFile(filePath):
            if os.path.exists(filePath):
                os.remove(filePath)

        deleteFile("../config.yml")
        deleteFile("data/data.json")

        python = sys.executable
        os.execl(python, python, *sys.argv)
