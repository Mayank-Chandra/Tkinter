from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
from tkinter import filedialog


root = Tk()
root.title('CheckBox')
root.iconbitmap("C:/Users/mayan/Downloads/datasets/icon1.ico")
root.geometry('400x400')
var = StringVar()
def show():
    myLabel = Label(root, text=var.get()).pack()

checkbox = Checkbutton(root, text='Check ME OUT!!', variable=var, onvalue='YaY', offvalue='WoW')
checkbox.deselect()

mybutton = Button(root, text='Show yourself', command=show).pack()
checkbox.pack()


root.mainloop()