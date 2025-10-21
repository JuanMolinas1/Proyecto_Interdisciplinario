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
    Tabla_Fechas = 'select Reservas.fecha_entrada' \
    'from Reservas' \
    'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion' \
    'order by Reservas.fecha_entrada asc;'
    cursor.execute(Tabla_Fechas)
    return cursor.fetchall()

def InnerJoin_Tipos():
    Tabla_Tipos = 'select Habitaciones.tipo' \
    'from Reservas' \
    'inner join Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion' \
    'order by Reservas.fecha_entrada asc;'
    cursor.execute(Tabla_Tipos)
    return cursor.fetchall()
Conectar_SQL()
print(InnerJoin_Fechas)
print(InnerJoin_Tipos)
