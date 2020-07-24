import tkinter as tk


def initMainFrame(root, signinFrame):
    # Add white area on top of the white background
    mainFrame = tk.Frame(root)
    mainFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    # Centres all the elements in the frame
    subFrame = tk.Frame(mainFrame)
    subFrame.place(relx=0.5, rely=0.5, anchor="center")

    def updateImg(e, btn, imgPath):
        img = tk.PhotoImage(file=imgPath)
        btn["image"] = img
        btn.image = img

    signinImg = tk.PhotoImage(file="../sources/buttons/login-01.png")
    buttonSignin = tk.Button(subFrame, image=signinImg, padx=0, pady=0, borderwidth=0, highlightthickness=0, bd=0,
                             relief="flat", command=lambda: liftFrame(signinFrame))
    buttonSignin.config(image=signinImg)
    buttonSignin.image = signinImg
    buttonSignin["image"] = signinImg
    buttonSignin.bind("<Enter>", lambda e: updateImg(e, buttonSignin, "../sources/buttons/login-02.png"))
    buttonSignin.bind("<Leave>", lambda e: updateImg(e, buttonSignin, "../sources/buttons/login-01.png"))
    buttonSignin.pack(pady=10)

    closeImg = tk.PhotoImage(file="../sources/buttons/close-01.png")
    buttonClose = tk.Button(subFrame, image=closeImg, padx=0, pady=0, borderwidth=0, highlightthickness=0, bd=0,
                            relief="flat", command=lambda: root.quit())
    buttonClose.config(image=closeImg)
    buttonClose.image = closeImg
    buttonClose["image"] = closeImg
    buttonClose.bind("<Enter>", lambda e: updateImg(e, buttonClose, "../sources/buttons/close-02.png"))
    buttonClose.bind("<Leave>", lambda e: updateImg(e, buttonClose, "../sources/buttons/close-01.png"))
    buttonClose.pack(pady=10)

    mainFrame.tkraise()

    return mainFrame


def liftFrame(frame):
    frame.tkraise()
