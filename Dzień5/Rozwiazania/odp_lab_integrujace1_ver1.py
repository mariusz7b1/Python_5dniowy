"""" Rozwiązanie zadania integrujacego 1  versja 1"""
# importowanie modułów
import sys
from os import system

# FUNKCJE
# zwraca miasto z adresu


def get_miasto(adres):
    lst_adres = adres.split(",")
    miasto = lst_adres[1]
    miasto = miasto[7:]

    return miasto

# zwraca dostawce @ z adresu mail


def get_mail(mail):
    adres_mail = mail.split("@")[1]
    adres_mail = adres_mail[0:-1]
    return adres_mail

# pobiera dane z pliku zwraca listę  której elementami jest słownik


def get_data_fromfile(pelna_nazwa_pliku):
    try:
        f_in = open(pelna_nazwa_pliku, 'rt', encoding='utf-8')
    except IOError:
        print('Brak pliku z danymi źródłowymi')
        sys.exit()

    dane = []
    linia = f_in.readline()
    while linia != '':
        dane_linia = linia.split(";")

        if len(dane_linia) > 9:  # podwójne imię
            zm1 = 1
        else:
            zm1 = 0

        imie = dane_linia[0]

        nazwisko = dane_linia[1 + zm1]

        miasto = get_miasto(dane_linia[4 + zm1])

        dostawca_mail = get_mail(dane_linia[8 + zm1])

        dane.append({"imie": imie,
                    "nazwisko": nazwisko,
                     "miasto": miasto,
                     "dostawca_mail": dostawca_mail})
        linia = f_in.readline()
    f_in.close()
    return dane

# zwraca słownik imion wraz z ilością wystąpień


def get_dic_imion(dane):
    slownik_imion = {}
    for ele in dane:
        imie = ele["imie"]
        if imie not in slownik_imion:
            slownik_imion[imie] = 1
        else:
            slownik_imion[imie] += 1
    return slownik_imion

# zwraca liste z najbardziej polularnym imieniem/imionami


def get_polularne_imie(imiona):
    maksimum = max(imiona.values())
    lst = []
    for klucz in imiona.keys():
        if imiona[klucz] == maksimum:
            lst.append({klucz: imiona[klucz]})
    return lst


# czyszczenie ekranu
system("cls")

nazwa_pliku = "dane_10K.txt"
sciezka_do_pliku = "d:\\dane\\"


pelna_nazwa_pliku = sciezka_do_pliku + nazwa_pliku

lst_dane = get_data_fromfile(pelna_nazwa_pliku)

dic_imion = get_dic_imion(lst_dane)

polularne_imie = get_polularne_imie(dic_imion)
print(polularne_imie)

licznik = 0
for ele in dic_imion.values():
    licznik += ele
print(licznik)
