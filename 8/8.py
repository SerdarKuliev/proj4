#1
class Data:
    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = str(dd_mm_yy)

    @classmethod
    def ext(cls, dd_mm_yy):
        date = []

        for i in dd_mm_yy.split():
            if i != '-': date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'OK!'
                else:
                    return f'Fail'
            else:
                return f'Fail'
        else:
            return f'Fail'

    def __str__(self):
        return f'{Data.ext(self.dd_mm_yy)}'


today = Data('08 - 1 - 1986')
print(today)
print(Data.valid(8, 1, 1986))
print(today.valid(11, 8, 1998))
print(Data.ext('11 - 06 - 2000'))
print(today.ext('21 - 06 - 2020'))
print(Data.valid(1, 11, 2000))


#2-
class Div_0:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    @staticmethod
    def div1(n1, n2):
        try:
            return (n1/n2)
        except:
            return (f"NONE")


div = Div_0(20, 100)
print(Div_0.div1(1, 0))
print(Div_0.div1(1005, 0.8))

#3-
class Error:
    def __init__(self, *args):
        self.list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите: '))
                self.list.append(val)
                print(f'Текущий список: {self.list} \n ')
            except:
                print(f"Недопустимое значение!")
                y_or_n = input(f'Попробовать ещё? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(o.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'out'
                else:
                    return f'out'

o = Error(1)
print(o.my_input())

#456-
class Store:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель': self.name, 'Цена': self.price, 'Кол-во': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):


        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(Store):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Store):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Store):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())


# 7
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)