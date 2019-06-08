# -*- coding: utf-8 -*-

import time

print("In advance: This script is fully GDPR/DSGVO compliant and does not store any input data! ;-)")
time.sleep(3)

print("Enter your name:")
name = input()
print("Hello " + name + "!")

print("-------------------------------------------------------------------")

print("How old are you?")
age = input()
print("O.K., you are " + age + " years old.")

print("-------------------------------------------------------------------")

print("What year are you born in?")
year_of_birth = input()
print("Thank you! You are born in " + year_of_birth + " .")

print("-------------------------------------------------------------------")

x = 5
while x > -1:
    print(x)
    x -= 1
    time.sleep(1)

print("-------------------------------------------------------------------")

print("Here you can see the 'epoch', the moment, at which the time of this computer begins:")
print(time.gmtime(0))
time.sleep(4)

print("-------------------------------------------------------------------")

print("Here you can see the time (in seconds), that has passed since the 'epoch':")
print(time.time())
time.sleep(4)

print("-------------------------------------------------------------------")

print("Bye, " + name + "!")

print("-------------------------------------------------------------------")

print("A little calculator")
print("Disclaimer: This calculator only does +, -, * and / operations.")

print("How many numbers to operate with? (1-5)")
num_of_numbers = int(input())

if num_of_numbers == 1:
    num1 = int(input("Enter the number: "))
    result = num1
    print("The result is " + str(result) + ".")

elif num_of_numbers == 2:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2
    elif operator == 2:
        result = num1 - num2
    elif operator == 3:
        result = num1 * num2
    elif operator == 4:
        result = num1 / num2
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3
    elif operator == 2:
        result = num1 - num2 - num3
    elif operator == 3:
        result = num1 * num2 * num3
    elif operator == 4:
        result = num1 / num2 / num3
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 4:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4
    elif operator == 2:
        result = num1 - num2 - num3 - num4
    elif operator == 3:
        result = num1 * num2 * num3 * num4
    elif operator == 4:
        result = num1 / num2 / num3 / num4
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 5:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

else:
    print("Too many or too few numbers or incorrect input.")

print("***Closing this window means deleting the entered data.***")
