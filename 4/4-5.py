from functools import reduce

def gen(x,y):
    return x*y

list= [el for el in range(100,1001,2)]
print(f"list: {list}\nNumbers: {reduce(gen,list)}")


