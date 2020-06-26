i = int(input("Число"))
i2 = i%10
i = i//10
while i > 0:
   if i%10 > i2:
       i2 = i%10
   i = i//10
print("Самое большое из числел " + str(i2))
