class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = (self._length * self._width * self.weight * self.height * 0.001)
        return (asphalt_mass)

r = Road
print(r.asphalt_mass(length == int(input(":")), width == int(input(":"))))

