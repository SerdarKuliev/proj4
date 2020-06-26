
#Var1-------------------------------------------------------------
with open("ex1.txt", "w+", encoding='utf-8') as ser:
    ser.writelines([input("ВВЕДИ ФИО:"), "\n", input("ВОЗРАСТ:"), "\n", input("ВЕРОИСПОВЕДАНИЕ:"), "\n"])

#Var2------------------------------------------------------------- ??? не работает почему-то
with open("ex1-2.txt", "w+", encoding='utf-8') as ser2:
    def serd():
        try:
            ser.writelines([input("ВВЕДИ ФИО:"),"\n", input("ВОЗРАСТ:"),"\n", input("ВЕРОИСПОВЕДАНИЕ:"),"\n"])
            return
        except ValueError:
            return "the end"
print(serd)

#Var3-------------------------------------------------------------
lines = [input("ВВЕДИ ФИО:"), input("ВОЗРАСТ:"), input("ВЕРОИСПОВЕДАНИЕ:")]
with open("ex1-3.txt", "w+") as file:
    for  line in lines:
        file.write(line + '\n')


#Var4-------------------------------------------------------------
with open("ex1.txt", "w+", encoding='utf-8') as ser:
    while True:
        line = input("ВВЕДИ: ")
        if not line:
            break
        print (line, file=ser)
