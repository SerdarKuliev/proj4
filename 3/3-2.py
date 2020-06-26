#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_f(f1, f2, f3, f4, f5, f6):
    return f1, f2, f3, f4, f5, f6
print(my_f(input("Insert your name: "), input("Insert your surname: "), input("Insert your year of a birth: "), input("Insert your city: "), input("Insert your email: "), input("Insert your phone number: ")))


