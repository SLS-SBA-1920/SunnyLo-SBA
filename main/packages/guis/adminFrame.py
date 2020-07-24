import tkinter as tk
from packages.gui import getAppFrame, getCreateUserFrame
from packages.guis.editUserFrame import *
from data import storage

appFrame = None
usersCanvas = None


def initAdminFrame(root):
    global appFrame
    appFrame = tk.Frame(root)
    appFrame.grid_columnconfigure(0, weight=1)
    appFrame.grid_columnconfigure(1, weight=1)
    appFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    backImg = tk.PhotoImage(file="../sources/buttons/back-button.png")
    backBtn = tk.Button(appFrame, height=64, width=64, image=backImg, padx=0, pady=0, borderwidth=0,
                        highlightthickness=0, bd=0,
                        relief="flat", command=lambda: getAppFrame().tkraise())
    backBtn["image"] = backImg
    backBtn.image = backImg
    backBtn.grid(row=0, column=0, sticky="nw")

    createUserBtn = tk.Button(appFrame, text="Create User", padx=0, pady=0, borderwidth=0,
                              highlightthickness=0, bd=0,
                              relief="flat", command=lambda: getCreateUserFrame().tkraise())
    createUserBtn.grid(row=0, column=1, sticky="e", padx=10)
    loadUsers()
    return appFrame


def loadUsers():
    global appFrame, usersCanvas
    if not usersCanvas == None:
        usersCanvas.destroy()
    usersCanvas = tk.Canvas(appFrame)
    usersCanvas.grid(row=1, column=0, columnspan=2, sticky="we", padx=10, pady=20)
    frame = tk.Frame(usersCanvas)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.pack()
    tk.Label(frame, text="ID").grid(row=0, column=0, padx=20)
    tk.Label(frame, text="Username").grid(row=0, column=1, padx=20)
    tk.Label(frame, text="Admin").grid(row=0, column=2, padx=20)
    tk.Label(frame, text="Action").grid(row=0, column=3, columnspan=2, padx=20)
    i = 2

    if not storage.getContent("users") == None:
        for user in storage.getContent("users"):
            tk.Label(frame, text=(i - 1)).grid(row=i, column=0)
            tk.Label(frame, text=user.get("username")).grid(row=i, column=1)
            tk.Label(frame, text="✅" if user.get("admin") else "❌").grid(row=i, column=2)
            tk.Button(frame, text="✏️", command=lambda i=i: editUser(i - 2)).grid(row=i, column=3)
            tk.Button(frame, text="🗑️", command=lambda user=user: deleteUser(user)).grid(row=i, column=4)
            i = i + 1


def deleteUser(element):
    MsgBox = tk.messagebox.askquestion('Delete User',
                                       'Are you sure you want to delete the user\n' + element.get("username"),
                                       icon='warning')
    if MsgBox == 'yes':
        storage.getContent('users').remove(element)
        storage.save()
        loadUsers()
