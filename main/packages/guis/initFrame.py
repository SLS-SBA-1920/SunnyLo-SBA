import tkinter as tk
import bcrypt
import base64
import hashlib
from packages.gui import getMainFrame
from data import storage

changingColor = False


def initInitFrame(root):
    initFrame = tk.Frame(root, bg="blue")
    initFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    # Centres all the elements in the frame
    subFrame = tk.Frame(initFrame)
    subFrame.place(relx=0.5, rely=0.5, anchor="center")

    def login(*args, **kwargs):
        labelError.config(text="Creating user...")
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

        passwd = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password.get().encode('utf-8')).digest()),
                               bcrypt.gensalt())
        storage.addContent("users", {"username": username.get(), "password": passwd.decode("utf-8"), "admin": True})
        root.focus()
        password.set("")
        usernameEntry.config(state="disabled")
        passwordEntry.config(state="disabled")
        loginBtn.config(state="disabled")
        labelError.config(text="Success. You'll be redirected to the main page in a second")
        root.after(1000, lambda: labelError.config(text=labelError.cget("text") + "."))
        root.after(2000, lambda: labelError.config(text=labelError.cget("text") + "."))
        root.after(3000, lambda: labelError.config(text=labelError.cget("text") + "."))
        root.after(4000, lambda: labelError.config(text=labelError.cget("text") + "."))
        root.after(5000, lambda: getMainFrame().tkraise())

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

    signinLabel = tk.Label(subFrame, text="To start, please setup an administrative user", font=("", 50, "bold"))
    signinLabel.pack()

    username = tk.StringVar()
    usernameLabel = tk.Label(subFrame, text="Username:")
    usernameLabel.pack(pady=(0, 10))
    usernameEntry = tk.Entry(subFrame, textvariable=username)
    usernameEntry.pack()
    usernameEntry.bind("<Tab>", lambda e: passwordEntry.focus())
    usernameEntry.bind('<Return>', login)

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

    loginBtn = tk.Button(subFrame, text="Create User", command=login)
    loginBtn.pack(pady=(50, 0))

    labelError = tk.Label(subFrame, text="")
    labelError.pack()

    initFrame.tkraise()

    return initFrame


def liftFrame(frame):
    frame.tkraise()
