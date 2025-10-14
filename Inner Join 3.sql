set lc_time_names = 'es_ES';

select monthname(Reservas.fecha_entrada) as mes, sum(Servicios.precio) as dinero_mes
from Reservas
inner join Servicios_Reservas on Reservas.id_reserva = Servicios_Reservas.reserva
inner join Servicios on Servicios.id_servicio = Servicios_Reservas.servicio
where year(Reservas.fecha_entrada) = 2024
group by month(Reservas.fecha_entrada)
order by month(Reservas.fecha_entrada)
limit 13;
