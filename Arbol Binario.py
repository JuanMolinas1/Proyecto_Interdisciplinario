import mysql.connector
from datetime import date
from mysql.connector import errorcode

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

def InnerJoin_Fechas():
    Tabla_Fechas = 'select Reservas.fecha_entrada ' \
    'from Reservas ' \
    'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion ' \
    'order by Reservas.fecha_entrada asc;'
    cursor.execute(Tabla_Fechas)
    return cursor.fetchall()

def InnerJoin_Tipos():
    Tabla_Tipos = 'select Habitaciones.tipo ' \
    'from Reservas ' \
    'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion ' \
    'order by Reservas.fecha_entrada asc;'
    cursor.execute(Tabla_Tipos)
    return cursor.fetchall()

def InnerJoin_Completo():
    Tabla_Tipos = 'select Habitaciones.numero, Habitaciones.zona, Habitaciones.tipo, Reservas.fecha_entrada ' \
    'from Reservas ' \
    'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion ' \
    'order by Reservas.fecha_entrada asc;'
    cursor.execute(Tabla_Tipos)
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

def Consultar_Fecha

Tabla_Fecha = InnerJoin_Fechas()

Conectar_SQL()
