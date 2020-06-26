with open("text_3.txt", "r", encoding='utf-8') as ser:
    s_sum = []
    less = []
    line = ser.read().split('\n')
    for i in line:
        i= i.split()
        if float (i[1])< 20000:
            less.append(i[0])
        s_sum.append(i[1])

print(f" Менее 20 000 {less} Средняя {sum(map(float, s_sum)) / len(s_sum)}!")
