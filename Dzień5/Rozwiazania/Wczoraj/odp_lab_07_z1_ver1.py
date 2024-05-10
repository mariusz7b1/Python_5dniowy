"""Rozwiązanie zadania 7a.1  wersja z with TRADYCYJNA """
SAMOGLOSKI = "aeiouy"


def main():
    # Definiowanie samogłosek

    # Inicjalizacja liczników
    liczba_a = 0
    rozne_znaki = []
    liczba_samoglosek = 0

    # Otwarcie pliku do odczytu
    with open("d:\\dane\\testowy.txt", "rt", encoding="utf-8") as file:
        for linia in file:
            for znak in linia.lower():
                # Liczenie wystąpień litery "a"
                if znak == 'a':
                    liczba_a += 1
                # Zliczanie różnych znaków
                if znak not in rozne_znaki:
                    rozne_znaki.append(znak)
                # Zliczanie samogłosek
                if znak in SAMOGLOSKI:
                    liczba_samoglosek += 1

    # Otwarcie pliku do zapisu
    with open("d:\\dane\\raport1-a.txt", "wt", encoding="utf-8") as plik_raport:
        plik_raport.write(f"Liczba wystąpień litery 'a': {liczba_a}\n")
        plik_raport.write(f"Liczba różnych znaków: {len(rozne_znaki)}\n")
        plik_raport.write(f"Liczba wystąpień samogłosek: {liczba_samoglosek}\n")


main()
