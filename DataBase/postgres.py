# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:31:52 2019

@author: Mauro
"""

import psycopg2

def create_table():    
    conn=psycopg2.connect("dbname='db1' user='postgres' password='07031980' host='localhost' port='5432'")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL) ")
    conn.commit()
    conn.close
    
def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='07031980' host='localhost' port='5432'")
    cursor=conn.cursor()
    cursor.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close
    
def view():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='07031980' host='localhost' port='5432'")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows=cursor.fetchall()
    conn.close()
    return rows

def delete (item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='07031980' host='localhost' port='5432'")
    cursor=conn.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()  
    
def update (quantity, price, item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='07031980' host='localhost' port='5432'")
    cursor=conn.cursor()
    cursor.execute("update store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item))
    conn.commit()
    conn.close()  

create_table()
insert("Orange",21,0.6)
update (13,0.6,"Orange")
print(view())
    
    
    
    