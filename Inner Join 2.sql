-- Clientes con más de 3 reservas en el último año.
select Clientes.nombre, Clientes.apellido, count(Reservas.id_reserva) as cantidad_reservas
from Clientes
inner join Reservas on Clientes.id_cliente = Reservas.cliente
group by Clientes.id_cliente
having count(Reservas.id_reserva) > 3;
