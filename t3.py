from tkinter import *

root = Tk()
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter your Name")


def myclick():
    hello = "Hello "+e.get()
    mylabel1 = Label(root, text=hello)
    mylabel1.pack()


mybutton = Button(root, text="Enter your Name", command=myclick)
mybutton.pack()
root.mainloop()
