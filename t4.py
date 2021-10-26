from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("Icon Creating")
root.iconbitmap("C:/Users/mayan/Downloads/datasets/icon1.ico")

myImg = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/Wallpaper/s1.jpg"))
myImg1 = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/Wallpaper/s2.jpg"))
myImg3 = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/Wallpaper/s4.jpg"))
myImg4 = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/Wallpaper/s5.jpg"))
myImg5 = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/Wallpaper/s6.jpg"))
image_list = [myImg, myImg1, myImg3, myImg4, myImg5]

my_label = Label(image=myImg)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_num - 1])
    button_forward = Button(root, text='>', command=lambda: forward(image_num + 1))
    button_back = Button(root, text='<', command=lambda: back(image_num - 1))
    if image_num == 5:
        button_forward = Button(root, text='>', state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text='Image ' + str(image_num) + ' Of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_num):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_num - 1])
    button_forward = Button(root, text='>', command=lambda: forward(image_num + 1))
    button_back = Button(root, text='<', command=lambda: back(image_num - 1))
    if image_num == 1:
        button_back = Button(root, text='<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text='Image ' + str(image_num) + ' Of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


status = Label(root, text='Image 1 Of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
button_back = Button(root, text='<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit', command=root.quit)
button_forward = Button(root, text='>', command=lambda: forward(2))
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
