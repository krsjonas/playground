#*# coding: utf-8 #*#

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

print("How many numbers to operate with? (1-3)")
number_of_numbers = int(input())

if number_of_numbers == 1:
    number_1 = int(input("Enter the number: "))
    result = number_1
    print("The result is " + str(result) + ".")

elif number_of_numbers == 2:
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = number_1 + number_2
    elif operator == 2:
        result = number_1 - number_2
    elif operator == 3:
        result = number_1 * number_2
    elif operator == 4:
        result = number_1 / number_2
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif number_of_numbers == 3:
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    number_3 = int(input("Enter the third number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = number_1 + number_2 + number_3
    elif operator == 2:
        result = number_1 - number_2 - number_3
    elif operator == 3:
        result = number_1 * number_2 * number_3
    elif operator == 4:
        result = number_1 / number_2 / number_3
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

else:
    print("Too many or too few numbers or incorrect input.")

print("***Closing this window means deleting the entered data.***")
