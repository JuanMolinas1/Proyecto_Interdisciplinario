# Informe del Proyecto

## Proyecto N°3: Registros de Hotel

### Integrantes del grupo

**Juan Molinas**
- Líder de grupo
- Enfocado en la corrección de errores
- Diseño y formato en Python

**Gonzalo Delgado**
- Programador SQL
- Encargado de la base de datos SQL
- Corrección de errores de la base de datos
- Participación en la creación de consultas Python/SQL

**Santiago Goldfarb**
- Asistente SQL y Python
- Apoyo en la base de datos junto a Gonzalo
- Resolución de dudas técnicas
- Asistencia en consultas y otros trabajos en Python

**Pablo Cardozo**
- Organización del trello
- Consultas para los reportes
- Ayuda en la creación del logo
- Creación del menú de selección en Python

### Descripción

La base de datos del hotel está diseñada para almacenar y organizar la información de servicios, empleados, clientes y otros elementos clave del sistema.
Este sistema está pensado para los recepcionistas, no para los clientes

### Características del proyecto

* Organización rápida de clientes, habitaciones y otros datos.
* Reservas en tiempo real de habitaciones.
* Registro del dinero generado.
* Organización de sueldos.
* Creación de archivos `.json` para consultas.
* Información sobre habitaciones y disponibilidad según fechas.
* Administración de horarios, sueldos y otros datos de trabajadores.
* Identificación de clientes con privilegios (VIP) y zonas especiales (Deluxe, Presidencial, etc).

### Requisitos del proyecto

* Librerías: `json`, `heapq`, `datetime`, `mysql.connector`.
* Compilador o entorno: Visual Studio, PyCharm, etc.
* XAMPP.
* MySQL Workbench 8.0 CE.

### Contenido de `Proyecto.rar`

* Contiene el archivo `hotel.sql`
* Contiene el archivo `main.py`
* Contiene la carpeta `/logo` con el png `Logo Hotel.png`

---

# Manual de Usuario

1. Descargar el archivo `Proyecto.rar`.
2. Descomprimir el archivo en cualquier carpeta.
3. Ejecutar XAMPP e iniciar los servicios Apache y MySQL.
4. Abrir MySQL Workbench y crear una conexión con cualquier nombre.
5. Abrir la conexión
6. Ir a File/Open SQL Script y elegir dentro de la carpeta del proyecto el archivo `hotel.sql`.
7. Encender la base de datos.
8. Abrir cmd y ejecutar la siguiente línea de código:

   ```bash
   python -m pip install mysql-connector
   ```

9. Abrir la carpeta de Proyecto con Visual Studio
10. Ejecutar el archivo de Python y comenzar a usar el programa.
