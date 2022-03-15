#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:28:36 2022

@author: khalid
"""
print(" # Python program for check the door password !")

# let say initial count number is 0
password_attempt = 1

# Apply while condition and if else in between: Let say count is not 4
while True:
    
    password = input("Please enter your given password: ")

    # Try match the password
    if password_attempt <= 3:
        if password == "open@":
            print("Successfully login!")
            break
        else:
            print("Sorry, try again") 
        password_attempt += 1 
            
    else:
        #print("Please input your security answer")
        security_answer = input("Please enter your security answer for a favorite color:  ")

        if security_answer == "black":
            print("Help the user to reset your password")
        else:
            print("Your door is locked")
        break
        
        
        
