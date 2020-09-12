# -*- coding: utf-8 -*-
"""
Created on Wed May 29 02:18:25 2019

@author: Mauro
"""
import json
from difflib import get_close_matches
data=json.load(open("fullprogram\data.json","r"))
def findw(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        answ=str.upper(input('Did you mean %s instead?. Y/N:' %get_close_matches(word,data.keys())[0]))
        if answ=="Y":
            return data[get_close_matches(word,data.keys())[0]]                
        else:    
            return ""
    else:
        return "Word not found, please try again."
exit=""
while exit!="N":    
    word=str.lower(input("Enter a word:"))
    if word !="":
        definition=findw(word)
        print(str.capitalize("%s: "%get_close_matches(word,data.keys())[0]))
        i=0
        while i<len(definition):
            print(i+1,".",definition[i])
            i=i+1
        exit=str.upper(input("Look for another word? Y/N:"))
    else:
        print("Please enter a word!!")
        
        







