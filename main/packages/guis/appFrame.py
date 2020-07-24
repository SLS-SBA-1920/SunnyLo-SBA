import tkinter as tk


def initAppFrame(root):
    appFrame = tk.Frame(root)
    appFrame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    # Centres all the elements in the frame
    subFrame = tk.Frame(appFrame)
    subFrame.place(relx=0.5, rely=0.5, anchor="center")

    label = tk.Label(subFrame, text="There is currently\nnothing in the app")
    label.pack()

    return appFrame


def liftFrame(frame):
    frame.tkraise()
