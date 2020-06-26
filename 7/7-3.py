class Cell:
    def __init__(self, W):
        self.W = int(W)

    def __str__(self):
        return f'Result {self.W * "*"}'

    def __add__(self, other):
        return Cell(self.W + other.W)

    def __sub__(self, other):
         return self.W - other.W if (self.W - other.W) > 0 else print('minus')

    def __mul__(self, other):
        return Cell(int(self.W * other.W))

    def __truediv__(self, other):
         return Cell(round(self.W // other.W))

    def order(self, cellsrow):
        row = ''
        for i in range(int(self.W / cellsrow)):
            row += f'{"*" * cellsrow} \\n'
        row += f'{"*" * (self.W % cellsrow)}'
        return row

cells1 = Cell(15)
cells2 = Cell(7)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.order(3))
print(cells1.order(4))
print(cells1 / cells2) 