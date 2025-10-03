SELECT nombre AS recepcionista, descripcion AS turno
FROM Recepcionistas 
INNER JOIN Turnos  ON turno = id_turno;

SELECT nombre AS cliente, descripcion AS servicio, precio
FROM Servicios_Reservas 
INNER JOIN Clientes ON cliente = id_cliente
INNER JOIN Servicios  ON servicio = id_servicio;

SELECT id_reserva, nombre AS cliente, nombre AS recepcionista,precio
FROM reservas
INNER JOIN Clientes on cliente = id_cliente

SELECT  id_reserva, nombre AS cliente, nombre AS recepcionista, precio
FROM Reservas 
INNER JOIN Clientes  ON  cliente = id_cliente
INNER JOIN Recepcionistas  ON recepcionista = id_recepcionista

SELECT nombre AS recepcionista, descripcion AS turno
FROM Recepcionistas
INNER JOIN Turnos ON turno =  id_turno

 -- La tabla recepcionista no existe, existe la tabla empleados y en emplados pueden ser de diferentes tipos, entre ellos recepcionista.
