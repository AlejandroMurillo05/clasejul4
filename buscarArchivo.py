import io 

fd = open("mbox-short.txt", "r", encoding="utf-8")
cont =  0
for linea in fd:
    if linea.lower().find("From") > -1:
        cont += 1  
    
fd.close()

print("Cantidad de lineas: ", cont)