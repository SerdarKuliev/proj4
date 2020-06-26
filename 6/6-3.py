class Worker:
    name = "Sergey"
    surname = "Frolov"
    position = "manager"
    income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):
    get_full_name = Worker.name + Worker.surname
    get_total_income = (Worker.wage: input(": ") + Worker.bonus: input(": "))

    def start(self):
        print(f"111")

    def stop(self):
        print("000")

Q= Worker(50,20)
print(q.start())
print(q.stop())