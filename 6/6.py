def read_data("jjj.txt"):
    data = []
with open("jjj.txt", 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.split()
for item in parts:
    data.append(int(item))
    return data

numbers = read_data("jjj.txt")
print(numbers)
print(sum(numbers))