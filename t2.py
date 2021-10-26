from tkinter import *

root = Tk()


def click():
    myLabel = Label(root, text="Look I Clicked the button")
    myLabel.pack()


myButton = Button(root, text="Click ME!!", command=click, bg='blue', fg='white')
myButton.pack()
root.mainloop()
