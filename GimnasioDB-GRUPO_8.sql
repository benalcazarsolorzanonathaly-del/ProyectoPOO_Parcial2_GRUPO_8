-- ============================================
-- SCRIPT DE CREACIÓN: GIMNASIO DB - SQL SERVER
-- ============================================

-- 1. Crear base de datos
USE master;
GO

IF EXISTS (SELECT name FROM sys.databases WHERE name = 'GimnasioDB')
BEGIN
    ALTER DATABASE GimnasioDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE GimnasioDB;
    PRINT '🗑️ Base de datos GimnasioDB eliminada (existía previamente).';
END
GO

CREATE DATABASE GimnasioDB;
PRINT '✅ Base de datos GimnasioDB creada.';
GO

USE GimnasioDB;
GO

-- 2. Crear tabla Membresias
CREATE TABLE Membresias (
    id_membresia INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(100) NOT NULL,
    precio_base DECIMAL(10,2) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    acceso_sala BIT DEFAULT 0,
    acceso_clases BIT DEFAULT 0,
    plan_videos VARCHAR(50) NULL,
    incluye_app BIT DEFAULT 0,
    fecha_registro DATETIME DEFAULT GETDATE(),
    activo BIT DEFAULT 1
);
GO

-- 3. Agregar constraints
ALTER TABLE Membresias 
ADD CONSTRAINT CHK_Precio_Positivo 
CHECK (precio_base >= 0);

ALTER TABLE Membresias 
ADD CONSTRAINT CHK_Tipo_Valido 
CHECK (tipo IN ('Presencial', 'Virtual'));
GO

-- 4. Crear índices
CREATE INDEX IX_Membresias_Nombre ON Membresias(nombre);
CREATE INDEX IX_Membresias_Tipo ON Membresias(tipo);
CREATE INDEX IX_Membresias_Activo ON Membresias(activo);
GO

-- 5. Insertar datos de ejemplo
INSERT INTO Membresias (nombre, precio_base, tipo, acceso_sala, acceso_clases) 
VALUES 
    ('Plan Básico Presencial', 50.00, 'Presencial', 1, 0),
    ('Plan Premium Presencial', 80.00, 'Presencial', 1, 1),
    ('Plan Familiar Presencial', 120.00, 'Presencial', 1, 1);

INSERT INTO Membresias (nombre, precio_base, tipo, plan_videos, incluye_app) 
VALUES 
    ('Virtual Básico', 30.00, 'Virtual', 'Estándar', 0),
    ('Virtual Full', 45.00, 'Virtual', 'Premium', 1),
    ('Virtual Pro', 60.00, 'Virtual', 'Avanzado', 1);
GO

-- 6. Verificar creación
SELECT 'Tabla Membresias' AS Tabla, COUNT(*) AS Registros FROM Membresias;
GO

SELECT * FROM Membresias;
GO

PRINT '=========================================';
PRINT '✅ ESQUEMA GIMNASIODB CREADO EXITOSAMENTE';
PRINT '=========================================';
GO