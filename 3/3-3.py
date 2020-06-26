#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_f():
    w1 = int(input("Insert number 1: "))
    w2 = int(input("Insert number 2: "))
    w3 = int(input("Insert number 3: "))
    n =(w1+w2+w3)-(min(w1, w2, w3))
    return n
print(my_f())