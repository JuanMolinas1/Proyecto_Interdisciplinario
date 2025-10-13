SELECT c.nombre, c.apellido, COUNT(r.id_reserva) AS cantidad_reservas
FROM Clientes c
INNER JOIN Reservas r ON c.id_cliente = r.cliente
WHERE r.fecha_entrada >= CURDATE() - INTERVAL 1 YEAR
GROUP BY c.id_cliente
HAVING COUNT(r.id_reserva) > 3;
