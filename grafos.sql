SELECT
    C.id_cliente AS Id_Cliente,
    C.nombre AS Nombre_Cliente,
    R.id_reserva AS Id_Reservas,
    H.id_habitacion AS Id_habitacion,
    H.zona AS Zona,
    S.tipo AS ID_Servicios 
FROM
    Clientes C
left JOIN
    Reservas R ON C.id_cliente = R.cliente
left JOIN
    Habitaciones H ON R.habitacion = H.id_habitacion
LEFT JOIN
    Servicios_Reservas SR ON R.id_reserva = SR.reserva 
left JOIN
    Servicios S ON SR.servicio = S.id_servicio
order by Id_Cliente asc;
