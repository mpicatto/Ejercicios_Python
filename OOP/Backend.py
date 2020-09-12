# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:39:58 2019

@author: Mauro
"""

import sqlite3
class database:
    def __init__(self):
        self.conn=sqlite3.connect("books.db")
        self.cursor=self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bookStore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER) ")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cursor.execute("INSERT INTO bookStore VALUES(NULL,?, ?, ?, ?)",(title,author,year,isbn))
        self.conn.commit()
        self.conn.close

    def view(self):
        self.cursor.execute("SELECT * FROM bookStore")
        rows=self.cursor.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.cursor.execute("SELECT * FROM bookStore WHERE  title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cursor.fetchall()
        return rows

    def delete (self,id):
        self.cursor.execute("DELETE FROM bookStore WHERE id=?", (id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cursor.execute("UPDATE bookStore SET  title=?,author=?,year=?,isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit() 
    
    def __del__(self):
        self.conn.close