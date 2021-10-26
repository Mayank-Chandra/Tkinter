from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
from sklearn import neighbors
import matplotlib.pyplot as plt
root=Tk()
root.title('NotePad')
root.geometry("1600x900")
root.config(background='SkyBlue')
root.iconbitmap("F:/python/datasets/icon1.ico")
Label_heading=Label(root,text='Notepad',bg='SkyBlue',font=('Nanum Pen Script',24))
Label_Frame1=LabelFrame(root,padx=50,pady=50)
Entry_note=Entry(Label_Frame1)
def show():
    shownotes=Entry_note.get()
    label_show=Label(root,text=shownotes,bg='SkyBlue')
    label_show.grid(row=4,column=3)



Label_Frame1.grid(row=2, column=3,padx=10,pady=10)
Label_heading.grid(row=0,column=1)
Entry_note.grid(row=0,column=0,ipadx=100,ipady=100)
show_button=Button(root,text='Show Notes',command=show)
show_button.grid(row=3,column=3)
root.mainloop()

