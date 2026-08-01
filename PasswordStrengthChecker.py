#                               Password Strength Checker ⭐⭐⭐
# Ask user for password.

# Check:
# Length ≥ 8
# Contains uppercase
# Contains lowercase
# Contains digit
# Contains special character

# Output:
# Weak
# Medium
# Strong
# Very Strong

# Don't use any external libraries.

import string

def input_pass():
    password = input("\nEnter User Password: ")     #takes input and pass it to data function
    data(password)

def data(password):
    pass_list = [i for i in password]       #1st store password each letter in a list 
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    lowerlist = [i for i in alphabets]          #this store each alphabet as a lower case in a list
    upperlist = [i for i in alphabets.upper()]  #now we are storing each alphabet as upper case in the list
    checker(pass_list, lowerlist, upperlist)    #passes all the lists to the checker function

def checker(pass_list, lowerlist, upperlist):
    checklower = any(i in lowerlist for i in pass_list)   #checks if the password contain any lower case letter if so it return True
    checkupper = any(i in upperlist for i in pass_list)   #checks if the password contain any upper case letter if so it return True
    checknumber = any(i.isdigit() for i in pass_list)     #checks if it contain any digit if so, return True else False
    checksymbol = any(i in string.punctuation for i in pass_list)   #using built-in function (string) to check if it contain any symbol if so return True
    sizeofPassword = len(pass_list)
    checkpass(sizeofPassword,checklower,checkupper,checknumber,checksymbol) 

def checkpass(size, check_lower,check_upper,check_number,check_symbol):
    if size >= 8 and check_number and check_lower and check_upper and check_symbol: #if the conditions are all true then continue else
        if size <= 10:
            print("Medium password")
        elif size <= 12:
            print("Strong password")
        elif size >= 13:
            print("Very Strong password")
        else:
            print("Weak Password.")
    else:
        print("Try Again,\nPassword must be atleast 8 digits and must have 1 upper 1 lower letter and 1 Symbol.")
        input_pass()        #recall the input

input_pass()