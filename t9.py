from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Dialog Box")
root.iconbitmap("C:/Users/mayan/Downloads/datasets/icon1.ico")

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='C:/Users/mayan/Downloads', title='Select a File', filetypes=(
    ('png files', '*.png'), ('jpeg', '*.jpeg'), ('all files', '*.*')))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    image_label = Label(root, image=my_image).pack()


my_button  = Button(root, text='Open File ', command=open).pack()
root.mainloop()
