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

def InnerJoin_Fechas():
    tabla = 'select Reservas.fecha_entrada ' \
    'from Reservas ' \
    'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion ' \
    'order by Reservas.fecha_entrada asc;'
    cursor.execute(tabla)
    return cursor.fetchall()

def InnerJoin_Tipos():
    tabla = 'select Habitaciones.tipo ' \
    'from Reservas ' \
    'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion ' \
    'order by Reservas.fecha_entrada asc;'
    cursor.execute(tabla)
    return cursor.fetchall()

def InnerJoin_Reservas():
    tabla = 'select Habitaciones.numero, Habitaciones.zona, Habitaciones.tipo, Reservas.fecha_entrada ' \
    'from Reservas ' \
    'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion ' \
    'order by Reservas.fecha_entrada asc;'
    cursor.execute(tabla)
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
            print("Buscador de Fechas")
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
            print("Busqueda de tipo")
            tipo = str(input("Ingrese el tipo de habitación buscado: ")).capitalize()
            if tipo != "Standard" or tipo != "Deluxe" or tipo != "Presidencial":
                print("Ingrese un tipo de habitación valido")
            else:
                return tipo
        except ValueError:
            print("Por favor ingrese un texto válido")

Tabla_Fecha = InnerJoin_Fechas()
Tabla_Tipo = InnerJoin_Tipos()
Tabla_Reservas = InnerJoin_Reservas()

try:   
    encontro, medio = Busqueda_Binaria(Tabla_Fecha, Consultar_Fecha())
except TypeError:
    encontro = False

if encontro == True:
    comparacion = (Tabla_Tipo, medio, Consultar_Tipo())
else:
    comparacion = False

if comparacion == True:
    print("\n-- Reserva Encontrada --")
    for llave, valor in Tabla_Reservas[medio].items():
        print(f"{llave.capitalize()}: {valor}")
else:
    print("No se encontro una reserva con sus especificaciones.")
