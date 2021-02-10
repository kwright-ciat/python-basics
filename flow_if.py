'''
flow_if.py
Show basic usage of if statment
'''
age = input("How old are you? ")
if age.isdigit():
    age = int(age)
else:
    print("You must input a integer age!")
    exit()

if age > 15 and age < 18:
    print("old enough to get permit")
elif age > 17:
    print("old enough to drive")
else:
    print("you can't drive yet")

name=input("Enter your name: ")
if name == 'Nick':
    print("Hi there, Nick")
else:
    print("Hello, stranger")
