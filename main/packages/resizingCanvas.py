from tkinter import *

from PIL import Image, ImageTk


class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)

        self.image = Image.open("../sources/bg.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image.resize((1280, 720), Image.ANTIALIAS))

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill="both", expand=True)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):

        if self.changeSize is None:
            self.changeSize = event.height - 720
        new_width = event.width - self.changeSize
        new_height = event.height - self.changeSize

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)
