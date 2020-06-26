#1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_f(num, num2):
    global n
num = input("Insert number:")
num2 = input("Insert still another number:")
print("Your numbers: " + str(num) + " and " + str(num2))
try:
    num = int(num)
    num2 = int(num2)
    n = int(num / num2)
    print((str(num)) + ":" + (str(num2)) + "=" + (str(n)))
except (ValueError, ZeroDivisionError):
    print("ERROR, it's 0 or not number.")
OK = input("OK?")