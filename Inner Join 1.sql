--Habitaciones disponibles en un rango de fechas.

select Habitaciones.numero as 'Numero_Habitacion', Habitaciones.tipo as 'Tipo', Habitaciones.capacidad as 'Capacidad_Max', Habitaciones.zona as 'Zona'
from Habitaciones
where Habitaciones.id_habitacion not in (
        select Reservas.habitacion
        from Reservas
        where Reservas.fecha_entrada < '2025-07-03 14:00:00' and Reservas.fecha_salida > '2025-08-03 14:00:00'
)
and Habitaciones.estado = 'Disponible'
order by Habitaciones.numero;
