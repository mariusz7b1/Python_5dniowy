"""
pliki - tradycyjna obsługa otwórz / zamknij
"""

from sys import exit
from os import system


def czysc_slowo(slowo):
    # Usuwamy spacje na początku i na końcu słowa
    slowo = slowo.strip()

    # Usuwamy znaki nie będące literami na początku słowa
    while len(slowo) > 0 and not slowo[0].isalpha():
        slowo = slowo[1:]

    # Usuwamy znaki nie będące literami na końcu słowa
    while len(slowo) > 0 and not slowo[-1].isalpha():
        slowo = slowo[:-1]

    # Zamieniamy słowo na małe litery
    slowo = slowo.lower()

    return slowo


system("cls")

# odczyt z pliku

in_file_name = "testowy.txt"
out_file_name = "slowa_z_pliku.txt"
file_path = "d:\\dane\\"     # "d:\dane\"

try:
    # otwarcie pliku do odczytu
    f_in = open(file_path + in_file_name, "rt", encoding="utf-8")
except IOError:
    print("Nie udało się otworzyć pliku do odczytu")
    exit()

try:
    # otwarcie pliku do zapisu
    f_out = open(file_path + out_file_name, "wt", encoding="utf-8")
except IOError:
    print("Nie udało się otworzyć pliku do zapisu")
    f_in.close()  # nie jest to konieczne
    exit()

f_out.write("To jest moj plik ze słowami" + "\n\n")
lista_slow = []
while True:
    # odczyt za posrednictewm readline
    linia = f_in.readline()
    if len(linia) == 0:
        break
    else:
        # przykład
        lista_slow_lini = linia.split()
        for slowo in lista_slow_lini:
            slowo = czysc_slowo(slowo)
            lista_slow.append(slowo)

lista_slow = list(set(lista_slow))
lista_slow.sort()

for slowo in lista_slow:
    f_out.write(slowo + "\n")

f_in.close()
f_out.close()
