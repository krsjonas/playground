# -*- coding: utf-8 -*-

# locale: en-US

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

print("How many numbers to operate with? (1-17)")
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

elif num_of_numbers == 6:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 7:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 8:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    num8 = int(input("Enter the eighth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 9:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    num8 = int(input("Enter the eighth number: "))
    num9 = int(input("Enter the nineth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 10:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    num8 = int(input("Enter the eighth number: "))
    num9 = int(input("Enter the nineth number: "))
    num10 = int(input("Enter the tenth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 11:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    num8 = int(input("Enter the eighth number: "))
    num9 = int(input("Enter the nineth number: "))
    num10 = int(input("Enter the tenth number: "))
    num11 = int(input("Enter the eleventh number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 12:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    num8 = int(input("Enter the eighth number: "))
    num9 = int(input("Enter the nineth number: "))
    num10 = int(input("Enter the tenth number: "))
    num11 = int(input("Enter the eleventh number: "))
    num12 = int(input("Enter the twelveth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 13:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    num8 = int(input("Enter the eighth number: "))
    num9 = int(input("Enter the nineth number: "))
    num10 = int(input("Enter the tenth number: "))
    num11 = int(input("Enter the eleventh number: "))
    num12 = int(input("Enter the twelveth number: "))
    num13 = int(input("Enter the thirteenth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 14:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    num8 = int(input("Enter the eighth number: "))
    num9 = int(input("Enter the nineth number: "))
    num10 = int(input("Enter the tenth number: "))
    num11 = int(input("Enter the eleventh number: "))
    num12 = int(input("Enter the twelveth number: "))
    num13 = int(input("Enter the thirteenth number: "))
    num14 = int(input("Enter the fourteenth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13 - num14
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13 * num14
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13 / num14
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 15:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    num8 = int(input("Enter the eighth number: "))
    num9 = int(input("Enter the ninth number: "))
    num10 = int(input("Enter the tenth number: "))
    num11 = int(input("Enter the eleventh number: "))
    num12 = int(input("Enter the twelfth number: "))
    num13 = int(input("Enter the thirteenth number: "))
    num14 = int(input("Enter the fourteenth number: "))
    num15 = int(input("Enter the fifteenth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14 + num15
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13 - num14 - num15
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13 * num14 * num15
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13 / num14 / num15
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")
    
elif num_of_numbers == 16:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    num8 = int(input("Enter the eighth number: "))
    num9 = int(input("Enter the nineth number: "))
    num10 = int(input("Enter the tenth number: "))
    num11 = int(input("Enter the eleventh number: "))
    num12 = int(input("Enter the twelveth number: "))
    num13 = int(input("Enter the thirteenth number: "))
    num14 = int(input("Enter the fourteenth number: "))
    num15 = int(input("Enter the fifteenth number: "))
    num16 = int(input("Enter the sixteenth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14 + num15 + num16
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13 - num14 - num15 - num16
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13 * num14 * num15 * num16
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13 / num14 / num15 / num16
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

elif num_of_numbers == 17:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    num6 = int(input("Enter the sixth number: "))
    num7 = int(input("Enter the seventh number: "))
    num8 = int(input("Enter the eighth number: "))
    num9 = int(input("Enter the nineth number: "))
    num10 = int(input("Enter the tenth number: "))
    num11 = int(input("Enter the eleventh number: "))
    num12 = int(input("Enter the twelveth number: "))
    num13 = int(input("Enter the thirteenth number: "))
    num14 = int(input("Enter the fourteenth number: "))
    num15 = int(input("Enter the fifteenth number: "))
    num16 = int(input("Enter the sixteenth number: "))
    num17 = int(input("Enter the seventeenth number: "))
    print("Which operator do you want to use?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14 + num15 + num16 + num17
    elif operator == 2:
        result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10 - num11 - num12 - num13 - num14 - num15 - num16 - num17
    elif operator == 3:
        result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10 * num11 * num12 * num13 * num14 * num15 * num16 * num17
    elif operator == 4:
        result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10 / num11 / num12 / num13 / num14 / num15 / num16 / num17
    else:
        print("Invalid input for an operator.")
    print("The result is " + str(result) + ".")

else:
    print("Too many or too few numbers or incorrect input.")

print("***Closing this window means deleting the entered data.***")
