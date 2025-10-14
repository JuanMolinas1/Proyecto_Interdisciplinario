set lc_time_names = 'es_ES';

select monthname(Reserva.fecha_entrada) as mes, sum(Servicios.precio) as dinero_mes
from Reservas
inner join Reservas_Servicios on Reserva.id_reserva = Servicios_Reserva.id_reserva
inner join Servicios on Servicios.id_servicio = Servicios_Reserva.id_servicio
where year(Reservas.fecha_entrada) = 2024
group by month(Reservas.fecha_entrada)
order by month(Reservas.fecha_entrada);
