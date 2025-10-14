--Habitaciones disponibles en un rango de fechas.
SELECT
    H.numero AS 'Numero_Habitacion',
    H.tipo AS 'Tipo',
    H.capacidad AS 'Capacidad_Max',
    H.zona
FROM
    Habitaciones H
WHERE
    H.id_habitacion NOT IN (
        -- Subconsulta: Encuentra los id_habitacion que *tienen* una reserva que CONFLICTÚA
        SELECT
            R.habitacion
        FROM
            Reservas R
        WHERE
            -- Condición de solapamiento de fechas:
            -- La reserva R comienza antes de que termine mi rango DESEADO
            R.fecha_entrada < '2025-11-05 12:00:00'
            -- Y la reserva R termina después de que empiece mi rango DESEADO
            AND R.fecha_salida > '2025-11-01 14:00:00'
    )
    AND H.estado = 'Disponible' -- Opcional: solo habitaciones con estado 'Disponible'
ORDER BY
    H.numero;
