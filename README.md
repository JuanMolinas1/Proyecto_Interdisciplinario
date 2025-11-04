# Proyecto_Interdisciplinario
## Ciclo Lectivo: 2025
## Curso y División: 4° 2°
## Docentes:
  - Federico Leonel Bouzon
  - Sofia Marmol
## Integrantes:
  - Pablo Cardozo
  - Gonzalo Delgado
  - Santiago Goldfarb
  - Juan Molinas
## Proyecto Elegido: `Sistema de Reservas para Hotel`

## Consiga:
### Contexto
Un hotel de la ciudad necesita un sistema para gestionar reservas de
habitaciones, clientes y servicios adicionales (SPA, restaurante, etc.). El
sistema debe combinar estructuras de datos avanzadas para optimizar
búsquedas y una base de datos relacional para almacenar información
persistente.
### Objetivos
1. Diseñar una base de datos normalizada (hasta 3FN) con tablas para
habitaciones, clientes, reservas y servicios.
2. Implementar estructuras de datos en memoria:
    - Árbol B+: Para búsqueda rápida de habitaciones disponibles por
fecha y tipo.
    - Tabla hash: Para acceder a clientes frecuentes por DNI en O(1).
    - Grafos: Modelar relaciones entre servicios (ej: cliente que reserva
habitación + SPA).
    - Montículo (heap): Priorizar reservas según tipo (ej: suites
premium primero).
3. Conectar ambas partes:
    - Sincronizar datos entre estructuras y BD con operaciones CRUD.
    - Optimizar consultas SQL con índices y joins.

### Requisitos Mínimos
### 1. Base de Datos (SQL)
#### Tablas:
  - Habitaciones (ID, tipo, precio, capacidad, estado).
  - Clientes (ID, nombre, DNI, teléfono, historial_reservas).
  - Reservas (ID, ID_Habitación, ID_Cliente, fecha_entrada, fecha_salida).
  - Servicios (ID, nombre, precio, ID_Reserva).
#### Relaciones:
  - Claves primarias/foráneas entre reservas, habitaciones y clientes.
#### Consultas complejas:
  - Habitaciones disponibles en un rango de fechas.
  - Clientes con más de 3 reservas en el último año.
  - Ingresos mensuales por servicios adicionales.

### 2. Estructuras de Datos (Código)
  - Árbol B+: Indexar habitaciones por fecha y tipo para búsqueda eficiente.
  - Tabla hash: Almacenar clientes frecuentes (key: DNI, value: Cliente).
  - Grafos: Mostrar servicios contratados junto a reservas (ej: "Cliente X → Habitación 101 → SPA").
  - Montículo: Priorizar reservas de suites o clientes VIP.

### 3. Integración
#### Lenguaje: Python + MySQL.
#### Funcionalidades:
  - Registrar reserva (actualizar BD y árbol B+).
  - Buscar habitaciones disponibles (árbol B+ + consulta SQL con fechas).
  - Generar reportes:
    - "Ocupación por temporada" (SQL + código).
    - "Servicios más demandados" (SQL + código).

### Entregables
  1. Repositorio GitHub con:
    - Código fuente (src/).
    - Scripts SQL (database/create_tables.sql).
    - Documentación (docs/):
    - Enunciado.md (este archivo).
    - Diagrama DER (DER.png).
    - Manual de usuario (ManualUsuario.md).

  2. Presentación Oral:
    - Demo del sistema (5-10 min).
    - Explicación técnica: cómo se integraron las estructuras y BD.
  3. Carpeta de campo con:
    - Investigaciones.
    - Implementaciones de código.
    - Descripción de lo realizado de forma diaria (Tener en cuenta que toda imagen debe tener un alto máximo de media carilla).
    - Formato APA.
