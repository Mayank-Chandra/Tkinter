from tkinter import *
import PIL 
from PIL import Image
from PIL import ImageTk
import sqlite3
root=Tk()
root.title('Database')
root.iconbitmap('F:/python/datasets/icon1.ico')
root.geometry('400x400')
#Create or Connect Database
# Create Submit

conn=sqlite3.connect('address_book.db')
#Create Cursor
c=conn.cursor()
#Commit Change
#c.execute('CREATE TABLE addresses(first_name text,last_name text,address text,city text,state text,zipcode integers)')

conn.commit()
#Close 
conn.close()
#Create Table

def submit():
    conn=sqlite3.connect('address_book.db')
    #Create Cursor
    c=conn.cursor()
   
    #Create Table
    c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
    {
        'f_name':first_name.get(),
        'l_name':last_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zip.get()
    })

    conn.commit()
    #Close 
    conn.close()

    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zip.delete(0,END)

def query():
    conn=sqlite3.connect('address_book.db')
    #Create Cursor
    c=conn.cursor()
    #query the database
    c.execute('SELECT *,oid FROM addresses')
    rec=c.fetchall()
   # print(rec)
    print_records=''
    for record in rec:
        print_records+= str(record) + '\n'
        query_label=Label(root,text=print_records)
        query_label.grid(row=8,column=0,columnspan=2)
    conn.commit()
    #Close 
    conn.close()


#Create text books
first_name=Entry(root,width=30)
first_name.grid(row=0,column=1,padx=20)

last_name=Entry(root,width=30)
last_name.grid(row=1,column=1,padx=20)

address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)

city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)

state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)

zip=Entry(root,width=30)
zip.grid(row=5,column=1,padx=20)

#Create text box label

first_name_label=Label(root,text='First Name')
first_name_label.grid(row=0,column=0)

last_name_label=Label(root,text='Last Name')
last_name_label.grid(row=1,column=0)

address_label=Label(root,text='Address')
address_label.grid(row=2,column=0)

city_label=Label(root,text='City')
city_label.grid(row=3,column=0)

state_label=Label(root,text='State')
state_label.grid(row=4,column=0)

zip_label=Label(root,text='Zip Code')
zip_label.grid(row=5,column=0)

#Create Submit Button
submit_button=Button(root,text='Add Record to Database',command=submit)
submit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#Create a query button
query_b=Button(root,text='Show Records',command=query)
query_b.grid(row=7,column=0,columnspan=2,padx=10,pady=10,ipadx=137)

root.mainloop()