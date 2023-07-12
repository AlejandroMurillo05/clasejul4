import io

#abrirlo

fd = open("texto.txt", "r")
fd.seek(55)
#leer = fd.read()
leer2 = fd.readline(6)
leer3 = fd.readlines()
fd.close()

print(leer2.rstrip())
print(leer3)


