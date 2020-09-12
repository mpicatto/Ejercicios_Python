# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:39:58 2019

@author: Mauro
"""

import sqlite3

def create():
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS bookStore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER) ")
    conn.commit()
    conn.close

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO bookStore VALUES(NULL,?, ?, ?, ?)",(title,author,year,isbn))
    conn.commit()
    conn.close
    
def view():
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM bookStore")
    rows=cursor.fetchall()
    conn.close()
    return rows    

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM bookStore WHERE  title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cursor.fetchall()
    conn.close
    return rows 
    
def delete (id):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM bookStore WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("UPDATE bookStore SET  title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
    conn.commit()
    conn.close()  
    

create()
#insert("La Bella y la Bestia","Karl Disney",1948,4654643511315)
#delete(3)
#print(search(title="El Capital"))
#◘update(1,'El Capital','Karl Marx',1856,45454564446)
#print(view())