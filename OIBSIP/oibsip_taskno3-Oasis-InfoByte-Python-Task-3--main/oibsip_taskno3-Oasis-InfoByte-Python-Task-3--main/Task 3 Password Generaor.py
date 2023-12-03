import random

lower="qwertyuioplkjhgfdsazxcvbnm"
upper="QWERTYUIOPLKJHGFDSAZXCVBNM"
numbers="1234567890"
symbol="!@#$%^&*()_+=`~/*-+.[]()}{"

all = lower+upper+numbers+symbol
name = input("Enter your name: ")
print("Welcome",name)
print("Welcome to the Password Generator Application")
length = int(input("Enter the Length of Password "))

if length<=0:
    print("Password can't be generated in this length")
else :    
    password="".join(random.sample(all,length))
    print("Password is ",password)
