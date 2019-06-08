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

x = 0
while x < 5:
    print(x)
    x += 1
    time.sleep(0.5)

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
print("***Closing this windows means deleting the entered data.***")
