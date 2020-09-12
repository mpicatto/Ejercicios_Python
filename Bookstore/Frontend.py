# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:13:23 2019

@author: Mauro
"""
from tkinter import *
import Backend as backend

def view_comm():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_comm():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_num.get(), isbn_num.get()):
        list1.insert(END,row)
        
def add_entry():
    backend.insert(title_text.get(), author_text.get(), year_num.get(), isbn_num.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(), author_text.get(), year_num.get(), isbn_num.get() ))    

def get_select(event):
    try:
        global selectedentry
        index=list1.curselection()[0]
        selectedentry=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selectedentry[1])
        e2.delete(0,END)
        e2.insert(END,selectedentry[2])
        e3.delete(0,END)
        e3.insert(END,selectedentry[3])
        e4.delete(0,END)
        e4.insert(END,selectedentry[4])
    except IndexError:
        pass
    
def delete_entry():
    backend.delete(selectedentry[0])
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
  
def update_entry():
    backend.update(selectedentry[0],title_text.get(), author_text.get(), year_num.get(), isbn_num.get())
    list1.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_num.get(), isbn_num.get()):
        list1.insert(END,row)

   
    

window=Tk()
window.wm_title("Bookstore DataBase")

l1=Label(window, text="Title")
l1.grid(row=0, column=0)
l2=Label(window, text="Author")
l2.grid(row=0, column=2)
l3=Label(window, text="Year")
l3.grid(row=1, column=0)
l4=Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0, column=1)
author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0, column=3)
year_num=StringVar()
e3=Entry(window,textvariable=year_num)
e3.grid(row=1, column=1)
isbn_num=StringVar()
e4=Entry(window,textvariable=isbn_num)
e4.grid(row=1, column=3)

list1=Listbox(window, height=8, width=40)
list1.grid(row=2, column=0, rowspan=8, columnspan=2,)
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=8)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_select)

b1=Button(window,text="View all", width=12,command=view_comm)
b1.grid(row=2, column=3)
b2=Button(window,text="Search entry", width=12,command=search_comm)
b2.grid(row=3, column=3)
b3=Button(window,text="Add entry", width=12, command=add_entry)
b3.grid(row=4, column=3)
b4=Button(window,text="Update Selected", width=12, command=update_entry)
b4.grid(row=5, column=3)
b5=Button(window,text="Delete Selected", width=12, command=delete_entry)
b5.grid(row=6, column=3)
b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()



