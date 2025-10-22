import mysql.connector
from mysql.connector import errorcode
import datetime
from datetime import date

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

def InnerJoin_Completo():
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
            return medio
        elif fecha_medio < fecha_busqueda:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def Consultar_Fecha():
    while True:
        try: 
            print("Buscador de Fechas: ")
            año = int(input("Ingrese el año: "))
            mes = int(input("Ingrese el mes: "))
            dia = int(input("Ingrese el día: "))
            fecha_busqueda = datetime.date(año, mes, dia)
            break
        except ValueError:
            print("Por favor ingrese una fecha valida")
    return fecha_busqueda

Tabla_Fecha = InnerJoin_Fechas()
print(Busqueda_Binaria(Tabla_Fecha, Consultar_Fecha()))
