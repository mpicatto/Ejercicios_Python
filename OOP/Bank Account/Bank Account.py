# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:52:16 2019

@author: Mauro
"""

class Account:
    def __init__(self,filepath):
        self.filepath=filepath
        with open (filepath,'r') as file:
            self.balance=int(file.read())
            
    def withdraw(self, amount):
        self.balance=self.balance-amount
        
    def deposit(self, amount):
        self.balance=self.balance+amount
    
    def commit(self):
        with open (self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    
    type="cheking"
    
    def __init__(self, filepath,fee):
        Account.__init__(self, filepath)
        self.fee=fee
    
    def transfer(self, amount):
        self.balance=self.balance-amount - self.fee
        
        
        
jack_checking=Checking("jack.txt",5)
jack_checking.deposit(400)
jack_checking.commit()
print(jack_checking.balance)

joanne_checking=Checking("joanne.txt",5)
joanne_checking.deposit(400)
joanne_checking.commit()
print(joanne_checking.balance)

        

        