# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 00:00:31 2019

@author: Mauro
"""
import time
from datetime import datetime as dt
#host_path="C:\Windows\System32\drivers\etc\hosts"
hosttemp="hosts"#path to hosts file
redirect="127.0.0.1" #fake ip to redirect browser when blocked page searched
website_list=["www.youporn.com","youporn.com", "tube8.com","www.tube8.com"] #sites to block

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,22):#checks if current time is in the timeframe 
        with open(hosttemp,"r+") as file:#opens the file "host" via a Variable
            content=file.read()
            for web in website_list:# iterates the website list 
                if web in content: #if item in the list is already in the text file it does nothin
                    pass
                else:
                    file.write(redirect+" "+ web+"\n") #if item is not tin the text it write it down  
        
                    
    else:
        with open(hosttemp,"r+") as file:
            content=file.readlines() #readlines convert text to list
            file.seek(0) #places cursor at the beggining of the text file.
            for line in content:
                if not any(web in line for web in website_list):#compares website list vs file.readlines list. If item not found in file.readline, it appends the line in the file
                    file.write(line) #write items from file.readlines list if condition met
                    file.truncate #It crops the text after the appended text from list
               
time.sleep(5) #time interbal to execute the loop
    
    


