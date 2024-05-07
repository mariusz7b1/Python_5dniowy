# przykład a
lista_1 = ["A", "B", "C"]
lista_2 = lista_1
lista_3 = lista_2
del lista_1[0]
del lista_2[0]
print(lista_3)

# przykład b
lista_1 = ["A", "B", "C"]
lista_2 = lista_1
lista_3 = lista_2
del lista_1[0]
del lista_2
print(lista_3)

# przykład c
lista_1 = ["A", "B", "C"]
lista_2 = lista_1
lista_3 = lista_2

del lista_1[0]
del lista_2[:]

print(lista_3)


# przykład d
lista_1 = ["A", "B", "C"]
lista_2 = lista_1[:]
lista_3 = lista_2[:]

del lista_1[0]
del lista_2[0]

print(lista_3)
