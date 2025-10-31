-- Servicio mas demandado
select Servicios.tipo as Tipo_Servicio, count(Servicios_Reservas.servicio) as Veces_Contratado
from Servicios_Reservas
join Servicios on Servicios_Reservas.servicio = Servicios.id_servicio
group by Servicios.tipo
order by Veces_Contratado desc
limit 1;



Pablo Cardozo
select
	year(fecha_entrada) AS año,
    case
		WHEN MONTH(fecha_entrada) BETWEEN 1 AND 3 THEN 'Temporada 1( Enero-Marzo)'
		WHEN MONTH(fecha_entrada) BETWEEN 4 AND 6 THEN 'Temporada 1( Abril-Junio)'
		WHEN MONTH(fecha_entrada) BETWEEN 7 AND 9 THEN 'Temporada 1( Julio-Septiembre)'
		WHEN MONTH(fecha_entrada) BETWEEN 10 AND 12 THEN 'Temporada 4( Octubre-Diciembre)'
	END AS Temporada,
	COUNT(*) as Cantidad_Reservas
From Reservas
group by Año, Temporada
ORDER BY Año, temporada;
     
