from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.iconbitmap('C:/Users/mayan/Downloads/datasets/icon1.ico')


def popup():
    response = messagebox.showinfo("This is My popup", 'Hello World')
    label = Label(root, text=response).pack()


    #if response == 'yes':
        #label = Label(root, text='You Clicked YES!!').pack()
    #else:
        #label = Label(root, text='You Clicked NO!!').pack()


Button(root, text='Pop Up', command=popup).pack()

root.mainloop()
