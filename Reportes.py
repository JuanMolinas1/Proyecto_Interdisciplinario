# Librerias
import mysql.connector
from mysql.connector import errorcode
import datetime
from datetime import date
import heapq
import json

# Variables Globales
# Para la conexion SQL
cursor = None
cnx = None

# Conectar a la Base de Datos
def Conectar_SQL():
    global cnx, cursor
    cnx = mysql.connector.connect(
        user = 'root',
        password = '',
        host = 'localhost',
        database = 'hotel'
    )
    cursor = cnx.cursor(dictionary=True)
    print("Conexión establecida")

Conectar_SQL()

def InnerJoin(consulta):
    cursor.execute(consulta)
    return cursor.fetchall()

Registro_Servicio_Demandado = InnerJoin(
    "select Servicios.tipo as Tipo_Servicio, count(Servicios_Reservas.servicio) as Veces_Contratado " \
    "from Servicios_Reservas " \
    "join Servicios on Servicios_Reservas.servicio = Servicios.id_servicio " \
    "group by Servicios.tipo " \
    "order by Veces_Contratado desc " \
    "limit 1; "
)

Ocupacion_Temporada = InnerJoin(
    "select " \
	"year(fecha_entrada) AS año, " \
    "case " \
		"when month(fecha_entrada) between 1 and 3 then 'Temporada 1 (Enero - Marzo)' " \
		"when month(fecha_entrada) between 4 and 6 then 'Temporada 2 (Abril - Junio)' " \
		"when month(fecha_entrada) between 7 and 9 then 'Temporada 3 (Julio - Septiembre)' " \
		"when month(fecha_entrada) between 10 and 12 then 'Temporada 4 (Octubre - Diciembre)' " \
	"end AS Temporada, " \
	"count(*) as Cantidad_Reservas " \
    "from Reservas " \
    "group by Año, Temporada " \
    "order BY Año, temporada; " \
     
)

nombre_archivo = "Servicio Mas Demandado.json"

with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
   json.dump(Registro_Servicio_Demandado, archivo, indent=4, ensure_ascii=False)


print(f"El Reporte '{nombre_archivo}' fue creado con éxito")

nombre_archivo = "Ocupacion Por Temporadax.json"

with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
   json.dump(Ocupacion_Temporada, archivo, indent=4, ensure_ascii=False)

print(f"El Reporte '{nombre_archivo}' fue creado con éxito")
