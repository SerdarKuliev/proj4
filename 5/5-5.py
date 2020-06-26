from random import randint

num_str = " ".join([str(randint(1, 1000)) for _ in range(100000)])
with open("python.txt", mode="w+") as file:
    file.write(num_str)
    file.seek(0)
    print(sum(map(int, file.readline().split())))
