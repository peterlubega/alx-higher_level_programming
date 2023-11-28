#!/usr/bin/python3
user_input = input("Enter a number: ")
number = int(user_input)
if number == 0:
   print(number, "is Zero")
elif number < 0:
   print(number, "is negative")
else:
    print(number, "is positive")
