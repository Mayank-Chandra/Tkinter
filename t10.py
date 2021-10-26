from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('Sliders')
root.iconbitmap("C:/Users/mayan/Downloads/datasets/icon1.ico")
root.geometry('400x400')
vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide(var):
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x400')

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()
def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + 'x' + str(vertical.get()))
my_button = Button(root, text='Click Me!', command=slide).pack()

root.mainloop()