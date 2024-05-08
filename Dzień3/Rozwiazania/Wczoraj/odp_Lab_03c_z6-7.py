"""
Przykładowa relizacja:
Zadanie 6,7  z Laboratorium 03c
"""
from os import system
system('cls')
str1 = input("Podaj ciąg znaków: ")
# zadanie 6
# w jednej lini:
print("-".join(list("".join(str1.split()))))

# rozbite na dwie = input("Podaj ciąg znaków: ")
str2 = ("".join(str1.split()))
print("-".join(list(str2)))


# zadanie 6
print(str1[::-1])
# bez spacji
print(str2[::-1])
