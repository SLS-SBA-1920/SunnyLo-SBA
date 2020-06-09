import tkinter as tk


def startGUI():
    window = tk.Tk()
    window.title("St. Louis School ICT SBA by SunnyLo")

    canvas = tk.Canvas(window, height=600, width=400)
    canvas.pack()

    frame = tk.Frame(window, bg="blue")
    frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)

    button = tk.Button(frame, text="Login")
    button.pack()

    label = tk.Label(frame, text="Click a button to get started", bg="yellow")
    label.pack()

    entry = tk.Entry(frame, bg="green")
    entry.pack()

    frame.destroy()
    frame.place()

    window.mainloop()
