#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
#Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [34, None, 3.14, "Yo!", [1,2,67], 8*5, '8*5', True, '1:key']
print("Всего элементов: " + str(len(my_list)))
print("Тип списка: " + str(type(my_list)))
print("1-й элемент: " +str(type(my_list[0])) + " = " + str(my_list[0]))
print("3-й элемент: " +str(type(my_list[2])) + " = " + str(my_list[2]))
print("4-й элемент: " +str(type(my_list[3])) + " = " + str(my_list[3]))
print("5-й элемент: " +str(type(my_list[4])) + " = " + str(my_list[4]))
print("6-й элемент: " +str(type(my_list[5])) + " = " + str(my_list[5]))
print("7-й элемент: " +str(type(my_list[6])) + " = " + str(my_list[6]))
print("8-й элемент: " +str(type(my_list[7])) + " = " + str(my_list[7]))
print("9-й элемент: " +str(type(my_list[8])) + " = " + str(my_list[8]))
print(my_list)
ok = input("!")