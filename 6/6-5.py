class Stationery:
    title = "title"

    def draw(self):
        print("Запуск отрисовки.")

class Pen:
    Stationery.title = "Pen"
    print(Stationery.title)


class Pencil:
    Stationery.title = "Pencil"
    print(Stationery.title)

class Handle:
    Stationery.title = "Handle"
    print(Stationery.title)




