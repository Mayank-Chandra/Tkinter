from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox

root = Tk()
root.title("New Windows")
root.iconbitmap("C:/Users/mayan/Downloads/datasets/icon1.ico")


def open():
    global img
    top = Toplevel()
    img = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/srm1.png"))
    img = Label(top, image=img).pack()
    b2 = Button(top, text='Close Windows', command=top.destroy).pack()


b1 = Button(root, text='Open Second Windows', command=open).pack()

root.mainloop()
