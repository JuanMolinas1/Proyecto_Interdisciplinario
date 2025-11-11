# Librerias
import os
import mysql.connector
#python -m pip install mysql-connector
from mysql.connector import errorcode
import datetime
from datetime import date
import heapq
import json


# Variables Globales
# Para la conexion SQL
cursor = None
cnx = None

# Las tablas
Tabla_Reservas = []
Tabla_sinHash = []
Tabla_Hash = []
Grafos = []
Monticulo = []
heap = []
Registro_Servicio_Demandado = []
Registro_Ocupacion_Temporada = []


# Conectar a la Base de Datos
def Conectar_SQL():
    global cnx, cursor
    try:
        cnx = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'hotel'
        )
        cursor = cnx.cursor(dictionary=True)
        print("Conexión establecida")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o contraseña incorrectos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe!")
        else:
            print(err)


# Crear las tablas con consultas SQL
def InnerJoin(consulta):
    cursor.execute(consulta)
    return cursor.fetchall()


# Crear las tablas usando las consultas de antes
def Crear_Tablas():
    global Tabla_Reservas, Tabla_sinHash, Tabla_Hash, Grafos, Monticulo, heap, Registro_Servicio_Demandado, Registro_Ocupacion_Temporada

    # Tabla de búsqueda binaria
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

    Grafos = InnerJoin(
        "select " \
        "Clientes.id_cliente as Id_Cliente, " \
        "Clientes.nombre as Nombre_Cliente, " 
        "Reservas.id_reserva as Id_Reserva, " 
        "Habitaciones.id_habitacion as Id_Habitacion, " \
        "Habitaciones.zona as Zona, " \
        "Servicios.tipo as Servicio " \
        "from Clientes " \
        "left join Reservas on Clientes.id_cliente = Reservas.cliente " \
        "left join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion " \
        "left join Servicios_Reservas on Reservas.id_reserva = Servicios_Reservas.reserva " \
        "left join Servicios on Servicios_Reservas.servicio = Servicios.id_servicio " \
        "order by Id_Cliente asc; " \
    )


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

    Registro_Servicio_Demandado = InnerJoin(
        "select Servicios.tipo as Tipo_Servicio, count(Servicios_Reservas.servicio) as Veces_Contratado "
        "from Servicios_Reservas "
        "join Servicios on Servicios_Reservas.servicio = Servicios.id_servicio "
        "group by Servicios.tipo "
        "order by Veces_Contratado desc "
        "limit 1; "
    )

    Registro_Ocupacion_Temporada = InnerJoin(
        "select "
        "year(fecha_entrada) AS Temporada, "
        "case "
        "when month(fecha_entrada) between 1 and 3 then 'Parte 1 (Enero - Marzo)' "
        "when month(fecha_entrada) between 4 and 6 then 'Parte 2 (Abril - Junio)' "
        "when month(fecha_entrada) between 7 and 9 then 'Parte 3 (Julio - Septiembre)' "
        "when month(fecha_entrada) between 10 and 12 then 'Parte 4 (Octubre - Diciembre)' "
        "end AS Parte, "
        "count(*) as Cantidad_Reservas "
        "from Reservas "
        "group by Temporada, Parte "
        "order BY Temporada, Parte; "
    )


# Impresion de Tablas con formato
def Imprimir_Tabla(tabla, titulo):
    if not tabla:
        print(f"{titulo} N/a")
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


# Punto 2.1 Tabla Ordenada para Busqueda Binaria
def Tabla_Reservas():
    Imprimir_Tabla(Tabla_Reservas, "Tabla Reservas")

# Punto 2.2 Tabla Hash para Clientes frecuentes (>= 2 Reservas)
def Mostrar_Hash():
    Imprimir_Tabla(Tabla_sinHash, "Tabla Sin Hash")
    Imprimir_Tabla(Tabla_Hash, "Tabla Hash")


#Punto 2.3 Grafos para Clientes con Reservas y Servicios
def Mostrar_Grafos():
    Imprimir_Tabla(Grafos, "Grafos")


# Punto 2.4 Montículo para Reserva con mayor prioridad
def Mostrar_Monticulo():
    if heap:
        _, _, _, _, _, cliente_top = heapq.heappop(heap)
        print("\n-- Reserva con mayor prioridad --")
        Monticulo_Top = []
        Monticulo_Top.append(cliente_top)
        Imprimir_Tabla(Monticulo_Top, "Cliente con Mayor Prioridad (Montículo)")
    else:
        print("No hay clientes")


# Punto 3.1 Insertar Reserva nueva
def Insertar_Reserva():
    print("\n-- Insertar Nueva Reserva --")
    while True:
        try:
            habitacion = int(input("habitacion: "))
            cliente = int(input("cliente: "))
            recepcionista = int(input("recepcionista: "))
            precio = int(input("precio: "))  
            cant_huespedes = int(input("cant_huespedes: "))
            break
        except ValueError:
            print("Ingrese los datos correctamente")

    print("Ingrese fecha de entrada:")
    while True:
        try:
            año = int(input("Año: "))
            mes = int(input("Mes: "))
            dia = int(input("Día: "))
            fecha_entrada = datetime.date(año, mes, dia)
            break
        except ValueError:
            print("Ingrese la fecha correctamente, (AAAA/M/D)")

    print("Ingrese fecha de salida:")
    while True:
        try:
            año = int(input("Año: "))
            mes = int(input("Mes: "))
            dia = int(input("Día: "))
            fecha_salida = datetime.date(año, mes, dia)
            break
        except ValueError:
            print("Ingrese la fecha correctamente (AAAA/M/D)")

    sql = "INSERT INTO Reservas (habitacion, cliente, recepcionista, precio, cant_huespedes, fecha_entrada, fecha_salida) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(sql,(habitacion, cliente, recepcionista, precio, cant_huespedes, fecha_entrada, fecha_salida))
    cnx.commit()
    print("Reserva insertada correctamente.")


# Punto 3.2 Busqueda Binaria para buscar reservas segun fecha de inicio y tipo de habitación
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
    encontro, medio = Busqueda_Binaria(Tabla_Reservas, fecha)
    if encontro:
        tipo = Consultar_Tipo()
        if Tabla_Reservas[medio]["tipo"] == tipo:
            Tabla_Encontrada = []
            Tabla_Encontrada.append(Tabla_Reservas[medio])
            Imprimir_Tabla(Tabla_Encontrada, "Reserva Encontrada")
        else:
            print("No se encontró una reserva con ese tipo.")
    else:
        print("No se encontró una reserva con esa fecha.")


# Ejercicio 3.3 Reportes JSON
def Generar_Reporte(nombre_archivo, tabla):
    ruta = f"archivos/{nombre_archivo}.json"
    with open(ruta, 'w', encoding='utf-8') as archivo:
        json.dump(tabla, archivo, indent=4, ensure_ascii=False)
    print(f"El Reporte {nombre_archivo} fue creado con éxito")
    return ruta


# Main
def main():
    Conectar_SQL()
    Crear_Tablas()
    while True:
        try:
            menu = int(input("\n\n== Hoteles Connecticut == \nIngrese que desea hacer:"
            "\n1. Crear Tabla Hash/Sin Hash"
            "\n2. Crear Grafos"
            "\n3. Crear Monticulo"
            "\n4. Crear Reservas"
            "\n5. Buscar Reservas"
            "\n6. Crear Reporte Servicio"
            "\n7. Crear Reporte Reserva"
            "\n -"))
            if menu == 1:
                Mostrar_Hash()
            elif menu == 2:
                Mostrar_Grafos()
            elif menu == 3:
                Mostrar_Monticulo()
            elif menu == 4:
                Insertar_Reserva()
            elif menu == 5:
                Busqueda()
            elif menu == 6:
                while True:
                    try:
                        Generar_Reporte("Servicio_Mas_Demandado", Registro_Servicio_Demandado)
                        break
                    except FileNotFoundError:
                        os.makedirs("archivos")
            elif menu == 7:
                while True:
                    try:
                        Generar_Reporte("Ocupacion_Por_Temporada", Registro_Ocupacion_Temporada)
                        break
                    except FileNotFoundError:
                        os.makedirs("archivos")
            elif menu== 0:
                break
        except ValueError:
            print("Ingrese un tipo de dato válido.")

main()
