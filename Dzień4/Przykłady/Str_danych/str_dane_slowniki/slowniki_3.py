

# dict.keys() - Zwraca wszystkie klucze w słowniku.

slownik = {'jabłko': 1, 'banan': 2, 'cytryna': 3}
print(slownik.keys())


# dict.values() - Zwraca wszystkie wartości w słowniku.
print(slownik.values())

# dict.items() - Zwraca pary klucz-wartość w formie krotek.
print(slownik.items())

# dict.get(key, default) - Zwraca wartość dla danego klucza, jeśli klucz jest w słowniku. Jeśli nie, zwraca wartość domyślną.
print(slownik.get('ananas', 'Nie znaleziono takiego owocu'))

# dict.setdefault(key, default) - Zwraca wartość dla danego klucza, jeśli klucz istnieje. Jeśli nie, dodaje klucz do słownika z wartością domyślną.
print(slownik.setdefault('ananas', 4))
print(slownik)


# dict.update(another_dict) - Łączy dwa słowniki. Jeśli istnieją zduplikowane klucze, ten metoda nadpisze wartości kluczy w oryginalnym słowniku.

inny_slownik = {'ananas': 5, 'mango': 6}
slownik.update(inny_slownik)
print(slownik)


# dict.pop(key) - Usuwa element ze słownika o podanym kluczu.

slownik.pop('mango')
print(slownik)


# dict.clear() - Usuwa wszystkie elementy ze słownika.

slownik.clear()
print(slownik)
