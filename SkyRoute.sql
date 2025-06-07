#Base de datos
#Implementación y Consulta de la Base de Datos:
#Escribir las sentencias SQL (lenguaje DDL) necesarias para crear la estructura de la base de datos (tablas, restricciones, claves primarias, claves foráneas) basándose en el modelo relacional diseñado en la Actividad Integradora 2.  
#Escribir sentencias SQL (lenguaje DML) para insertar datos de ejemplo en cada una de las tablas creadas (al menos 3 registros por tabla).  
#Escribir al menos 5 consultas SQL (lenguaje DML - SELECT) que permitan recuperar información relevante del sistema. Ejemplos:
#Listar todos los clientes. 
#Mostrar las ventas realizadas en una fecha específica. 
#Obtener la última venta de cada cliente y su fecha. 
#Listar todos los destinos que empiezan con “S”
#Mostrar cuántas ventas se realizaron por país. 
#Agrupar todas las sentencias SQL (DDL y DML) en uno o varios archivos .sql, añadiendo comentarios que expliquen el propósito de cada sentencia o bloque de sentencias.  


#Crear base de datos
CREATE DATABASE IF NOT EXISTS `SkyRoute S.R.L.`;
USE `SkyRoute S.R.L.`;


#TABLA: Clientes

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    razon_social VARCHAR(100) NOT NULL,
    cuit VARCHAR(20) NOT NULL UNIQUE,
    correo VARCHAR(100) NOT NULL
);


#TABLA: Destinos

CREATE TABLE IF NOT EXISTS destinos (
    id_destino INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(100) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    costo DECIMAL(10,2) NOT NULL
);


#TABLA: Empleados

CREATE TABLE IF NOT EXISTS empleados (
    id_empleados INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(15) NOT NULL UNIQUE
);


#TABLA: Ventas

CREATE TABLE IF NOT EXISTS ventas (
    id_ventas INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_destino INT,
    id_empleado INT,
    fecha_ventas DATETIME NOT NULL,
    costo_total DECIMAL(10,2) NOT NULL,
    estado ENUM('Activa', 'Anulada') DEFAULT 'Activa',
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_destino) REFERENCES destinos(id_destino),
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleados)
);


#TABLA: Botón Arrepentimiento

CREATE TABLE IF NOT EXISTS boton_arrepentimiento (
    id_arrepentimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_ventas INT UNIQUE,
    fecha_anulacion DATETIME NOT NULL,
    motivo_anulacion TEXT,
    FOREIGN KEY (id_ventas) REFERENCES ventas(id_ventas)
);


#DATOS DE EJEMPLO (DML)


#Clientes
INSERT INTO clientes (razon_social, cuit, correo) VALUES
('Viajes SA', '30-12345678-9', 'contacto@viajessa.com'),
('MundoTur', '30-87654321-0', 'info@mundotur.com'),
('Turismo Express', '30-11112222-3', 'ventas@turexpress.com');

#Destinos
INSERT INTO destinos (ciudad, pais, costo) VALUES
('Pepinin', 'Argentina', 20000),
('Rabanito', 'Chile', 35000),
('Bananon', 'Uruguay', 30000);

#Empleados
INSERT INTO empleados (nombre, apellido, dni) VALUES
('Lucía', 'Pérez', '30555888'),
('Carlos', 'Ramírez', '29333444'),
('Ana', 'Fernández', '27888999');

#Ventas
INSERT INTO ventas (id_cliente, id_destino, id_empleado, fecha_ventas, costo_total, estado) VALUES
(1, 1, 1, NOW(), 20000, 'Activa'),
(2, 3, 2, NOW(), 30000, 'Activa'),
(3, 2, 3, NOW(), 35000, 'Activa');

#Botón de arrepentimiento
INSERT INTO boton_arrepentimiento (id_ventas, fecha_anulacion, motivo_anulacion) VALUES
(2, NOW(), 'Error en el destino');
