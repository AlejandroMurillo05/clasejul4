
import json

# Definir la estructura de datos
clientes = {}
tarjetas = {}

# Funciones de gestión de datos
def cargar_datos():
    try:
        with open('clientes.json', 'r') as file:
            global clientes
            clientes = json.load(file)
    except FileNotFoundError:
        print("No se encontró el archivo de clientes. Se creará uno nuevo.")

    try:
        with open('tarjetas.json', 'r') as file:
            global tarjetas
            tarjetas = json.load(file)
    except FileNotFoundError:
        print("No se encontró el archivo de tarjetas. Se creará uno nuevo.")

def guardar_datos():
    with open('clientes.json', 'w') as file:
        json.dump(clientes, file, indent=4)

    with open('tarjetas.json', 'w') as file:
        json.dump(tarjetas, file, indent=4)

# Funciones de gestión de tarjetas de crédito
def agregar_tarjeta():
    # Solicitar información al usuario
    tipo_tarjeta = input("Ingrese el tipo de tarjeta (Master Card, Visa, American Express): ")
    numero_tarjeta = input("Ingrese el número de la tarjeta de crédito: ")
    fecha_validez = input("Ingrese el mes y año de validez (MM/YY): ")
    codigo_verificacion = input("Ingrese el código de verificación (entre 100 y 999): ")
    id_cliente = input("Ingrese el ID del cliente dueño de la tarjeta: ")

    # Guardar la tarjeta en el diccionario de tarjetas
    tarjeta = {
        "tipo": tipo_tarjeta,
        "numero": numero_tarjeta,
        "validez": fecha_validez,
        "codigo": codigo_verificacion,
        "cliente": id_cliente
    }
    tarjetas[numero_tarjeta] = tarjeta

    print("Tarjeta de crédito agregada exitosamente.")

def modificar_tarjeta():
    numero_tarjeta = input("Ingrese el número de la tarjeta de crédito a modificar: ")

    if numero_tarjeta in tarjetas:
        # Solicitar nueva información al usuario
        tipo_tarjeta = input("Ingrese el nuevo tipo de tarjeta (Master Card, Visa, American Express): ")
        fecha_validez = input("Ingrese el nuevo mes y año de validez (MM/YY): ")
        codigo_verificacion = input("Ingrese el nuevo código de verificación (entre 100 y 999): ")
        id_cliente = input("Ingrese el nuevo ID del cliente dueño de la tarjeta: ")

        # Modificar los datos de la tarjeta
        tarjeta = tarjetas[numero_tarjeta]
        tarjeta["tipo"] = tipo_tarjeta
        tarjeta["validez"] = fecha_validez
        tarjeta["codigo"] = codigo_verificacion
        tarjeta["cliente"] = id_cliente

        print("Tarjeta de crédito modificada exitosamente.")
    else:
        print("El número de tarjeta ingresado no existe.")

def eliminar_tarjeta():
    numero_tarjeta = input("Ingrese el número de la tarjeta de crédito a eliminar: ")

    if numero_tarjeta in tarjetas:
        del tarjetas[numero_tarjeta]
        print("Tarjeta de crédito eliminada exitosamente.")
    else:
        print("El número de tarjeta ingresado no existe.")

def mostrar_tarjetas_cliente():
    id_cliente = input("Ingrese el ID del cliente: ")

    if id_cliente in clientes:
        print("Información del cliente:")
        print("Nombre: ", clientes[id_cliente]["nombre"])
        print("Cédula: ", clientes[id_cliente]["cedula"])
        print("Teléfono: ", clientes[id_cliente]["telefono"])

        tarjetas_cliente = [tarjeta for tarjeta in tarjetas.values() if tarjeta["cliente"] == id_cliente]

        print("Tarjetas de crédito registradas a su nombre:")
        for tarjeta in tarjetas_cliente:
            print("Tipo: ", tarjeta["tipo"])
            print("Número: ", tarjeta["numero"])
            print("Validez: ", tarjeta["validez"])
            print("Código: ", tarjeta["codigo"])
    else:
        print("El ID de cliente ingresado no existe.")

def mostrar_informacion_tarjeta():
    numero_tarjeta = input("Ingrese el número de la tarjeta de crédito: ")

    if numero_tarjeta in tarjetas:
        tarjeta = tarjetas[numero_tarjeta]
        id_cliente = tarjeta["cliente"]

        print("Información de la tarjeta de crédito:")
        print("Tipo: ", tarjeta["tipo"])
        print("Número: ", tarjeta["numero"])
        print("Validez: ", tarjeta["validez"])
        print("Código: ", tarjeta["codigo"])

        if id_cliente in clientes:
            print("Información del cliente:")
            print("Nombre: ", clientes[id_cliente]["nombre"])
            print("Cédula: ", clientes[id_cliente]["cedula"])
            print("Teléfono: ", clientes[id_cliente]["telefono"])
    else:
        print("El número de tarjeta ingresado no existe.")

def listar_tarjetas():
    print("Listado de tarjetas de crédito:")
    for tarjeta in tarjetas.values():
        id_cliente = tarjeta["cliente"]
        if id_cliente in clientes:
            nombre_cliente = clientes[id_cliente]["nombre"]
        else:
            nombre_cliente = "Desconocido"

        print("Número: ", tarjeta["numero"])
        print("Validez: ", tarjeta["validez"])
        print("Tipo: ", tarjeta["tipo"])
        print("ID Cliente: ", id_cliente)
        print("Nombre Cliente: ", nombre_cliente)

def listar_clientes():
    print("Listado de clientes con tarjetas de crédito:")
    for cliente in clientes.values():
        print("Cédula: ", cliente["cedula"])
        print("Nombre: ", cliente["nombre"])
        print("Teléfono: ", cliente["telefono"])

def contar_tarjetas_tipo():
    tipo_tarjeta = input("Ingrese el tipo de tarjeta (Master Card, Visa, American Express): ")

    contador = 0
    for tarjeta in tarjetas.values():
        if tarjeta["tipo"] == tipo_tarjeta:
            contador += 1

    print("Cantidad de tarjetas de tipo", tipo_tarjeta, ":", contador)

# Función principal del programa
def main():
    cargar_datos()

    while True:
        print("Bienvenido al sistema de gestión de tarjetas de crédito")
        print("1. Agregar tarjeta de crédito")
        print("2. Modificar tarjeta de crédito")
        print("3. Eliminar tarjeta de crédito")
        print("4. Mostrar tarjetas de crédito de un cliente")
        print("5. Mostrar información de una tarjeta de crédito")
        print("6. Listar tarjetas de crédito")
        print("7. Listar clientes con tarjetas de crédito")
        print("8. Contar tarjetas de cierto tipo")
        print("9. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            agregar_tarjeta()
        elif opcion == "2":
            modificar_tarjeta()
        elif opcion == "3":
            eliminar_tarjeta()
        elif opcion == "4":
            mostrar_tarjetas_cliente()
        elif opcion == "5":
            mostrar_informacion_tarjeta()
        elif opcion == "6":
            listar_tarjetas()
        elif opcion == "7":
            listar_clientes()
        elif opcion == "8":
            contar_tarjetas_tipo()
        elif opcion == "9":
            guardar_datos()
            print("hasta luego")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()