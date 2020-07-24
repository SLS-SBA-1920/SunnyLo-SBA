import tkinter as tk
import bcrypt
import base64
import hashlib
from packages.gui import getAdminFrame
from data import storage
from data import config

changingColor = False

index = None
editUserFrame = None
username = None
admin = None


def initEditUserFrame(root):
    global editUserFrame, username, admin, index
    editUserFrame = tk.Frame(root)
    editUserFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    backImg = tk.PhotoImage(file="../sources/buttons/back-button.png")
    backBtn = tk.Button(editUserFrame, height=64, width=64, image=backImg, padx=0, pady=0, borderwidth=0,
                        highlightthickness=0, bd=0,
                        relief="flat", command=lambda: getAdminFrame().tkraise())
    backBtn["image"] = backImg
    backBtn.image = backImg
    backBtn.place(relx=0.0, rely=0.0, anchor="nw")

    # Centres all the elements in the frame
    subFrame = tk.Frame(editUserFrame)
    subFrame.place(relx=0.5, rely=0.5, anchor="center")

    def login(*args, **kwargs):
        if username.get() == "":
            labelError.config(text="Please fill in your username")
            usernameEntry.focus()
            changeColor(usernameEntry, 0, 5)
            return False
        passwd = None
        if password.get() == "":
            passwd = storage.getContent("users")[index].get("password")
        else:
            passwd = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password.get().encode('utf-8')).digest()),
                                   bcrypt.gensalt(rounds=config.getContent("PasswordEncryptionSecurityLevel"))).decode(
                "utf-8")
        storage.getContent("users")[index] = {"username": username.get(), "password": passwd,
                                              "admin": admin.get() == 1}
        storage.save()
        username.set("")
        password.set("")
        admin.set(0)
        labelError.config(text="")
        from packages.guis.adminFrame import loadUsers
        loadUsers()
        getAdminFrame().tkraise()

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

    tk.Label(subFrame, text="Edit User", font=("", 50, "bold")).pack()

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
    passwordLabel = tk.Label(subFrame, text="Password (Leave blank to keep\nthis user's password the same):")
    passwordLabel.pack(pady=(50, 10))
    passwordEntry = tk.Entry(subFrame, show="*", textvariable=password)
    passwordEntry.pack()
    passwordEntry.bind("<Tab>", nextFocus)
    passwordEntry.bind('<Return>', login)

    admin = tk.IntVar()
    adminCheckBtn = tk.Checkbutton(subFrame, text="Administrator", variable=admin, onvalue=1, offvalue=0)
    adminCheckBtn.pack()

    loginBtn = tk.Button(subFrame, text="Edit", command=login)
    loginBtn.pack(pady=(50, 0))

    labelError = tk.Label(subFrame, text="")
    labelError.pack()


def editUser(i):
    global username, admin, index
    user = storage.getContent("users")[i]
    username.set(user.get("username"))
    admin.set(1 if user.get("admin") else 0)
    editUserFrame.tkraise()
    index = i
