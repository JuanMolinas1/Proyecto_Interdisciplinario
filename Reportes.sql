-- Servicio mas demandado
select Servicios.tipo as Tipo_Servicio, count(Servicios_Reservas.servicio) as Veces_Contratado
from Servicios_Reservas
join Servicios on Servicios_Reservas.servicio = Servicios.id_servicio
group by Servicios.tipo
order by Veces_Contratado desc
limit 1;

