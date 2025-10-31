import mysql.connector
from mysql.connector import errorcode
import datetime
from datetime import date
import heapq

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

Monticulo = InnerJoin(
    'select Clientes.id_cliente, Clientes.nombre, Clientes.vip, Habitaciones.tipo as habitacion, Reservas.precio ' \
    'from Clientes ' \
    'inner join Reservas on Clientes.id_cliente = Reservas.cliente ' \
    'inner join Habitaciones on Reservas. habitacion = Habitaciones.id_habitacion;' \
    )

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

if heap:
    _, _, _, _, _, cliente_top = heapq.heappop(heap)
    print("\n-- Reserva con mayor prioridad --")
    for llave, valor in cliente_top.items():
        print(f"{llave.capitalize()}: {valor}")
else:
    print("No hay clientes")
