# -*- coding: utf-8 -*-

# locale: de-DE

import time

print("Vorab: Dieses Skript ist vollständig GDPR/DSGVO-konform und speichert keinerlei eingegebene Daten! ;-)")
time.sleep(3)

print("Gib Deinen Namen ein:")
name = input()
print("Hallo " + name + "!")

print("-------------------------------------------------------------------")

print("Wie alt bist Du?")
age = input()
print("O.K., Du bist " + age + " Jahre alt.")

print("-------------------------------------------------------------------")

print("In welchem Jahr bist Du geboren?")
year_of_birth = input()
print("Danke! Du bist im Jahr " + year_of_birth + " geboren.")

print("-------------------------------------------------------------------")

x = 5
while x > -1:
    print(x)
    x -= 1
    time.sleep(1)

print("-------------------------------------------------------------------")

print("Hier siehst Du den 'Epoch', also den Zeitpunkt, an dem die Zeitrechnung dieses Computers beginnt:")
print(time.gmtime(0))
time.sleep(4)

print("-------------------------------------------------------------------")

print("Hier siehst Du die Zeit (in Sekunden), die seit dem 'Epoch' vergangen ist:")
print(time.time())
time.sleep(4)

print("-------------------------------------------------------------------")

print("Tschau, " + name + "!")

print("-------------------------------------------------------------------")

print("Ein kleiner Taschenrechner")
print("Disclaimer: Dieser Taschenrechner rechnet nur mit +, -, * und /.")

print("Mit wie vielen Zahlen soll gerechnet werden? (1-9)")
number_of_numbers = int(input())

if number_of_numbers == 1:
    number_1 = int(input("Gib die Zahl ein: "))
    result = number_1
    print("Das Ergebnis ist " + str(result) + ".")

elif number_of_numbers == 2:
    number_1 = int(input("Gib die erste Zahl ein: "))
    number_2 = int(input("Gib die zweite Zahl ein: "))
    print("Welchen Operator willst Du benutzen?")
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
        print("Ungültige Eingabe für einen Operator.")
    print("Das Ergebnis ist " + str(result) + ".")

elif number_of_numbers == 3:
    number_1 = int(input("Gib die erste Zahl ein: "))
    number_2 = int(input("Gib die zweite Zahl ein: "))
    number_3 = int(input("Gib die dritte Zahl ein: "))
    print("Welchen Operator willst Du benutzen?")
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
        print("Ungültige Eingabe für einen Operator.")
    print("Das Ergebnis ist " + str(result) + ".")

elif number_of_numbers == 4:
    number_1 = int(input("Gib die erste Zahl ein: "))
    number_2 = int(input("Gib die zweite Zahl ein: "))
    number_3 = int(input("Gib die dritte Zahl ein: "))
    number_4 = int(input("Gib die vierte Zahl ein: "))
    print("Welchen Operator willst Du benutzen?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = number_1 + number_2 + number_3 + number_4
    elif operator == 2:
        result = number_1 - number_2 - number_3 - number_4
    elif operator == 3:
        result = number_1 * number_2 * number_3 * number_4
    elif operator == 4:
        result = number_1 / number_2 / number_3 / number_4
    else:
        print("Ungültige Eingabe für einen Operator.")
    print("Das Ergebnis ist " + str(result) + ".")

elif number_of_numbers == 5:
    number_1 = int(input("Gib die erste Zahl ein: "))
    number_2 = int(input("Gib die zweite Zahl ein: "))
    number_3 = int(input("Gib die dritte Zahl ein: "))
    number_4 = int(input("Gib die vierte Zahl ein: "))
    number_5 = int(input("Gib die fünfte Zahl ein: "))
    print("Welchen Operator willst Du benutzen?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = number_1 + number_2 + number_3 + number_4 + number_5
    elif operator == 2:
        result = number_1 - number_2 - number_3 - number_4 - number_5
    elif operator == 3:
        result = number_1 * number_2 * number_3 * number_4 * number_5
    elif operator == 4:
        result = number_1 / number_2 / number_3 / number_4 / number_5
    else:
        print("Ungültige Eingabe für einen Operator.")
    print("Das Ergebnis ist " + str(result) + ".")

elif number_of_numbers == 6:
    number_1 = int(input("Gib die erste Zahl ein: "))
    number_2 = int(input("Gib die zweite Zahl ein: "))
    number_3 = int(input("Gib die dritte Zahl ein: "))
    number_4 = int(input("Gib die vierte Zahl ein: "))
    number_5 = int(input("Gib die fünfte Zahl ein: "))
    number_6 = int(input("Gib die sechste Zahl ein: "))
    print("Welchen Operator willst Du benutzen?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = number_1 + number_2 + number_3 + number_4 + number_5 + number_6
    elif operator == 2:
        result = number_1 - number_2 - number_3 - number_4 - number_5 - number_6
    elif operator == 3:
        result = number_1 * number_2 * number_3 * number_4 * number_5 * number_6
    elif operator == 4:
        result = number_1 / number_2 / number_3 / number_4 / number_5 / number_6
    else:
        print("Ungültige Eingabe für einen Operator.")
    print("Das Ergebnis ist " + str(result) + ".")

elif number_of_numbers == 7:
    number_1 = int(input("Gib die erste Zahl ein: "))
    number_2 = int(input("Gib die zweite Zahl ein: "))
    number_3 = int(input("Gib die dritte Zahl ein: "))
    number_4 = int(input("Gib die vierte Zahl ein: "))
    number_5 = int(input("Gib die fünfte Zahl ein: "))
    number_6 = int(input("Gib die sechste Zahl ein: "))
    number_7 = int(input("Gib die siebte Zahl ein: ")
    print("Welchen Operator willst Du benutzen?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = number_1 + number_2 + number_3 + number_4 + number_5 + number_6 + number_7
    elif operator == 2:
        result = number_1 - number_2 - number_3 - number_4 - number_5 - number_6 - number_7
    elif operator == 3:
        result = number_1 * number_2 * number_3 * number_4 * number_5 * number_6 * number_7
    elif operator == 4:
        result = number_1 / number_2 / number_3 / number_4 / number_5 / number_6 / number_7
    else:
        print("Ungültige Eingabe für einen Operator.")
    print("Das Ergebnis ist " + str(result) + ".")

elif number_of_numbers == 8:
    number_1 = int(input("Gib die erste Zahl ein: "))
    number_2 = int(input("Gib die zweite Zahl ein: "))
    number_3 = int(input("Gib die dritte Zahl ein: "))
    number_4 = int(input("Gib die vierte Zahl ein: "))
    number_5 = int(input("Gib die fünfte Zahl ein: "))
    number_6 = int(input("Gib die sechste Zahl ein: "))
    number_7 = int(input("Gib die siebte Zahl ein: "))
    number_8 = int(input("Gib die achte Zahl ein: "))
    print("Welchen Operator willst Du benutzen?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = number_1 + number_2 + number_3 + number_4 + number_5 + number_6 + number_7 + number_8
    elif operator == 2:
        result = number_1 - number_2 - number_3 - number_4 - number_5 - number_6 - number_7 - number_8
    elif operator == 3:
        result = number_1 * number_2 * number_3 * number_4 * number_5 * number_6 * number_7 * number_8
    elif operator == 4:
        result = number_1 / number_2 / number_3 / number_4 / number_5 / number_6 / number_7 / number_8
    else:
        print("Ungültige Eingabe für einen Operator.")
    print("Das Ergebnis ist " + str(result) + ".")

elif number_of_numbers == 9:
    number_1 = int(input("Gib die erste Zahl ein: "))
    number_2 = int(input("Gib die zweite Zahl ein: "))
    number_3 = int(input("Gib die dritte Zahl ein: "))
    number_4 = int(input("Gib die vierte Zahl ein: "))
    number_5 = int(input("Gib die fünfte Zahl ein: "))
    number_6 = int(input("Gib die sechste Zahl ein: "))
    number_7 = int(input("Gib die siebte Zahl ein: "))
    number_8 = int(input("Gib die achte Zahl ein: "))
    number_9 = int(input("Gib die neunte Zahl ein: "))
    print("Welchen Operator willst Du benutzen?")
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    operator = int(input())
    if operator == 1:
        result = number_1 + number_2 + number_3 + number_4 + number_5 + number_6 + number_7 + number_8 + number_9
    elif operator == 2:
        result = number_1 - number_2 - number_3 - number_4 - number_5 - number_6 - number_7 - number_8 - number_9
    elif operator == 3:
        result = number_1 * number_2 * number_3 * number_4 * number_5 * number_6 * number_7 * number_8 * number_9
    elif operator == 4:
        result = number_1 / number_2 / number_3 / number_4 / number_5 / number_6 / number_7 / number_8 / number_9
    else:
        print("Ungültige Eingabe für einen Operator.")
    print("Das Ergebnis ist " + str(result) + ".")

else:
    print("Zu viele oder zu wenige Zahlen oder fehlerhafte Eingabe.")

print("***Beim Schließen dieses Fensters werden alle eingegebenen Daten gelöscht.***")
