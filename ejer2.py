class Cliente:
    def __init__(self, dni, nombre, direccion, telefono, codigo):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.codigo = codigo
        self.aval = None

class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

class Reserva:
    def __init__(self, cliente, coches, fecha_inicio, fecha_fin, precio_alquiler, litros_gasolina, entregado):
        self.cliente = cliente
        self.coches = coches
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_alquiler = precio_alquiler
        self.litros_gasolina = litros_gasolina
        self.entregado = entregado
        self.precio_total = len(coches) * precio_alquiler

class Agencia:
    def __init__(self, nombre):
        self.nombre = nombre

def crear_cliente():
    dni = input("Ingrese el DNI del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    codigo = input("Ingrese el código único del cliente: ")
    return Cliente(dni, nombre, direccion, telefono, codigo)

def crear_reserva(cliente, coches):
    fecha_inicio = input("Ingrese la fecha de inicio de la reserva (formato YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin de la reserva (formato YYYY-MM-DD): ")
    precio_alquiler = float(input("Ingrese el precio de alquiler por día: "))
    litros_gasolina = float(input("Ingrese los litros de gasolina en el depósito: "))
    entregado = input("¿El coche ha sido entregado? (Sí/No): ").lower() == 'si'
    return Reserva(cliente, coches, fecha_inicio, fecha_fin, precio_alquiler, litros_gasolina, entregado)

coche1 = Coche("ABC123", "Toyota", "Rojo", "Corolla", "Garaje 1")
coche2 = Coche("DEF456", "Honda", "Azul", "Civic", "Garaje 2")

agencia1 = Agencia("Agencia A")

cliente1 = crear_cliente()

aval_dni = input("Ingrese el DNI del aval (o deje en blanco si no tiene aval): ")
cliente1.aval = None

if aval_dni:
    aval_cliente = crear_cliente()
    cliente1.aval = aval_cliente

reserva1 = crear_reserva(cliente1, [coche1, coche2])

print("\nInformación de la Reserva:")
print(f"Cliente: {reserva1.cliente.nombre}")
print(f"Fecha de Inicio: {reserva1.fecha_inicio}")
print(f"Fecha de Fin: {reserva1.fecha_fin}")
print(f"Precio Total: {reserva1.precio_total} EUR")
print(f"Coches Alquilados:")
for coche in reserva1.coches:
    print(f"Matrícula: {coche.matricula}, Modelo: {coche.modelo}, Marca: {coche.marca}")

print("\nInformación del Cliente:")
print(f"DNI: {cliente1.dni}")
print(f"Nombre: {cliente1.nombre}")
print(f"Dirección: {cliente1.direccion}")
print(f"Télefono: {cliente1.telefono}")
print(f"Código Único: {cliente1.codigo}")
print(f"Aval: {cliente1.aval.nombre if cliente1.aval else 'Ninguno'}")
