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

def InnerJoin_Hash():
    tabla = 'select Clientes.id_cliente as Identificador, Clientes.dni as DNI, Clientes.nombre as Nombre, count(Reservas.id_reserva) as Cant_Reservas ' \
    'from Reservas ' \
    'inner join Clientes on Reservas.cliente = Clientes.id_cliente' \
    'group by Clientes.id_cliente, Clientes.dni, Clientes.nombre' \
    'Having count(Reservas.id_reserva) >= 2; '
    cursor.execute(tabla)
    return cursor.fetchall()
