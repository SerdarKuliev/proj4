class TX:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def c(self):
        return round(self.width / 6.5 + 0.5, 3)

    def j(self):
        return round(self.height * 2 + 0.3, 3)

    @property
    def full(self):
        return str(f'Общее количество ткани {round(self.width / 6.5 + 0.5, 3) + round(self.height * 2 + 0.3, 3)}')


class Coat(TX):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.sc = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'На пальто ушло {self.sc} м. ткани'


class Jacket(TX):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.sj = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'На костюм ушло {self.sj} м. ткани'

coat = Coat(3, 4)
jacket = Jacket(1.5, 2)
print(coat)
print(jacket)
print(coat.full)
print(jacket.full)
print(jacket.c())
print(jacket.j())