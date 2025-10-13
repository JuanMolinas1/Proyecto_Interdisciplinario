select month(Reserva.fecha_entrada) as mes, sum(servicios.precio) as dinero_mes
from Reservas
inner join Reservas_Servicios on Reserva.id_reserva = servicios_reserva.id_reserva
inner join Servicios on Servicios.id_servicio = servicios_reserva
