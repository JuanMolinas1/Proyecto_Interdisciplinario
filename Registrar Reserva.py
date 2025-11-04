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

def InnerJoin(consulta):
    cursor.execute(consulta)
    return cursor.fetchall()

TablaHola = InnerJoin(
    "select * " \
    "from Reservas;"
)
print(TablaHola)
print("\n")
def ConsultaInsertar(habitacion, cliente, recepcionista, precio, cant_huespedes, fecha_entrada, fecha_salida):
    sql = "INSERT INTO Reservas (habitacion, cliente, recepcionista, precio, cant_huespedes, fecha_entrada, fecha_salida) VALUES ( %s, %s, %s, %s ,%s, %s, %s);"
    cursor.execute(sql,(habitacion, cliente, recepcionista, precio, cant_huespedes, fecha_entrada, fecha_salida))
    cnx.commit()
    return cursor.lastrowid

habitacion     =int(input("habitacion:     ")) 
cliente        =int(input("cliente:        ")) 
recepcionista  =int(input("recepcionista:  ")) 
precio         =int(input("precio:         "))  
cant_huespedes =int(input("cant_huespedes: "))

print("ingrese cuando entro:")
año = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el día: "))
fecha_entrada = datetime.date(año, mes, dia)
print("ingrese cuando salio:")
año = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el día: "))
fecha_salida = datetime.date(año, mes, dia)


    
ConsultaInsertar(habitacion, cliente, recepcionista, precio, cant_huespedes, fecha_entrada, fecha_salida)

TablaHola = InnerJoin(
    "select * from Reservas;"
)
print(TablaHola)
