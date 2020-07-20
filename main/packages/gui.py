# Import all dependencies
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from .resizingCanvas import ResizingCanvas

# All of the frame init
root = None
mainFrame = None
signinFrame = None
signupFrame = None
loginedFrame = None
adminControlFrame = None


def startGUI():
    global root
    root = tk.Tk()
    root.title("St. Louis School ICT SBA by SunnyLo")

    # Make the window content area transparent
    # root.wm_attributes("-transparent", True)
    # Set the root window background color to a transparent color
    # root.config(bg='systemTransparent')

    # Create the window in the centre of the screen
    positionRight = int(root.winfo_screenwidth() / 2 - 1280 / 2)
    positionDown = int(root.winfo_screenheight() / 2 - 720 / 2)
    root.geometry("+{}+{}".format(positionRight, positionDown))

    # Setup a background image of the GUI
    canvas = ResizingCanvas(root, width=1280, height=720)
    canvas.pack(fill="both", expand=True)

    # initLoginFrame()
    initMainFrame()


def initMainFrame():
    global root, mainFrame

    # Add white area on top of the white background
    mainFrame = tk.Frame(root)
    mainFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    # Centres all the elements in the frame
    subFrame = tk.Frame(mainFrame)
    subFrame.place(relx=0.5, rely=0.5)

    def enter(e, btn):
        print(btn, "entered")

    def leave(e, btn):
        print(btn, "leaved")

    signinImg1 = tk.PhotoImage(file="../sources/buttons/login-01.png")
    buttonSignin = tk.Button(subFrame, image=signinImg1, padx=0, pady=0, borderwidth=0, highlightthickness=0, bd=0,
                             relief="flat")
    buttonSignin.bind("<Enter>", lambda e: enter(e, buttonSignin))
    buttonSignin.bind("<Leave>", lambda e: leave(e, buttonSignin))
    buttonSignin.pack(side="top")

    buttonSignup = tk.Button(subFrame, text="Sign up")
    buttonSignup.pack()

    mainFrame.tkraise()

    # Keeps the GUI running
    root.mainloop()


def initLoginFrame():
    signinFrame = tk.Frame(root, bg="blue")
    signinFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    button = tk.Button(signinFrame, text="Login")
    button.pack()

    label = tk.Label(signinFrame, text="AAAAA", bg="yellow", font={"arial", 16})
    label.pack()

    entry = tk.Entry(signinFrame, bg="green")
    entry.pack()
