with open ("text_6.txt", "r") as text6:
    a = text6.readlines()
    for i in a:
        new_str = ''.join((q if q in '123456789' else ' ') for q in i)
        new_2 = [int(q) for q in new_str.split()]
        print(f"{i.split()[0]}{sum(new_2)}")


