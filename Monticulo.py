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

Monticulo = []

print(Monticulo)

Monticulo = InnerJoin(
    'select Clientes.id_cliente, Clientes.nombre, Clientes.vip, Habitaciones.tipo as habitacion, Reservas.precio ' \
    'from Clientes ' \
    'inner join Reservas on Clientes.id_cliente = Reservas.cliente ' \
    'inner join Habitaciones on Reservas. habitacion = Habitaciones.id_habitacion;' \
    )

