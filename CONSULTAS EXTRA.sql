--Empleados que trabajen en el sector de seguridad y entren antes de las 11-- 

SELECT E.id_empleado
FROM Empleados E 
INNER JOIN Turnos T ON E.id_empleado = T.empleado 
WHERE E.sector = 'seguridad' AND T.horario_salida < '11:00:00'; 
