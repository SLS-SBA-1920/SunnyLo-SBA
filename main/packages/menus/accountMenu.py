import tkinter as tk
import sys
import os
from packages.gui import getAdminFrame
from packages.guis.adminFrame import loadUsers

accountMenu = None


def initAccountMenu(menuBar):
    global accountMenu

    accountMenu = tk.Menu(menuBar, tearoff=0)
    accountMenu.add_command(label="Login", command=login)
    accountMenu.add_command(label="Logout", state="disabled", command=restartApp)
    accountMenu.add_separator()
    accountMenu.add_command(label="Open Admin Menu", state="disabled", command=openAdminMenu)
    menuBar.add_cascade(label="Account", menu=accountMenu)


def login():
    from packages.gui import getSigninFrame
    getSigninFrame().tkraise()


def setMenuStatus(name, state):
    global accountMenu
    accountMenu.entryconfig(name, state=state)


def restartApp():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def openAdminMenu():
    getAdminFrame().tkraise()
    loadUsers()
