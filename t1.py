from tkinter import *
root = Tk()
myLabel = Label(root, text="Hello World!!")
myLabel1 = Label(root, text="My Name Is Mayank ")

myLabel.grid(row=0, column=0)
myLabel1.grid(row=1, column=5)

root.mainloop()
