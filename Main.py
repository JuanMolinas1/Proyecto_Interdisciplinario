# Librerias
import mysql.connector
from mysql.connector import errorcode
import datetime
from datetime import date
import heapq


# Variables Globales
# Para la conexion SQL
cursor = None
cnx = None

# Las tablas
Tabla_Fecha = []
Tabla_Tipo = []
Tabla_Reservas = []
Tabla_sinHash = []
Tabla_Hash = []
Monticulo = []
heap = []


# Conectar a la Base de Datos
def Conectar_SQL():
    global cnx, cursor
    cnx = mysql.connector.connect(
        user = 'root',
        password = '',
        host = 'localhost',
        database = 'hotel'
    )
    cursor = cnx.cursor(dictionary=True)
    print("Conexión establecida")


# Crear las tablas con consultas SQL
def InnerJoin(consulta):
    cursor.execute(consulta)
    return cursor.fetchall()


# Crear las tablas usando las consultas de antes
def Crear_Tablas():
    global Tabla_Fecha, Tabla_Tipo, Tabla_Reservas, Tabla_sinHash, Tabla_Hash, Monticulo, heap

    # Tablas de búsqueda binaria
    Tabla_Fecha = InnerJoin(
        'select Reservas.fecha_entrada '
        'from Reservas '
        'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion '
        'order by Reservas.fecha_entrada asc;'
    )
    Tabla_Tipo = InnerJoin(
        'select Habitaciones.tipo '
        'from Reservas '
        'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion '
        'order by Reservas.fecha_entrada asc;'
    )
    Tabla_Reservas = InnerJoin(
        'select Habitaciones.numero, Habitaciones.zona, Habitaciones.tipo, Reservas.fecha_entrada '
        'from Reservas '
        'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion '
        'order by Reservas.fecha_entrada asc;'
    )


    # Tabla hash
    Tabla_sinHash = InnerJoin(
        'select Clientes.id_cliente as Identificador, Clientes.dni as DNI, Clientes.nombre as Nombre, '
        'count(Reservas.id_reserva) as Cant_Reservas '
        'from Reservas '
        'inner join Clientes on Reservas.cliente = Clientes.id_cliente '
        'group by Clientes.id_cliente, Clientes.dni, Clientes.nombre '
        'having count(Reservas.id_reserva) >= 2;'
    )

    # Conversión a Hash
    cant_registros = len(Tabla_sinHash)
    Tabla_Hash = []
    for fila in Tabla_sinHash:
        fila_hash = {llave: hash(valor) % cant_registros for llave, valor in fila.items()}
        Tabla_Hash.append(fila_hash)


    # Montículo
    Monticulo = InnerJoin(
        'select Clientes.id_cliente, Clientes.nombre, Clientes.vip, Habitaciones.tipo as habitacion, Reservas.precio '
        'from Clientes '
        'inner join Reservas on Clientes.id_cliente = Reservas.cliente '
        'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion;'
    )

    # Crear las Prioridades
    heap = [
        (
            -int(c["vip"]),
            -int(c["habitacion"].lower() == "presidencial"),
            -int(c["habitacion"].lower() == "suite"),
            -c["precio"],
            c["id_cliente"],
            c
        )
        for c in Monticulo
    ]

    heapq.heapify(heap)
    print("Tablas creadas correctamente.")


# Impresion de Tablas con formato
def Imprimir_Tabla(tabla, titulo):
    if not tabla:
        print(f"{titulo} vacía")
        return
    encabezados = list(tabla[0].keys())
    ancho_columnas = []
    for llave in encabezados:
        max_ancho = max(len(str(fila[llave])) for fila in tabla)
        max_ancho = max(max_ancho, len(llave))
        ancho_columnas.append(max_ancho)

    def Formatear_Fila(fila):
        return " | ".join(str(fila[llave]).ljust(ancho_columnas[i]) for i, llave in enumerate(encabezados))

    print(f"\n-- {titulo} --")
    print(Formatear_Fila({llave: llave for llave in encabezados}))
    print("-" * (sum(ancho_columnas) + 3 * (len(encabezados)-1)))
    for fila in tabla:
        print(Formatear_Fila(fila))


# Punto 2.1 Busqueda Binaria para buscar reservas segun fecha de inicio y tipo de habitación
# Busqueda Binaria para fecha pedida
def Busqueda_Binaria(tabla, fecha_busqueda):
    inicio, fin = 0, len(tabla) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        fecha_medio = tabla[medio]['fecha_entrada']
        if fecha_medio == fecha_busqueda:
            return True, medio
        elif fecha_medio < fecha_busqueda:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False, None

# Pedir fecha para buscar
def Consultar_Fecha():
    while True:
        try:
            print("\nBuscador de Fechas")
            año = int(input("Ingrese el año: "))
            mes = int(input("Ingrese el mes: "))
            dia = int(input("Ingrese el día: "))
            return datetime.date(año, mes, dia)
        except ValueError:
            print("Por favor ingrese una fecha válida")

# Pedir tipo para comparar
def Consultar_Tipo():
    while True:
        tipo = input("Ingrese el tipo de habitación buscado (Standard/Deluxe/Presidencial): ").capitalize()
        if tipo in ["Standard", "Deluxe", "Presidencial"]:
            return tipo
        print("Ingrese un tipo válido")

# Comparacion de todos los valores finales
def Busqueda():
    fecha = Consultar_Fecha()
    encontro, medio = Busqueda_Binaria(Tabla_Fecha, fecha)
    if encontro:
        tipo = Consultar_Tipo()
        if Tabla_Tipo[medio]["tipo"] == tipo:
            print("\n-- Reserva Encontrada --")
            for llave, valor in Tabla_Reservas[medio].items():
                print(f"{llave.capitalize()}: {valor}")
        else:
            print("No se encontró una reserva con ese tipo.")
    else:
        print("No se encontró una reserva con esa fecha.")


# Punto 2.2 Tabla Hash para Clientes frecuentes (>= 2 Reservas)
def Mostrar_Hash():
    Imprimir_Tabla(Tabla_sinHash, "Tabla Sin Hash")
    Imprimir_Tabla(Tabla_Hash, "Tabla Hash")


# Punto 2.4 Montículo para Reserva con mayor prioridad
def Mostrar_Monticulo():
    if heap:
        _, _, _, _, _, cliente_top = heapq.heappop(heap)
        print("\n-- Reserva con mayor prioridad --")
        for llave, valor in cliente_top.items():
            print(f"{llave.capitalize()}: {valor}")
    else:
        print("No hay clientes")


# Inicialización del Programa
def main():
    Conectar_SQL()
    Crear_Tablas()

    Busqueda()
    Mostrar_Hash()
    Mostrar_Monticulo()

main()
