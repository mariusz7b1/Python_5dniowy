# przykład a

moja_lista = [1, 2, 3, 4, 5]
moja_lista.insert(1, 6)
del moja_lista[0]
moja_lista.append(1)

print(moja_lista)

# przykład b
moja_lista = [1, 2, 3, 4, 5]
moja_lista2 = []
add = 0
for number in moja_lista:
    add += number
    moja_lista2.append(add)

print(moja_lista2)

# przykład c
moja_lista = []
del moja_lista
# print(moja_lista)

# przykład d

moja_lista = [1, [2, 3], 4]
print(moja_lista[1])
print(len(moja_lista))
