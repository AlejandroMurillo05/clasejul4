

import json

class TarjetaDeCredito:
    def __init__(self, tipo, numero, mes_valido, anio_valido, codigo_verificacion, id_cliente):
        self.tipo = tipo
        self.numero = numero
        self.mes_valido = mes_valido
        self.anio_valido = anio_valido
        self.codigo_verificacion = codigo_verificacion
        self.id_cliente = id_cliente

class Cliente:
    def __init__(self, nombre, cedula, telefono, sexo):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.sexo = sexo

class Banco:
    def __init__(self):
        self.tarjetas = []
        self.clientes = []

    def cargar_datos(self):
        try:
            with open('datos.json') as file:
                data = json.load(file)
                self.tarjetas = [TarjetaDeCredito(**t) for t in data['tarjetas']]
                self.clientes = [Cliente(**c) for c in data['clientes']]
        except FileNotFoundError:
            pass

    def guardar_datos(self):
        data = {
            'tarjetas': [vars(t) for t in self.tarjetas],
            'clientes': [vars(c) for c in self.clientes]
        }
        with open('datos.json', 'w') as file:
            json.dump(data, file)

    def agregar_tarjeta(self, tarjeta):
        self.tarjetas.append(tarjeta)

    def modificar_tarjeta(self, numero, tarjeta_nueva):
        for i, tarjeta in enumerate(self.tarjetas):
            if tarjeta.numero == numero:
                self.tarjetas[i] = tarjeta_nueva
                break

    def eliminar_tarjeta(self, numero):
        self.tarjetas = [tarjeta for tarjeta in self.tarjetas if tarjeta.numero != numero]

    def obtener_tarjetas_cliente(self, id_cliente):
        return [tarjeta for tarjeta in self.tarjetas if tarjeta.id_cliente == id_cliente]

    def obtener_informacion_tarjeta(self, numero):
        for tarjeta in self.tarjetas:
            if tarjeta.numero == numero:
                cliente = self.obtener_cliente(tarjeta.id_cliente)
                return tarjeta, cliente
        return None, None

    def obtener_listado_tarjetas(self):
        listado = []
        for tarjeta in self.tarjetas:
            cliente = self.obtener_cliente(tarjeta.id_cliente)
            listado.append({
                'numero': tarjeta.numero,
                'fecha_vencimiento': f"{tarjeta.mes_valido}/{tarjeta.anio_valido}",
                'tipo': tarjeta.tipo,
                'id_cliente': tarjeta.id_cliente,
                'nombre_cliente': cliente.nombre
            })
        return listado

    def obtener_listado_clientes(self):
        return [{
            'cedula': cliente.cedula,
            'nombre': cliente.nombre,
            'telefono': cliente.telefono
        } for cliente in self.clientes]

    def obtener_cantidad_tarjetas_tipo(self, tipo):
        count = 0
        for tarjeta in self.tarjetas:
            if tarjeta.tipo == tipo:
                count += 1
        return count

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def modificar_cliente(self, cedula, cliente_nuevo):
        for i, cliente in enumerate(self.clientes):
            if cliente.cedula == cedula:
                self.clientes[i] = cliente_nuevo
                break

    def eliminar_cliente(self, cedula):
        self.clientes = [cliente for cliente in self.clientes if cliente.cedula != cedula]

    def obtener_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.cedula == id_cliente:
                return cliente
        return None

def mostrar_menu():
    print("\n----- Menú -----\n")
    print("1. Añadir tarjeta de crédito")
    print("2. Modificar tarjeta de crédito")
    print("3. Eliminar tarjeta de crédito")
    print("4. Informe: Tarjetas de crédito de un cliente")
    print("5. Informe: Información de una tarjeta de crédito")
    print("6. Informe: Listado de tarjetas de crédito")
    print("7. Informe: Listado de clientes con tarjetas de crédito")
    print("8. Informe: Cantidad de tarjetas de cierto tipo")
    print("0. Salir")

def main():
    banco = Banco()
    banco.cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            tipo = input("Tipo de tarjeta (Master Card, Visa, American Express): ")
            numero = input("Número de tarjeta de crédito: ")
            mes_valido = input("Mes de validez: ")
            anio_valido = input("Año de validez: ")
            codigo_verificacion = input("Código de verificación (3 dígitos): ")
            id_cliente = input("ID del cliente dueño de la tarjeta: ")

            tarjeta = TarjetaDeCredito(tipo, numero, mes_valido, anio_valido, codigo_verificacion, id_cliente)
            banco.agregar_tarjeta(tarjeta)
            banco.guardar_datos()
            print("Tarjeta de crédito añadida exitosamente.")

        elif opcion == '2':
            numero = input("Ingrese el número de tarjeta de crédito a modificar: ")
            tarjeta_actual = None

            for tarjeta in banco.tarjetas:
                if tarjeta.numero == numero:
                    tarjeta_actual = tarjeta
                    break

            if tarjeta_actual:
                tipo = input(f"Nuevo tipo de tarjeta ({tarjeta_actual.tipo}): ")
                numero = input(f"Nuevo número de tarjeta de crédito ({tarjeta_actual.numero}): ")
                mes_valido = input(f"Nuevo mes de validez ({tarjeta_actual.mes_valido}): ")
                anio_valido = input(f"Nuevo año de validez ({tarjeta_actual.anio_valido}): ")
                codigo_verificacion = input(f"Nuevo código de verificación ({tarjeta_actual.codigo_verificacion}): ")
                id_cliente = input(f"Nuevo ID del cliente dueño de la tarjeta ({tarjeta_actual.id_cliente}): ")

                tarjeta_nueva = TarjetaDeCredito(
                    tipo or tarjeta_actual.tipo,
                    numero or tarjeta_actual.numero,
                    mes_valido or tarjeta_actual.mes_valido,
                    anio_valido or tarjeta_actual.anio_valido,
                    codigo_verificacion or tarjeta_actual.codigo_verificacion,
                    id_cliente or tarjeta_actual.id_cliente
                )

                banco.modificar_tarjeta(numero, tarjeta_nueva)
                banco.guardar_datos()
                print("Tarjeta de crédito modificada exitosamente.")
            else:
                print("La tarjeta de crédito no existe.")

        elif opcion == '3':
            numero = input("Ingrese el número de tarjeta de crédito a eliminar: ")
            banco.eliminar_tarjeta(numero)
            banco.guardar_datos()
            print("Tarjeta de crédito eliminada exitosamente.")

        elif opcion == '4':
            id_cliente = input("Ingrese el ID del cliente: ")
            tarjetas_cliente = banco.obtener_tarjetas_cliente(id_cliente)

            if tarjetas_cliente:
                cliente = banco.obtener_cliente(id_cliente)
                print(f"\nInformación de las tarjetas de crédito de {cliente.nombre}:")
                for tarjeta in tarjetas_cliente:
                    print(f"\nTipo: {tarjeta.tipo}")
                    print(f"Número: {tarjeta.numero}")
                    print(f"Mes y año de validez: {tarjeta.mes_valido}/{tarjeta.anio_valido}")
                    print(f"Código de verificación: {tarjeta.codigo_verificacion}")
            else:
                print("El cliente no tiene tarjetas de crédito registradas.")

        elif opcion == '5':
            numero = input("Ingrese el número de tarjeta de crédito: ")
            tarjeta, cliente = banco.obtener_informacion_tarjeta(numero)

            if tarjeta and cliente:
                print("\nInformación de la tarjeta de crédito:")
                print(f"\nTipo: {tarjeta.tipo}")
                print(f"Número: {tarjeta.numero}")
                print(f"Mes y año de validez: {tarjeta.mes_valido}/{tarjeta.anio_valido}")
                print(f"Código de verificación: {tarjeta.codigo_verificacion}")

                print("\nInformación del cliente:")
                print(f"\nID del cliente: {cliente.cedula}")
                print(f"Nombre: {cliente.nombre}")
                print(f"Número de teléfono: {cliente.telefono}")
                print(f"Sexo: {cliente.sexo}")
            else:
                print("La tarjeta de crédito no existe.")

        elif opcion == '6':
            tarjetas = banco.obtener_listado_tarjetas()
            print("\nListado de tarjetas de crédito:")
            for tarjeta in tarjetas:
                print(f"\nNúmero: {tarjeta['numero']}")
                print(f"Fecha de vencimiento: {tarjeta['fecha_vencimiento']}")
                print(f"Tipo: {tarjeta['tipo']}")
                print(f"ID del cliente: {tarjeta['id_cliente']}")
                print(f"Nombre del cliente: {tarjeta['nombre_cliente']}")

        elif opcion == '7':
            clientes = banco.obtener_listado_clientes()
            print("\nListado de clientes con tarjetas de crédito:")
            for cliente in clientes:
                print(f"\nCédula: {cliente['cedula']}")
                print(f"Nombre: {cliente['nombre']}")
                print(f"Teléfono: {cliente['telefono']}")

        elif opcion == '8':
            tipo = input("Ingrese el tipo de tarjeta (Master, Visa o American Express): ")
            cantidad = banco.obtener_cantidad_tarjetas_tipo(tipo)
            print(f"\nCantidad de tarjetas de tipo {tipo}: {cantidad}")

        elif opcion == '0':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == '__main__':
    main()