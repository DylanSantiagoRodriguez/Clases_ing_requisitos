class Empleado:
    def __init__(self, nombre, edad, sueldo_bruto):
        self.nombre = nombre
        self.edad = edad
        self.sueldo_bruto = sueldo_bruto

class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria, subordinados=None):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = subordinados if subordinados is not None else []

class Cliente:
    def __init__(self, nombre, edad, telefono_contacto):
        self.nombre = nombre
        self.edad = edad
        self.telefono_contacto = telefono_contacto

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []

    def contratar_empleado(self, empleado):
        self.empleados.append(empleado)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_empleados(self):
        print("\nEmpleados de la empresa", self.nombre)
        for empleado in self.empleados:
            print(f"Nombre: {empleado.nombre}, Edad: {empleado.edad}, Sueldo Bruto: {empleado.sueldo_bruto}")

    def mostrar_clientes(self):
        print("\nClientes de la empresa", self.nombre)
        for cliente in self.clientes:
            print(f"Nombre: {cliente.nombre}, Edad: {cliente.edad}, Teléfono de Contacto: {cliente.telefono_contacto}")

def crear_empresa():
    nombre_empresa = input("Ingrese el nombre de la empresa: ")
    empresa = Empresa(nombre_empresa)
    empresas.append(empresa)
    print(f"La empresa '{nombre_empresa}' ha sido creada.")

def crear_empleado():
    nombre = input("Nombre del empleado: ")
    edad = int(input("Edad del empleado: "))
    sueldo_bruto = float(input("Sueldo bruto del empleado: "))
    return Empleado(nombre, edad, sueldo_bruto)

def crear_directivo():
    nombre = input("Nombre del directivo: ")
    edad = int(input("Edad del directivo: "))
    sueldo_bruto = float(input("Sueldo bruto del directivo: "))
    categoria = input("Categoría del directivo: ")
    subordinados = []
    while True:
        subordinado = input("Nombre del subordinado (o dejar en blanco para terminar): ")
        if not subordinado:
            break
        subordinados.append(subordinado)
    return Directivo(nombre, edad, sueldo_bruto, categoria, subordinados)

def crear_cliente():
    nombre = input("Nombre del cliente: ")
    edad = int(input("Edad del cliente: "))
    telefono_contacto = input("Teléfono de contacto del cliente: ")
    return Cliente(nombre, edad, telefono_contacto)

empresas = []

while True:
    print("\n1. Crear Empresa")
    print("2. Añadir Empleado")
    print("3. Añadir Directivo")
    print("4. Añadir Cliente")
    print("5. Mostrar Datos")
    print("6. Salir")
    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        crear_empresa()
    elif opcion == '2':
        nombre_empresa = input("Ingrese el nombre de la empresa donde se añadirá el empleado: ")
        empresa_encontrada = None
        for empresa in empresas:
            if empresa.nombre == nombre_empresa:
                empresa_encontrada = empresa
                break
        if empresa_encontrada:
            empleado = crear_empleado()
            empresa_encontrada.contratar_empleado(empleado)
            print(f"El empleado '{empleado.nombre}' ha sido contratado en la empresa '{nombre_empresa}'.")
        else:
            print(f"No se encontró ninguna empresa con el nombre '{nombre_empresa}'.")
    elif opcion == '3':
        nombre_empresa = input("Ingrese el nombre de la empresa donde se añadirá el directivo: ")
        empresa_encontrada = None
        for empresa in empresas:
            if empresa.nombre == nombre_empresa:
                empresa_encontrada = empresa
                break
        if empresa_encontrada:
            directivo = crear_directivo()
            empresa_encontrada.contratar_empleado(directivo)
            print(f"El directivo '{directivo.nombre}' ha sido contratado en la empresa '{nombre_empresa}'.")
        else:
            print(f"No se encontró ninguna empresa con el nombre '{nombre_empresa}'.")
    elif opcion == '4':
        nombre_empresa = input("Ingrese el nombre de la empresa donde se añadirá el cliente: ")
        empresa_encontrada = None
        for empresa in empresas:
            if empresa.nombre == nombre_empresa:
                empresa_encontrada = empresa
                break
        if empresa_encontrada:
            cliente = crear_cliente()
            empresa_encontrada.agregar_cliente(cliente)
            print(f"El cliente '{cliente.nombre}' ha sido agregado a la empresa '{nombre_empresa}'.")
        else:
            print(f"No se encontró ninguna empresa con el nombre '{nombre_empresa}'.")
    elif opcion == '5':
        for empresa in empresas:
            empresa.mostrar_empleados()
            empresa.mostrar_clientes()
    elif opcion == '6':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
