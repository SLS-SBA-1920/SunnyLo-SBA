# Import all dependencies
import tkinter as tk

from resizeCanvas import ResizingCanvas

# All of the frame init
root = None
mainFrame = None
signinFrame = None
signupFrame = None
loginedFrame = None
adminControlFrame = None


def startGUI():
    root = tk.Tk()
    root.title("St. Louis School ICT SBA by SunnyLo")

    # Create the window in the centre of the screen
    positionRight = int(root.winfo_screenwidth() / 2 - 1280 / 2)
    positionDown = int(root.winfo_screenheight() / 2 - 720 / 2)
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Setup a background image of the GUI
    canvas = ResizingCanvas(root, width=1280, height=720)
    canvas.pack(fill="both", expand=True)

    initLoginFrame()
    initMainFrame()

    # Keeps the GUI running
    root.mainloop()


def initMainFrame():
    mainFrame = tk.Frame(root)
    mainFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    buttonSignin = tk.Button(mainFrame, text="Sign in")
    buttonSignin.pack()

    buttonSignup = tk.Button(mainFrame, text="Sign up")
    buttonSignup.pack()

    mainFrame.tkraise()


def initLoginFrame():
    signinFrame = tk.Frame(root, bg="blue")
    signinFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    button = tk.Button(signinFrame, text="Login")
    button.pack()

    label = tk.Label(signinFrame, text="AAAAA", bg="yellow", font={"arial", 16})
    label.pack()

    entry = tk.Entry(signinFrame, bg="green")
    entry.pack()
