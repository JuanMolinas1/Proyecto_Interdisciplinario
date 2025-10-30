drop database if exists EcoMove_SA;
create database EcoMove_SA;
use EcoMove_SA;

create table Organizaciones (
	id_organizacion int(1) auto_increment primary key,
	nombre varchar(30),
    sede varchar(50)
);

create table Vehiculos (
	id_vehiculo int(1) auto_increment primary key,
	tipo varchar(30),
    color varchar(15),
	organizacion int(1),
    foreign key(organizacion) references Organizaciones(id_organizacion)
);

create table Tecnicos (
	id_tecnico int(1) auto_increment primary key,
    nombre varchar(25),
    apellido varchar(25),
    dni bigint(8)
);

create table Piezas (
	id_pieza int(1) auto_increment primary key,
    nombre varchar(25),
    precio int(3),
    cantidad int(3)
);

create table Revisiones (
	id_revision int(1) auto_increment primary key,
    tecnico int(4),
    vehiculo int(4),
    problema varchar(50),
    fecha date,
    costo int(6),
    bateria int(3),
    tipo_servicio enum("Preventivo", "Correctivo"),
    foreign key (tecnico) references Tecnicos(id_tecnico),
    foreign key (vehiculo) references Vehiculos(id_vehiculo)
);

create table Piezas_Revision (
	id_pieza_revision int(1) auto_increment primary key,
    pieza int(1),
    revision int(1),
    foreign key (pieza) references Piezas(id_pieza),
    foreign key (revision) references Revisiones(id_revision)
);

insert into Organizaciones (nombre, sede) values
	("Pepito Interpraises", "Shipidibaum"),
	("Emuchito Compañi", "Ciudad Gotica"),
	("OppenEmpresa", "North"),
	("Robxs", "Washinton MCU"),
	("'Soy una compañia' ahh nombre", "'Soy Una Ciudad' ahh Ciudad");
    
insert into Vehiculos (tipo, color, organizacion) values
	("Auto Eléctrico", "Azul", 1),
    ("Moto de agua", "Negro", 5),
    ("Slurp", "Celeste", 4),
    ("Auto Eléctrico", "Verde", 2),
    ("Colectivo", "Rojo", 3);

insert into Tecnicos (nombre, apellido, dni) values
	("Francisco", "Gutierrez", 49283765),
    ("Thiago", "Viana", 48998723),
    ("Tito", "Calderon", 38227335),
    ("Alberto", "Instantaneo", 28776892),
    ("Luciano", "Hidrauler", 50676253);
    
insert into Piezas (nombre, precio, cantidad) values
	("Bujia", 40, 100),
    ("Motor", 20, 245),
	("Rueda", 10, 14),
    ("Botón", 57, 7),
    ("Maquina de vapor", 67, 67);
    
insert into Revisiones (tecnico, vehiculo, problema, fecha, costo, bateria, tipo_servicio) values
	(1, 1, "No prende", "2024-03-02", 100, 80, "Preventivo"),
    (3, 2, "No carga", "2024-12-12", 200, 80, "Correctivo"),
    (4, 3, "Hace mucho ruido", "2024-11-11", 300, 80, "Preventivo"),
    (2, 4, "Se maneja solo", "2012-10-10", 301, 80, "Preventivo"),
    (5, 5, "Hola", "2018-06-07", 67, 79, "Correctivo");
    
insert into Piezas_Revision (pieza, revision) values
	(1, 4),
    (2, 3),
    (3, 2),
    (4, 4),
    (5, 1);
    
select V.tipo, V.organizacion, R.tecnico
from Vehiculos V
inner join Revisiones R on V.id_vehiculo = R.vehiculo;

select id_revision, costo
from Revisiones
where costo > (
	select avg(costo)
    from Revisiones
);

select tipo_servicio, avg(costo)
from Revisiones
group by tipo_servicio;

-- No funciona
-- select tecnico, count(id_revision) as Cantidad_Revisiones
-- from Revisiones
-- where Cantidad_Revisiones > 3;

select vehiculo, count(id_revision) as Cantidad_revisiones
from Revisiones
group by vehiculo
order by Cantidad_revisiones asc
limit 1;

select V.organizacion, R.bateria
from Vehiculos V
inner join Revisiones R on V.id_vehiculo = R.vehiculo
where bateria < (
	select avg(bateria)
    from Revisiones
);

select tecnico, count(id_revision) as Revisioness
from Revisiones
group by tecnico
order by Revisioness desc
limit 3;
