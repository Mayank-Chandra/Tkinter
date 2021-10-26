from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("MyProject")
root.iconbitmap("C:/Users/mayan/Downloads/datasets/backiee_89586_a82_icon.ico")

frame1 = LabelFrame(root, padx=50, pady=50)
frame1.pack(padx=10, pady=10)
b1 = Button(frame1, text='Dont Click HERE!!!!!')
b2 = Button(frame1, text='Dont Click HERE!!!!! OR HERE!!!!!!!!!')
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)







root.mainloop()
