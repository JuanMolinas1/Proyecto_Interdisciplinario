drop database if exists hotel;
create database hotel;
use hotel;

create table Clientes(
    id_cliente int(4) auto_increment primary key,
    nombre varchar(30),
    apellido varchar(35),
    dni int(8),
    gmail varchar(50),
    telefono bigint(10),
    vip bool
);

create table Zonas(
    id_zona enum('A', 'B', 'C', 'D') primary key,
    nombre_zona enum('Zona Principal', 'Comedores', 'Habitaciones Exclusivas', 'Habitaciones Baratas')
);

create table Habitaciones(
    id_habitacion int(3) auto_increment primary key,
    numero int(3),
    zona enum('A', 'B', 'C', 'D'),
    estado enum('Disponible', 'Limpiando', 'Ocupada'),
    tipo enum('Presidencial','Suite','Standard'),
    capacidad int(1),
    foreign key(zona) references Zonas(id_zona)
);

create table Ascensores(
    id_ascensor int(1) auto_increment primary key,
    estado_ascensor enum('En Funcionamiento', 'En Mantenimiento'),
    peso_soportado int(4) default(220),
    zona_hotel enum('A', 'B', 'C', 'D'),
    foreign key(zona_hotel) references Zonas(id_zona)
);

create table Pagos(
    id_pago int(4) auto_increment primary key,
    forma_pago enum('Efectivo', 'Tarjeta', 'Crypto', 'Vacas'),
    estado_pago bool
);

create table Empleados(
    id_empleado int(3) auto_increment primary key,
    sector enum('Limpieza', 'Recepcion', 'Cocina', 'Mantenimiento', 'Seguridad'),
    nombre varchar(35),
    gmail varchar(35),
    sueldo float(6, 2)
);

create table Turnos(
    id_turno int(1) auto_increment primary key,
    empleado int(3),
    dia enum('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'),
    horario_entrada datetime,
    horario_salida datetime,
    foreign key(empleado) references Empleados(id_empleado)
);

create table Servicios(
    id_servicio int(1) auto_increment primary key,
    tipo enum('Toallas extra', 'Comida ilimitada', 'Masajes', 'SPA'),
    precio float(5, 2)
);

create table Mantenimientos(
    id_mantenimiento int(4) auto_increment primary key,
    empleado_involucrado int(3),
    habitacion int(3),
    zona enum('A', 'B', 'C', 'D'),
    tipo_mantenimiento enum('Limpieza', 'Reparación', 'Desratización'),
    foreign key(empleado_involucrado) references Empleados(id_empleado),
    foreign key(habitacion) references Habitaciones(id_habitacion),
    foreign key(zona) references Zonas(id_zona)
);
 
create table Reservas(
    id_reserva int(4) auto_increment primary key,
    habitacion int(3),
    cliente int(4),
    recepcionista int(4),
    precio float(9, 2),
    cant_huespedes int(1),
    fecha_entrada datetime,
    fecha_salida datetime,
    foreign key(habitacion) references Habitaciones(id_habitacion),
    foreign key(cliente) references Clientes(id_cliente),
    foreign key(recepcionista) references Empleados(id_empleado)
);
 
create table Servicios_Reservas(
    id_historial_servicio int(1) auto_increment primary key,
    cliente int(4),
    servicio int(1),
    foreign key(cliente) references Clientes(id_cliente),
    foreign key(servicio) references Servicios(id_servicio)
);

create table Registro_Reservas(
    id_registro_reserva int(1) auto_increment primary key,
    cliente int(4),
    reserva int(4),
    pago int(4),
    foreign key(cliente) references Clientes(id_cliente),
    foreign key(reserva) references Reservas(id_reserva),
    foreign key(pago) references Pagos(id_pago)
);

insert into Clientes (nombre, apellido, dni, gmail, telefono, vip) values
('Juan', 'Perez', 12345678, 'juan.perez@gmail.com', 1234567890, TRUE),
('Ana', 'Lopez', 23456789, 'ana.lopez@gmail.com', 2345678901, FALSE),
('Carlos', 'Gomez', 34567890, 'carlos.gomez@gmail.com', 3456789012, TRUE),
('Lucia', 'Fernandez', 45678901, 'lucia.fernandez@gmail.com', 4567890123, FALSE),
('Sofia', 'Martinez', 56789012, 'sofia.martinez@gmail.com', 5678901234, FALSE),
('Pedro', 'Ramirez', 67890123, 'pedro.ramirez@gmail.com', 6789012345, TRUE),
('Marta', 'Sanchez', 78901234, 'marta.sanchez@gmail.com', 7890123456, FALSE),
('Jorge', 'Diaz', 89012345, 'jorge.diaz@gmail.com', 8901234567, FALSE),
('Laura', 'Torres', 90123456, 'laura.torres@gmail.com', 9012345678, TRUE),
('Diego', 'Vargas', 11223344, 'diego.vargas@gmail.com', 1122334455, FALSE),
('Elena', 'Mendoza', 22334455, 'elena.mendoza@gmail.com', 2233445566, TRUE),
('Alberto', 'Rojas', 33445566, 'alberto.rojas@gmail.com', 3344556677, FALSE),
('Isabel', 'Castro', 44556677, 'isabel.castro@gmail.com', 4455667788, FALSE),
('Fernando', 'Gutierrez', 55667788, 'fernando.gutierrez@gmail.com', 5566778899, TRUE),
('Valeria', 'Morales', 66778899, 'valeria.morales@gmail.com', 6677889900, FALSE);

insert into Zonas (id_zona, nombre_zona) values
('A', 'Zona Principal'),
('B', 'Comedores'),
('C', 'Habitaciones Exclusivas'),
('D', 'Habitaciones Baratas');

insert into Habitaciones (numero, zona, estado, tipo, capacidad) values
(101, 'A', 'Disponible', 'Presidencial', 3),
(102, 'A', 'Ocupada', 'Suite', 2),
(103, 'B', 'Limpiando', 'Standard', 2),
(104, 'B', 'Disponible', 'Standard', 1),
(105, 'C', 'Ocupada', 'Presidencial', 4),
(106, 'C', 'Disponible', 'Suite', 2),
(107, 'D', 'Limpiando', 'Standard', 1),
(108, 'D', 'Disponible', 'Standard', 1),
(109, 'A', 'Ocupada', 'Suite', 3),
(110, 'B', 'Disponible', 'Standard', 2),
(111, 'C', 'Limpiando', 'Presidencial', 4),
(112, 'D', 'Disponible', 'Standard', 1),
(113, 'A', 'Ocupada', 'Suite', 2),
(114, 'B', 'Disponible', 'Standard', 2),
(115, 'C', 'Disponible', 'Presidencial', 3);

insert into Ascensores (estado_ascensor, peso_soportado, zona_hotel) values
('En Funcionamiento', 220, 'A'),
('En Mantenimiento', 220, 'B'),
('En Funcionamiento', 220, 'C'),
('En Funcionamiento', 220, 'D'),
('En Funcionamiento', 220, 'A'),
('En Funcionamiento', 220, 'B'),
('En Mantenimiento', 220, 'C'),
('En Funcionamiento', 220, 'D'),
('En Funcionamiento', 220, 'A'),
('En Funcionamiento', 220, 'B'),
('En Funcionamiento', 220, 'C'),
('En Funcionamiento', 220, 'D'),
('En Mantenimiento', 220, 'A'),
('En Funcionamiento', 220, 'B'),
('En Funcionamiento', 220, 'C');

insert into Pagos (forma_pago, estado_pago) values
('Efectivo', TRUE),
('Tarjeta', FALSE),
('Crypto', TRUE),
('Vacas', FALSE),
('Efectivo', TRUE),
('Tarjeta', TRUE),
('Crypto', FALSE),
('Vacas', TRUE),
('Efectivo', FALSE),
('Tarjeta', TRUE),
('Crypto', TRUE),
('Vacas', FALSE),
('Efectivo', TRUE),
('Tarjeta', FALSE),
('Crypto', TRUE);

insert into Empleados (sector, nombre, gmail, sueldo) values
('Recepcion', 'Luis Ramirez', 'luis.ramirez@gmail.com', 2500.50),
('Mantenimiento', 'Carmen Diaz', 'carmen.diaz@gmail.com', 2200.00),
('Cocina', 'Ana Torres', 'ana.torres@gmail.com', 2000.00),
('Seguridad', 'Jorge Salinas', 'jorge.salinas@gmail.com', 2300.00),
('Recepcion', 'Paula Moreno', 'paula.moreno@gmail.com', 2600.75),
('Mantenimiento', 'Miguel Soto', 'miguel.soto@gmail.com', 2150.00),
('Limpieza', 'Sandra Vega', 'sandra.vega@gmail.com', 2100.00),
('Seguridad', 'Alfredo Ruiz', 'alfredo.ruiz@gmail.com', 2350.00),
('Recepcion', 'Maria Lopez', 'maria.lopez@gmail.com', 2550.50),
('Mantenimiento', 'Ricardo Flores', 'ricardo.flores@gmail.com', 2250.00),
('Limpieza', 'Laura Mendoza', 'laura.mendoza@gmail.com', 2050.00),
('Cocina', 'Diego Gutierrez', 'diego.gutierrez@gmail.com', 2400.00),
('Recepcion', 'Clara Alvarez', 'clara.alvarez@gmail.com', 2580.00),
('Mantenimiento', 'Rosa Fernandez', 'rosa.fernandez@gmail.com', 2200.00),
('Limpieza', 'Jose Ramirez', 'jose.ramirez@gmail.com', 2000.00);

insert into Turnos (empleado, dia, horario_entrada, horario_salida) values
(1, 'Lunes', '2025-10-06 08:00:00', '2025-10-06 16:00:00'),
(2, 'Martes', '2025-10-07 09:00:00', '2025-10-07 17:00:00'),
(3, 'Miércoles', '2025-10-08 08:30:00', '2025-10-08 16:30:00'),
(4, 'Jueves', '2025-10-09 10:00:00', '2025-10-09 18:00:00'),
(5, 'Viernes', '2025-10-10 07:00:00', '2025-10-10 15:00:00'),
(6, 'Sábado', '2025-10-11 08:00:00', '2025-10-11 16:00:00'),
(7, 'Domingo', '2025-10-12 09:00:00', '2025-10-12 17:00:00'),
(8, 'Lunes', '2025-10-13 08:00:00', '2025-10-13 16:00:00'),
(9, 'Martes', '2025-10-14 09:00:00', '2025-10-14 17:00:00'),
(10, 'Miércoles', '2025-10-15 08:30:00', '2025-10-15 16:30:00'),
(11, 'Jueves', '2025-10-16 10:00:00', '2025-10-16 18:00:00'),
(12, 'Viernes', '2025-10-17 07:00:00', '2025-10-17 15:00:00'),
(13, 'Sábado', '2025-10-18 08:00:00', '2025-10-18 16:00:00'),
(14, 'Domingo', '2025-10-19 09:00:00', '2025-10-19 17:00:00'),
(15, 'Lunes', '2025-10-20 08:00:00', '2025-10-20 16:00:00');

insert into Servicios (tipo, precio) values
('Toallas extra', 5.00),
('Comida ilimitada', 50.00),
('Masajes', 40.00),
('SPA', 80.00);

insert into Mantenimientos (empleado_involucrado, habitacion, zona, tipo_mantenimiento) values
(2, 1, 'A', 'Limpieza'),
(3, 2, 'A', 'Reparación'),
(6, 3, 'B', 'Desratización'),
(7, 4, 'B', 'Limpieza'),
(2, 5, 'C', 'Reparación'),
(3, 6, 'C', 'Limpieza'),
(6, 7, 'D', 'Desratización'),
(7, 8, 'D', 'Limpieza'),
(2, 9, 'A', 'Reparación'),
(3, 10, 'B', 'Limpieza'),
(6, 11, 'C', 'Desratización'),
(7, 12, 'D', 'Limpieza'),
(2, 13, 'A', 'Reparación'),
(3, 14, 'B', 'Limpieza'),
(6, 15, 'C', 'Desratización');

insert into Reservas (habitacion, cliente, recepcionista, precio, cant_huespedes, fecha_entrada, fecha_salida) values
(1, 1, 1, 500.00, 2, '2025-11-01 14:00:00', '2025-11-05 12:00:00'),
(2, 2, 9, 450.00, 1, '2025-11-02 15:00:00', '2025-11-06 11:00:00'),
(3, 3, 13, 300.00, 2, '2025-11-03 14:00:00', '2025-11-07 12:00:00'),
(4, 4, 5, 280.00, 1, '2025-11-04 16:00:00', '2025-11-08 11:00:00'),
(5, 5, 5, 700.00, 3, '2025-11-05 14:00:00', '2025-11-10 12:00:00'),
(6, 6, 5, 600.00, 2, '2025-11-06 15:00:00', '2025-11-11 11:00:00'),
(7, 7, 1, 250.00, 3, '2025-11-07 14:00:00', '2025-11-09 12:00:00'),
(8, 4, 9, 200.00, 1, '2025-11-08 13:00:00', '2025-11-10 11:00:00'),
(9, 9, 13, 550.00, 2, '2025-11-09 14:00:00', '2025-11-13 12:00:00'),
(10, 10, 13, 300.00, 2, '2025-11-10 15:00:00', '2025-11-14 11:00:00'),
(11, 11, 5, 650.00, 3, '2025-11-11 14:00:00', '2025-11-15 12:00:00'),
(12, 4, 1, 210.00, 1, '2025-11-12 16:00:00', '2025-11-16 11:00:00'),
(13, 13, 9, 480.00, 2, '2025-11-13 14:00:00', '2025-11-17 12:00:00'),
(14, 14, 9, 320.00, 2, '2025-11-14 15:00:00', '2025-11-18 11:00:00'),
(15, 15, 9, 700.00, 3, '2025-11-15 14:00:00', '2025-11-19 12:00:00');

insert into Servicios_Reservas (cliente, servicio) values
(1, 1),
(1, 4),
(3, 3),
(3, 4),
(5, 2),
(5, 3),
(6, 3),
(7, 1),
(8, 2),
(9, 3),
(10, 1),
(10, 4),
(13, 1),
(14, 2),
(15, 3);

insert into Registro_Reservas (cliente, reserva, pago) values
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(4, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(4, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15);




