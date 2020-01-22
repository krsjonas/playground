# -*- coding: utf-8 -*-

print("Hallo! Ich bin Chatty! Wie heißt Du?")
name = str(input("Ich heiße: "))
print("Hallo, " + name + "!")

print("Kleiner Hinweis: Wenn Du nicht mehr mit mir chatten möchtest, drücke einfach Strg+Z")  # Tastenkombination überprüfen und implementieren!

i = 0
while i == 0:
    print("Gib hier eine Frage ein:")
    answer = str(input())
    if answer == "Wie heißt Du?":
        print("Ich bin Chatty!")
    elif answer == "Wie heißt du?":
        print("Ich bin Chatty!")
    elif answer == "Wer bist Du?":
        print("Ich bin Chatty!")
    elif answer == "Wer bist du?":
        print("Ich bin Chatty!")
    elif answer == "Wie alt bist Du?":
        print("Ich wurde im Januar 2020 programmiert, also bin ich noch nicht einmal ein Jahr alt.")
    elif answer == "Wie alt bist du?":
        print("Ich wurde im Januar 2020 programmiert, also bin ich noch nicht einmal ein Jahr alt.")
    elif answer == "Was hast Du an?":
        print("Ich als Bot bin nicht real, darum habe ich auch keine Kleidung.")
    elif answer == "Was hast du an?":
        print("Ich als Bot bin nicht real, darum habe ich auch keine Kleidung.")
    elif answer == "Was ist 2+2?":
        print("Das Ergebnis ist 4.")  # flexibler gestalten, als eine Art Taschenrechner
    else:
        print("Tut mir leid, ich habe Deine Frage nicht verstanden.")