import re
p= input("Input your password::  ")
x = True
while x:  
    if (len(p)<12 or len(p)>25):
        print("===================================================")
        print("Length is less than 12 or greater than 25 characters")
        break
    elif not re.search("[a-z]",p):
        print("===================================================")
        print("Does not contain lower case letters")
        break
    elif not re.search("[0-9]",p):
        print("===================================================")
        print("Missing numbers")
        break
    elif not re.search("[A-Z]",p):
        print("===================================================")
        print("Does not contain upper case letters")
        break
    elif not re.search("[$#@]",p):
        print("===================================================")
        print("Missing special characters")
        break
    elif re.search("\s",p):
        print("===================================================")
        break
    else:
        print("Valid Password")
        goodpassword = p
        print(goodpassword)
        x=False
        break

if x:
    print("Not a Valid Password")
    print("===================================================")
    print("Must have more than 12 characters")
    print("have upper and lower case charcters")
    print("Have numbers and have special characters like $#@")
    print("===================================================")
    

