count = 0
with open("ex2.txt", "r", encoding='utf-8') as ser:
    for line in ser:
        count += 1
        line_words = line.split()
        print(line, 'dlina stroki', len(line_words))
    print('vsego', count)