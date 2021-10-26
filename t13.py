from tkinter import *
import PIL
from PIL import Image
from PIL import ImageTk
import sqlite3
root=Tk()
root.title('Databases')
root.iconbitmap('C:/Users/mayan/Downloads/datasets/icon1.ico')
root.geometry('400x400')
#Databasse Creation
data=sqlite3.connect('address_book.db')
#Curser Creation
c=data.cursor()
#Create Table
c.execute(''''CREATE TABLE addresses(first_name text, last_name text, addresses text,city text, country text,zipcode integers)'''')
  
#Commit Changes
data.commit()
#Database Close
data.close()

root.mainloop()