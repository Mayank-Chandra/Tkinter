from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("SRM IST Database")
root.iconbitmap("C:/Users/mayan/Downloads/datasets/srm.ico")
Img = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/srm1.png"))
Img1 = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/srm1.png"))
Img2 = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/srm2.png"))
Img3 = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/srm3.png"))
Img_list = [Img1, Img2, Img3]
logo = Label(root, image=Img1)
logo.grid(row=0, column=0)


def forward(img_num):
    global button_forward
    global button_backward
    global img
    img.grid_forget()
    img = Label(frame2, image=Img_list[img_num-1])
    button_forward = Button(frame2, text='->', command=lambda:forward(img_num+1))
    button_backward = Button(frame2, text='<-', command=lambda:backward(img_num-1))
    if img_num == 3:
        button_forward = Button(frame2, text='->', state=DISABLED)
    button_forward.grid(row=1, column=3)
    button_backward.grid(row=1, column=0)
    img.grid(row=0, column=1)

def backward(img_num):
    global button_forward
    global button_backward
    global img
    img.grid_forget()
    img = Label(frame2, image=Img_list[img_num-1])
    button_forward = Button(frame2, text='->', command=lambda:forward(img_num+1))
    button_backward = Button(frame2, text='<-', command=lambda:backward(img_num-1))
    if img_num == 1:
        button_backward = Button(frame2, text='<-', state=DISABLED)
    button_forward.grid(row=1, column=3)
    button_backward.grid(row=1, column=0)
    img.grid(row=0, column=1)



def display():
    str1 = 'Your Name:' + entry1.get()
    str2 = 'Your Registration Number:' + entry2.get()
    str3 = 'Email Address:' + entry3.get()
    label4 = Label(root, text=str1)
    label5 = Label(root, text=str2)
    label6 = Label(root, text=str3)
    label4.grid(row=6, column=2)
    label5.grid(row=7, column=2)
    label6.grid(row=8, column=2)


def clearall():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)


Label1 = Label(root, text='SRM Institute Of Science And Technology '
                          'Delhi- Meerut Road, Modinagar, Ghaziabad, Uttar Pradesh 201204')
Label1.grid(row=0, column=3)
entry1 = Entry(root)
Label2 = Label(root, text='Student Name:')
Label3 = Label(root, text='Registration Number:')
label4a = Label(root, text='Email ID:')
label4a.grid(row=5, column=2)
entry3 = Entry(root)
entry3.get()
button1 = Button(root, text='Display Credentials', command=display)
button1.grid(row=7, column=3)
Label3.grid(row=4, column=2)
entry2 = Entry(root)
Label2.grid(row=3, column=2)
entry1.grid(row=3, column=4, columnspan=4, ipadx=50)
entry2.grid(row=4, column=4, columnspan=4, ipadx=50)
entry3.grid(row=5, column=4, columnspan=4, ipadx=50)
frame1 = LabelFrame(root, text='Click Here to Clear Entries ', padx=10, pady=10)
frame2 = LabelFrame(root, padx=10, pady=10)
frame2.grid(row=1, column=0, padx=10, pady=10)
b1 = Button(frame1, text='Clear Entries', command=clearall)
frame1.grid(row=1, column=6, padx=10, pady=10)
b1.pack()
button_forward = Button(frame2, text='->', command=lambda: forward(1))
button_backward = Button(frame2, text='<-', command=backward, state=DISABLED)
img = Label(frame2, image=Img1)
button_backward.grid(row=1, column=0)
button_forward.grid(row=1, column=3)
root.mainloop()
