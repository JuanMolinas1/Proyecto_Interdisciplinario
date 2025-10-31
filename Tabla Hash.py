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
    'inner join Clientes on Reservas.cliente = Clientes.id_cliente ' \
    'group by Clientes.id_cliente, Clientes.dni, Clientes.nombre ' \
    'Having count(Reservas.id_reserva) >= 2;'
    cursor.execute(tabla)
    return cursor.fetchall()

Tabla_sinHash = InnerJoin_Hash()
cant_registros = len(Tabla_sinHash)
Tabla_Hash = []

for fila in Tabla_sinHash:
    fila_hash = {}
    for llave, valor in fila.items():
        indice_hash = hash(valor) % cant_registros
        fila_hash[llave] = indice_hash
    Tabla_Hash.append(fila_hash)

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

Imprimir_Tabla(Tabla_sinHash, "Tabla Sin Hash")
Imprimir_Tabla(Tabla_Hash, "Tabla Hash")
