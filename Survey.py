from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox

root = Tk()
root.title("National Survey Of India")
root.iconbitmap("C:/Users/mayan/Downloads/datasets/indexicon.ico")
root.geometry("1920x1080")
root.config(background='Skyblue')


def clear():
    entry_name.delete(0, END)
    entry_adhaar.delete(0, END)
    entry_num.delete(0, END)
    entry_addresscurr.delete(0, END)
    entry_addresscurr2.delete(0, END)
    entry_addresscurr3.delete(0, END)

def copy():
    add1 = entry_addresscurr.get()
    add2 = entry_addresscurr2.get()
    add3 = entry_addresscurr3.get()
    entry_addressper = Label(root, text=add1, bg='Skyblue')
    entry_addressper2 = Label(root, text=add2, bg='Skyblue')
    entry_addressper3 = Label(root, text=add3, bg='Skyblue')

    entry_addressper.grid(row=15, column=16, sticky=W)
    entry_addressper2.grid(row=20, column=16, sticky=W)
    entry_addressper3.grid(row=25, column=16, sticky=W)


Img = ImageTk.PhotoImage(Image.open("C:/Users/mayan/Downloads/datasets/index.jpg"))
Img_label = Label(root, image=Img).grid(row=0, column=0, sticky=E)
heading_label = Label(root, text='GENERAL SURVEY OF INDIA', fg='Orange', anchor=E, bg='Skyblue')
heading_label2 = Label(root, text='Ministry Of Home Affairs and Welfare', fg='Orange', anchor=E, bg='Skyblue')
heading_label3 = Label(root, text='Government Of India', fg='Green', anchor=E, bg='Skyblue')
name_label = Label(root, text='Enter Your Full Name : ', bg='Skyblue')
address_label = Label(root, text="Enter Your Address : ", bg='Skyblue')
addper_label = Label(root, text='Permanent Address :', bg='Skyblue')
addcur_label = Label(root, text='Current Address ', bg='Skyblue')
number_label = Label(root, text='Phone Number :', bg='Skyblue')
entry_num = Entry(root)
entry_name = Entry(root)
entry_addresscurr = Entry(root)
entry_addresscurr2 = Entry(root)
entry_addresscurr3 = Entry(root)
entry_name.get()
entry_num.get()
entry_addresscurr.get()
entry_addresscurr2.get()
entry_addresscurr3.get()
# entry_adhaar.get()
# entry_addressper = Entry(root)
# entry_addressper2 = Entry(root)
# entry_addressper3 = Entry(root)
copy_button = Button(root, text='Same As Current Address? ', command=copy)
survey_label = Label(root, text='Vaccination Survey', font=('Arial', 30), bg='Skyblue')
heading_label4 = Label(root, text="COWIN", font=('Comic Sans MS', 30), fg='Blue', bg='Skyblue')
q1_label = Label(root, text='1) Which Vaccine Did you take? ', bg='Skyblue', font=24)
adhaar_label = Label(root, text='Adhaar Number : ', bg='Skyblue')
entry_adhaar = Entry(root)
clear_button = Button(root, text='Clear', command=clear)
entry_adhaar.get()
def display(var):
    top = Toplevel()
    def close():
        response = messagebox.askyesno("Close Window", "Do you want to close")
        label_response = Label(top, text=response).pack()
        if response == 1:
            top.destroy()
        else:
            pass

    name_str = 'Name :' + entry_name.get()
    num_str = 'Number :' + entry_num.get()
    num_add1 = 'Address :' + entry_addresscurr.get()
    num_add2 = entry_addresscurr2.get()
    num_add3 = entry_addresscurr3.get()
    add_str = 'Adhaar :' + entry_adhaar.get()
    name_str = Label(top, text=name_str).pack()
    num_str = Label(top, text=num_str).pack()
    num_add1 = Label(top, text=num_add1).pack()
    num_add2 = Label(top, text=num_add2).pack()
    num_add3 = Label(top, text=num_add3).pack()
    add_str = Label(top, text=add_str).pack()
    q1_label = Label(top, text='1) Which Vaccine Did you take? ').pack()
    Radiobutton(top, text='Covaxin', variable=vaccine, state=DISABLED, value=type1,
                command=lambda: display(vaccine.get())).pack()
    Radiobutton(top, text='CoviShield', variable=vaccine, state=DISABLED, value=type2,
                command=lambda: display(vaccine.get())).pack()
    q2_label = Label(top, text='2) Did you took both doses of vaccine? ').pack()
    Radiobutton(top, text='Yes', variable=ans, value=yes, state=DISABLED, command=lambda: display(ans.get())).pack()
    Radiobutton(top, text='No', variable=ans, value=no, state=DISABLED, command=lambda: display(ans.get())).pack()
    close_button = Button(top, text='Close', command=close).pack()

# vaccine_list = [('Covaxin', 'Covaxin'),
# ('CoviShield', 'CoviShield')]
vaccine = StringVar()
type1 = 'Covaxin'
type2 = 'CoviShield'
ans = StringVar()
yes = 'Yes'
no = 'No'
vaccine.set('NaN')
ans.set('yes')

# for vacname, type in vaccine_list:
# Radiobutton(root, text=vacname, variable=vaccine, value=type, font=18, bg='Skyblue').grid(row=37, column=7)

Radiobutton(root, text='Covaxin', variable=vaccine, value=type1, bg='Skyblue', font=18, command=lambda: display(vaccine.get())).grid(row=37, column=7)
Radiobutton(root, text='CoviShield', variable=vaccine, value=type2, bg='Skyblue', font=18, command=lambda: display(vaccine.get())).grid(row=37, column=8)
q2_label = Label(root, text='2) Did you took both doses of vaccine? ', bg='SkyBlue', font=24)
Radiobutton(root, text='Yes', variable=ans, value=yes, bg="SkyBlue", font=18, command=lambda: display(ans.get())).grid(row=39, column=7)
Radiobutton(root, text='No', variable=ans, value=no, bg="SkyBlue", font=18, command=lambda: display(ans.get())).grid(row=39, column=8)
new_window = Button(root, text='See Details', command=display)

new_window.grid(row=42, column=8)
clear_button.grid(row=40, column=8)
entry_adhaar.grid(row=33, column=8, padx=10, ipadx=100)
q2_label.grid(row=38, column=7)
adhaar_label.grid(row=33, column=7)
q1_label.grid(row=36, column=7)
heading_label4.grid(row=0, column=8)
survey_label.grid(row=35, column=7)
number_label.grid(row=32, column=7)
entry_num.grid(row=32, column=8, padx=10, ipadx=100)
copy_button.grid(row=30, column=8)
addcur_label.grid(row=10, column=8)
addper_label.grid(row=10, column=16)
entry_addresscurr.grid(row=15, column=8, padx=10, ipadx=100)
entry_addresscurr2.grid(row=20, column=8, padx=10, ipadx=100)
entry_addresscurr3.grid(row=25, column=8, padx=10, ipadx=100)
# entry_addressper.grid(row=15, column=16, padx=10, ipadx=100)
# entry_addressper2.grid(row=20, column=16, padx=10, ipadx=100)
# entry_addressper3.grid(row=25, column=16, padx=10, ipadx=100)
address_label.grid(row=10, column=7)
entry_name.grid(row=6, column=8, padx=10, columnspan=3, ipadx=100)
name_label.grid(row=6, column=7)
heading_label.grid(row=1, column=0, columnspan=2)
heading_label2.grid(row=2, column=0, columnspan=2)
heading_label3.grid(row=3, column=0, columnspan=2)
root.mainloop()
