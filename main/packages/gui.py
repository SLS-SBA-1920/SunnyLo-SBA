# Import all dependencies
import tkinter as tk
import sys
from .resizingCanvas import ResizingCanvas

# All of the frame init
root = None
initFrame = None
mainFrame = None
signinFrame = None
signupFrame = None
loginedFrame = None
adminControlFrame = None


def startGUI(*args, **kwargs):
    global root, mainFrame, signinFrame, signupFrame, initFrame
    root = tk.Tk()
    root.title("St. Louis School ICT SBA by SunnyLo")

    logo = tk.PhotoImage(file='../sources/icon.gif')
    root.call('wm', 'iconphoto', root._w, logo)

    if sys.platform == 'darwin':
        from Foundation import NSBundle
        bundle = NSBundle.mainBundle()
        if bundle:
            info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
            if info and info['CFBundleName'] == 'Python':
                info['CFBundleName'] = "SLS SBA"

    # Create the window in the centre of the screen
    positionRight = int(root.winfo_screenwidth() / 2 - 1280 / 2)
    positionDown = int(root.winfo_screenheight() / 2 - 720 / 2)
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Setup a background image of the GUI
    canvas = ResizingCanvas(root, width=1280, height=720)
    canvas.pack(fill="both", expand=True)

    # Init menu bar
    from .menus.mainMenu import initMenu
    initMenu(root)

    # Init all frames
    from .guis.signinFrame import initLoginFrame
    signinFrame = initLoginFrame(root)
    from .guis.signupFrame import initSignupFrame
    signupFrame = initSignupFrame(root)
    from .guis.mainFrame import initMainFrame
    mainFrame = initMainFrame(root, signinFrame, signupFrame)

    # Check if it is first init
    if len(args) == 1:
        from .guis.initFrame import initInitFrame
        initFrame = initInitFrame(root)

    # Keeps the GUI running
    root.mainloop()


def getMainFrame():
    return mainFrame


def getSigninFrame():
    return signinFrame


def getSignupFrame():
    return signupFrame
