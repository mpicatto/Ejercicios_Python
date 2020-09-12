# -*- coding: utf-8 -*-
"""
Created on Wed May 29 02:18:25 2019

@author: Mauro
"""
import json #impotors json library into python
from difflib import get_close_matches #difflib  provides classes and functions for comparing sequences. Imports get_close_matches from module.
data=json.load(open("fullprogram\data.json","r")) #open and read a Json file into a Python dictionary
def findw(word):#Function to search for user word in the dictionary
    if word in data: #if word as written found in dictionary prints definition
        return data[word]
    elif str.lower(word) in data: #convets word lo lower cases and search for it. If found returns it.
        return data[str.lower(word)]
    elif str.upper(word) in data: #convets word lo upper cases and search for it. If found returns it.
        return data[str.upper(word)]
    elif len(get_close_matches(word,data.keys()))>0: # If not found returns closest mach.
        answ=str.upper(input('Did you mean %s instead?. Y/N:' %get_close_matches(str.lower(word),data.keys())[0]))#asks if closest mach was the correct one.
        if answ=="Y": #if yes returs closest match
            return data[get_close_matches(str.lower(word),data.keys())[0]]                
        else:    
            return ""#if not returns nothing, user will be asked to enter a word again
    else:
        return "Word not found, please try again." #word not found, user asked to enter word again.
exit="" #variable used in while loop to exit it
while exit!="N":    #while loop; conditioon to exit is variable exit= to N
    word=str.capitalize(input("Enter a word:")) #User input: word to be searched in dictionaty. Variable word declared
    if word !="": #if statement; if user doesn´t enter a word is asked to enter en word again; if word entered program continues.
        definition=findw(word) #this variable calls findw function adnd passes word as argument
        if type(definition)==list: #checks if definition from the dictionary is a list or not.
            if word in data: #if statement if word is a key in data dictionaru  the word is printed
                print("%s:"%word)
            elif str.upper(word)in data: #if not found looks for the word un upper cases in the dictionary and prints it
                print("%s:"%str.upper(word))
            else:    #if not found it prints the closest match 
                print(str.capitalize("%s: "%get_close_matches(str.lower(word),data.keys())[0]))
            i=0
            while i<len(definition): #loop to print the definition of the word in separate lines. Definition comes tinto a list. the loop prints each item in one line
                print(i+1,".",definition[i])
                i=i+1
            exit=str.upper(input("Look for another word? Y/N:"))   #after printing the definition asked if user wants to look for another word.
        else:
            print(definition) #prints definition form dictionary when is no t a list
            exit=str.upper(input("Look for another word? Y/N:"))#after printing the definition asked if user wants to look for another word.
    else:
        print("Please enter a word!!") #when user does not enter a word it is asked to enter one.
        






