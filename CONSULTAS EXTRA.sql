--Empleados que trabajen en el sector de seguridad y entren antes de las 11-- 

SELECT Empleados.id_empleado
FROM Empleados 
INNER JOIN Turnos ON Empleados.id_empleado = Turnos.empleado 
WHERE Empleado.sector = 'seguridad' AND Turnos.horario_salida < '11:00:00'; 

-- Empleados que trabajen en el sector de seguridad y entren antes de las 11

select nombre, sector, sueldo
from Empleados
where sector = "seguridad" and sueldo > 2000
