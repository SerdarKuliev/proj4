time= input("Введите число, в секундах, и я переведу его в часы.")
time = int(time)
htime = time//3600
mtime = time//60-htime*60
stime = time%60
print('{0}:{1}:{2}'.format((htime), (mtime), (stime)))
