#Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
#for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
#начиная с 1! и до n!.
#Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import islice, cycle, count

def ex7(el1,el2,el3):
    try:
        el1,el2,el3 = int(el1), int(el2), int(el3)
        list = [el for el in islice(count(), el1, el2 + 1)]
        r_list = iter(el for el in cycle(list))
        rep_list = [next(r_list) for _ in range(list)]
        print(list)
        return rep_list
    except ValueError:
        return "Error!!"

print(ex7(input("1:"), input("2:"), input("3:")))

