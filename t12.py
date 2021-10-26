from tkinter import * 
import PIL
from PIL import Image
from PIL import ImageTk
root=Tk()
root.title('Dropmenus')
root.iconbitmap('C:/Users/mayan/Downloads/datasets/icon1.ico')
root.geometry('400x400')
options=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
clicked=StringVar()
clicked.set(options[0])
drop=OptionMenu(root,clicked,*options)
drop.pack()
def show():
    myLabel=Label(root,text=clicked.get())
    myLabel.pack()
myButton=Button(root,text='Show Selection',command=show)
myButton.pack()

root.mainloop()