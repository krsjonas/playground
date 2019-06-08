#*# coding: utf-8 #*#

import time

print("Vorab: Dieses Skript ist vollständig DSGVO-konform und speichert keinerlei eingegebene Daten! ;-)")
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
print("Vielen Dank! Du bist im Jahr " + year_of_birth + " geboren.")

print("-------------------------------------------------------------------")

x = 0
while x < 5:
    print(x)
    x += 1
    time.sleep(0.5)

print("-------------------------------------------------------------------")

print("Hier siehst Du den 'Epoch', also den Zeitpunkt, an dem die Zeitrechnung dieses Computers beginnt:")
print(time.gmtime(0))
time.sleep(4)

print("-------------------------------------------------------------------")

print("Hier siehst Du die Zeit (in Sekunden), die seit dem 'Epoch' vergangen ist")
print(time.time())
time.sleep(4)

print("-------------------------------------------------------------------")

print("Servus, " + name + "!")
