select
    Clientes.id_cliente as Id_Cliente,
    Clientes.nombre as Nombre_Cliente,
    Reservas.id_reserva as Id_Reservas,
    Habitaciones.id_habitacion as Id_habitacion,
    Habitaciones.zona as Zona,
    Servicios.tipo as Id_Servicios 
from
    Clientes
left join
    Reservas on Clientes.id_cliente = Reservas.cliente
left join
    Habitaciones on Reservas.habitacion = Habitaciones.id_habitacion
left join
    Servicios_Reservas on Reservas.id_reserva = Servicios_Reservas.reserva 
left join
    Servicios on Servicios_Reservas.servicio = Servicios.id_servicio
order by Id_Cliente asc;
