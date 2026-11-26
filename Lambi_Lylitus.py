# Autor: Vahur Maask
# Kuupäev: 26.11.2026

import time

# Algseadistus
lamp_H1 = False

print("Programmi algus")

while True:
    print("\nLambi olek:", "SEES" if lamp_H1 else "VÄLJAS")

    lyliti = input("Kas vajutad lülitit S1? (jah/ei): ").lower()

    # Kontrollime, kas lüliti S1 on vajutatud
    if lyliti == "jah":

        # Kontrollime lambi olekut
        if lamp_H1:
            print("Deaktiveeri lamp H1")
            lamp_H1 = False

        else:
            print("Aktiveeri lamp H1")
            lamp_H1 = True

            # Lülita lamp sisse 10 minutiks
            print("Lamp H1 põleb 10 minutit...")
            time.sleep(600)

            lamp_H1 = False
            print("10 minutit möödus. Lamp H1 lülitati välja.")

    elif lyliti == "ei":
        print("Lülitit ei vajutatud.")

    else:
        print("Vale sisend! Sisesta jah või ei.")
