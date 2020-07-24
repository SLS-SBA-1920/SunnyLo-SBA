import tkinter as tk

menuBar = None


def initMenu(root):
    global menuBar
    menuBar = tk.Menu(root)

    from packages.menus.accountMenu import initAccountMenu
    initAccountMenu(menuBar)

    from packages.menus.windowMenu import initWindowMenu
    initWindowMenu(root, menuBar)

    from packages.menus.helpMenu import initHelpMenu
    initHelpMenu(menuBar)

    root.config(menu=menuBar)
