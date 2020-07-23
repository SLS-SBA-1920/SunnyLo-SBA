import tkinter as tk
import bcrypt
import base64
import hashlib
from packages.gui import getMainFrame
from data import storage

changingColor = False


def initLoginFrame(root):
    signinFrame = tk.Frame(root, bg="blue")
    signinFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    backImg = tk.PhotoImage(file="../sources/buttons/back-button.png")
    backBtn = tk.Button(signinFrame, height=64, width=64, image=backImg, padx=0, pady=0, borderwidth=0,
                        highlightthickness=0, bd=0,
                        relief="flat", command=lambda: liftFrame(getMainFrame()))
    backBtn["image"] = backImg
    backBtn.image = backImg
    backBtn.place(relx=0.0, rely=0.0, anchor="nw")

    # Centres all the elements in the frame
    subFrame = tk.Frame(signinFrame)
    subFrame.place(relx=0.5, rely=0.5, anchor="center")

    def login(*args, **kwargs):
        labelError.config(text="Loggining...")
        if username.get() == "":
            labelError.config(text="Please fill in your username")
            usernameEntry.focus()
            changeColor(usernameEntry, 0, 5)
            return False
        if password.get() == "":
            labelError.config(text="Please fill in your password")
            passwordEntry.focus()
            changeColor(passwordEntry, 0, 5)
            return False

        users = storage.getContent("users")
        for userData in users:
            if userData["username"] == username.get():
                passwd = base64.b64encode(hashlib.sha256(password.get().encode('utf-8')).digest())
                if bcrypt.checkpw(passwd, userData["password"].encode('utf-8')):
                    labelError.config(text="Correct")
                    return True
                else:
                    break
        labelError.config(text="Invalid username and password")

    def _from_rgb(rgb):
        return "#%02x%02x%02x" % rgb

    def changeColor(entry, color, change):
        global changingColor
        if (color == 0 and not changingColor) or not color == 0:
            if color + change == 255:
                changingColor = False
                return False
            changingColor = True
            entry.config(background=_from_rgb((255, color + change, color + change)))
            root.after(4, lambda: changeColor(entry, color + change, change))

    def removeError(*args):
        labelError.config(text="")

    signinLabel = tk.Label(subFrame, text="Login", font=("", 50, "bold"))
    signinLabel.pack()

    username = tk.StringVar()
    usernameLabel = tk.Label(subFrame, text="Username:")
    usernameLabel.pack(pady=(0, 10))
    usernameEntry = tk.Entry(subFrame, textvariable=username)
    usernameEntry.pack()
    usernameEntry.bind("<Tab>", lambda e: passwordEntry.focus())
    usernameEntry.bind('<Return>', login)
    username.trace_add("write", removeError)

    def nextFocus(e):
        usernameEntry.focus()
        return ("break")

    password = tk.StringVar()
    passwordLabel = tk.Label(subFrame, text="Password:")
    passwordLabel.pack(pady=(50, 10))
    passwordEntry = tk.Entry(subFrame, show="*", textvariable=password)
    passwordEntry.pack()
    passwordEntry.bind("<Tab>", nextFocus)
    passwordEntry.bind('<Return>', login)
    password.trace_add("write", removeError)

    loginBtn = tk.Button(subFrame, text="Login", command=login)
    loginBtn.pack(pady=(50, 0))

    labelError = tk.Label(subFrame, text="")
    labelError.pack()

    return signinFrame


def liftFrame(frame):
    frame.tkraise()
