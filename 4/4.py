Это просто записи

#4.2-------------------------------------------------------------
new_list = (300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55)
list = []
for i in range(len(new_list)-1):
    if new_list[i] < new_list[i+1]:
        list.append(new_list[i+1])
print(list)
#4.3---------------------------------------------------------------



#мпорт модклей

def sg_m():
        print('Hello MF')

def calc():
    n = int(input('N'))
    return n**4 + 100500




from sys import argv

scr_name, first, second, third = argv

print(scr_name)
print(first)
print(second)
print(third)



my_list = [1, 2, 3, 4, 5, 6]
new_list = [i +10 for i in my_list if i % 2 == 0]
print(new_list)

my_list = [1, 2, 3, 4, 5, 6]
my_sec_list =[11, 22, 33, 44, 55]
new_list = [i + j for i in my_list if i % 2 == 0 for j in my_sec_list]
print(new_list)


new_list = {el: el*3 for el in range(10,20)}
print(new_list)

list(range(10,21))

my_tup = (1, 2, 3, 4, 5, 6)
new_obj = [i + 3 for i in my_tup if i % 2 == 0 for j in my_sec_list]
print(len(new_obj))

print(next(new_obj))
print(list(new_obj))

#random()
#randint()
#randrange()

from random import randint, randrange, random

print(randint(0,1000))
print(randrange(100,1000, 40))
print(random()*10000)
