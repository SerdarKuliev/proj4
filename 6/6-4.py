class Shape_98:
    def __init__(self, speed, color, name, is_police, show_speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed = show_speed

    def go(self):
        print("going")

    def stop(self):
        print("stoping")

    def turn(self):
        print("turning")

r = Shape_98(100, "white", "1", 10, True)
print(r.go())
print(r.stop())
print(r.turn())
print(r)




