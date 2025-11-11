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
- Participante del proyecto

### Descripción

La base de datos del hotel está diseñada para almacenar y organizar la información de servicios, empleados, clientes y otros elementos clave del sistema.

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

---

# Manual de instalación y uso

1. Descargar el archivo `Proyecto.rar`.

2. Descomprimir el archivo en cualquier carpeta.

3. Ejecutar XAMPP e iniciar los servicios Apache y MySQL.

4. Abrir MySQL Workbench y crear una conexión con cualquier nombre.

5. Ir a Data Import, seleccionar la opción "Import from self-contained file" y elegir dentro de la carpeta del proyecto el archivo `hotel.sql`.

6. Encender la base de datos.

7. Abrir el archivo de Python del proyecto e instalar la librería necesaria ejecutando en la terminal:

   ```bash
   python -m pip install mysql-connector
   ```

8. Ejecutar el archivo de Python y comenzar a usar el programa.
