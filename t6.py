from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title("RadioButton")
root.iconbitmap("C:/Users/mayan/Downloads/datasets/icon1.ico")


# a = IntVar()
# a.set("2")


def click(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


modes = [
    ("Paneer", "Paneer"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]
pizza = StringVar()
pizza.set("paneer")
for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


# Radiobutton(root, text='Option1', variable=a, value=1, command=lambda: click(a.get())).pack()
# Radiobutton(root, text='Option2', variable=a, value=2, command=lambda: click(a.get())).pack()
# Radiobutton(root, text='Option3', variable=a, value=3, command=lambda: click(a.get())).pack()
# Radiobutton(root, text='Option4', variable=a, value=4, command=lambda: click(a.get())).pack()
#myLabel = Label(root, text=pizza.get())
#myLabel.pack()
mybutton = Button(root, text='Click ME', command=lambda: click(pizza.get()))
mybutton.pack()
root.mainloop()
