drop database if exists Hotel;
create database Hotel;
use Hotel;

create table Clientes(
    id_cliente int(4) auto_increment primary key,
    nombre varchar(30),
    apellido varchar(35),
    dni int(8),
    gmail varchar(50),
    telefono int(10)
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
    peso_soportado int default(220),
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
    sector varchar(20),
    nombre varchar(35),
    gmail varchar(35),
    sueldo float(4, 2)
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
    tipo enum('Toallas extra', 'Comida ilimitada', 'Masajes'),
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
    precio float (9, 2),
    cant_huespedes int(1),
    fecha_entrada datetime,
    fecha_salida datetime,
    foreign key(habitacion) references Habitaciones(id_habitacion)
);
 
create table Servicios_Reservas(
    id_historial_serv int(1) auto_increment primary key,
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