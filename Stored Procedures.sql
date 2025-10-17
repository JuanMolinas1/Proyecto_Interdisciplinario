use hotel;

DELIMITER //
-- Habitaciones disponibles en un rango de fechas.
create procedure Habitaciones_Disponibles()
begin
	select Habitaciones.numero as 'Numero_Habitacion', Habitaciones.tipo as 'Tipo', Habitaciones.capacidad as 'Capacidad_Max', Habitaciones.zona as 'Zona'
	from Habitaciones
	where Habitaciones.id_habitacion not in (
			select Reservas.habitacion
			from Reservas
			where Reservas.fecha_entrada > '2024-01-01 01:00:00' and Reservas.fecha_salida < '2024-02-01 23:00:00'
	)
	and Habitaciones.estado = 'Disponible'
	order by Habitaciones.numero;
end //
DELIMITER ; 

DELIMITER //
-- Clientes con más de 3 reservas en el último año.
create procedure Clientes_Habituales()
begin
	select Clientes.nombre as Nombre, Clientes.apellido as Apellido, count(Reservas.id_reserva) as Cantidad_reservas
	from Clientes
	inner join Reservas on Clientes.id_cliente = Reservas.cliente
	group by Clientes.id_cliente
	having count(Reservas.id_reserva) > 3;
end //
DELIMITER ;

DELIMITER //
-- Ingresos mensuales por servicios adicionales.
create procedure Servicio_Mes()
begin
	set lc_time_names = 'es_ES';

	select monthname(Reservas.fecha_entrada) as Meses, sum(Servicios.precio) as Dinero_mes
	from Reservas
	inner join Servicios_Reservas on Reservas.id_reserva = Servicios_Reservas.reserva
	inner join Servicios on Servicios.id_servicio = Servicios_Reservas.servicio
	where year(Reservas.fecha_entrada) = 2024
	group by month(Reservas.fecha_entrada)
	order by month(Reservas.fecha_entrada)
	limit 12;
end //
DELIMITER ;
