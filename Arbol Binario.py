import mysql.connector
from mysql.connector import errorcode
import datetime
from datetime import date

#python -m pip install mysql-connector

cursor = None
cnx = None

def Conectar_SQL():
    global cnx, cursor
    cnx = mysql.connector.connect(
        user = 'root',
        password= '',
        host = 'localhost',
        database = 'hotel'
    )
    cursor = cnx.cursor(dictionary = True)
    print("Conexión establecida")

Conectar_SQL()

def InnerJoin(consulta):
    cursor.execute(consulta)
    return cursor.fetchall()

def Busqueda_Binaria(Tabla_Fecha, fecha_busqueda):
    inicio = 0
    fin = len(Tabla_Fecha) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        fecha_medio = Tabla_Fecha[medio]['fecha_entrada']
        if fecha_medio == fecha_busqueda:
            return True, medio
        elif fecha_medio < fecha_busqueda:
            inicio = medio + 1
        else:
            fin = medio - 1
    return False

def Consultar_Fecha():
    while True:
        try: 
            print("\nBuscador de Fechas")
            año = int(input("Ingrese el año: "))
            mes = int(input("Ingrese el mes: "))
            dia = int(input("Ingrese el día: "))
            fecha_busqueda = datetime.date(año, mes, dia)
            break
        except ValueError:
            print("Por favor ingrese una fecha valida")
    return fecha_busqueda

def Comparar_Tipo(Tabla_Tipo, medio, tipo):
    if Tabla_Tipo[medio]["tipo"] == tipo:
        return True
    else:
        return False

def Consultar_Tipo():
    while True:
        try:
            print("\nBusqueda de tipo")
            t = str(input("Ingrese el tipo de habitación buscado: "))
            tipo = t.capitalize()
            if tipo == "Standard" or tipo == "Deluxe" or tipo == "Presidencial":
                return tipo
            else:
                print("Ingrese un tipo de habitación valido")
        except ValueError:
            print("Por favor ingrese un texto válido")

Tabla_Fecha = []
Tabla_Tipo = []
Tabla_Reservas = []

def Crear_Arbol_Binario():
    global Tabla_Fecha, Tabla_Tipo, Tabla_Reservas
    Tabla_Fecha = InnerJoin(
        'select Reservas.fecha_entrada ' \
        'from Reservas ' \
        'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion ' \
        'order by Reservas.fecha_entrada asc;'
        )
    Tabla_Tipo = InnerJoin(
        'select Habitaciones.tipo ' \
        'from Reservas ' \
        'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion ' \
        'order by Reservas.fecha_entrada asc;'
        )
    Tabla_Reservas = InnerJoin(
        'select Habitaciones.numero, Habitaciones.zona, Habitaciones.tipo, Reservas.fecha_entrada ' \
        'from Reservas ' \
        'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion ' \
        'order by Reservas.fecha_entrada asc;'
        )

Crear_Arbol_Binario()

def Busqueda():
    try:
        encontro, medio = Busqueda_Binaria(Tabla_Fecha, Consultar_Fecha())
    except TypeError:
        encontro = False

    if encontro == True:
        comparacion = Comparar_Tipo(Tabla_Tipo, medio, Consultar_Tipo())
    else:
        comparacion = False

    if comparacion == True:
        print("\n-- Reserva Encontrada --")
        for llave, valor in Tabla_Reservas[medio].items():
            print(f"{llave.capitalize()}: {valor}")
    else:
        print("No se encontro una reserva con sus especificaciones.")

Busqueda()
