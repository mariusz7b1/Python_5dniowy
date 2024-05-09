def fibonacci(n):
    if n < 0:
        print("Argument musi być liczbą dodatnią.")
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        war1 = fibonacci(n - 1)
        war2 = fibonacci(n - 2)
        return war1+war2


n = int(input("podaj liczbę naturalną "))
wynik = fibonacci(n)
print(f"{n}-ty element ciągu Fibonacciego wynosi: {wynik}")
