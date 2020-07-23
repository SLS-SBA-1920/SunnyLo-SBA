import tkinter as tk

fullScreen = False


def initWindowMenu(root, menuBar):
    windowMenu = tk.Menu(menuBar, tearoff=0)
    windowMenu.add_command(label="Full Screen", command=lambda: fullScreenToggle(root, windowMenu), accelerator="F11")
    windowMenu.add_command(label="Maximise", command=lambda: root.state('zoomed'))
    windowMenu.add_command(label="Minimise", command=lambda: root.iconify())
    windowMenu.add_separator()
    windowMenu.add_command(label="Exit", command=root.quit)
    menuBar.add_cascade(label="Window", menu=windowMenu)

    root.bind("<Escape>", lambda e: disableFullScreen(root, windowMenu))
    root.bind("<F11>", lambda e: fullScreenToggle(root, windowMenu))


def fullScreenToggle(root, windowMenu):
    global fullScreen
    if fullScreen:
        disableFullScreen(root, windowMenu)
    else:
        enableFullScreen(root, windowMenu)


def disableFullScreen(root, windowMenu):
    global fullScreen
    root.attributes('-fullscreen', False)
    fullScreen = False
    windowMenu.entryconfig(0, label="Full Screen")


def enableFullScreen(root, windowMenu):
    global fullScreen
    fullScreen = True
    root.attributes('-fullscreen', True)
    windowMenu.entryconfig(0, label="Exit Full Screen")
