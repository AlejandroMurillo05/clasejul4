import csv
import re
def obtener_direcciones():
    direcciones = []
    with open('mbox-short.txt', 'r') as archivo:
        for linea in archivo:
            if re.match('^From:', linea):
                direccion = re.findall('\S+@\S+', linea)
                if direccion:
                    direcciones.append(direccion[0])
    return direcciones
def enviar_mensajes(direcciones):
    mensajes = []
    for i in range(len(direcciones)-1, -1, -1):
        mensaje = f"Estimado/a,\n\nEste es un mensaje de prueba enviado a {direcciones[i]}.\n\nGracias,\nTu nombre"
        mensajes.append(mensaje)
        print(mensaje)
    return mensajes
def guardar_mensajes(mensajes):
    with open('mensajes.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Mensaje'])
        for mensaje in mensajes:
            writer.writerow([mensaje])
direcciones = obtener_direcciones()
mensajes = enviar_mensajes(direcciones)
guardar_mensajes(mensajes)