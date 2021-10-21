--
-- File generated with SQLiteStudio v3.3.3 on sáb. oct. 9 03:05:46 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: mensajes
CREATE TABLE mensajes (message_id INTEGER PRIMARY KEY, from_id INTEGER REFERENCES usuario (id), to_id INTEGER NOT NULL, asunto VARCHAR NOT NULL, mensaje VARCHAR NOT NULL);
INSERT INTO mensajes (message_id, from_id, to_id, asunto, mensaje) VALUES (1, 2, 3, 'hola', 'hola');

-- Table: mensajesV1
CREATE TABLE mensajesV1 (message_id INTEGER PRIMARY KEY, usuario VARCHAR NOT NULL, asunto VARCHAR NOT NULL, mensaje VARCHAR NOT NULL);
INSERT INTO mensajesV1 (message_id, usuario, asunto, mensaje) VALUES (1, 'Luis2345', 'Hola', 'Hola como estas?');
INSERT INTO mensajesV1 (message_id, usuario, asunto, mensaje) VALUES (2, 'Maria2', 'Saludo', 'Hola, buenas noticias.');

-- Table: usuario
CREATE TABLE usuario (id INTEGER PRIMARY KEY, nombre VARCHAR NOT NULL, usuario VARCHAR NOT NULL, correo VARCHAR NOT NULL, clave VARCHAR NOT NULL);
INSERT INTO usuario (id, nombre, usuario, correo, clave) VALUES (1, 'Pedro', 'Pedro1', 'p@p.com', 'pbkdf2:sha256:260000$lqMnnsIlUrqMnm12$a59d1ed53eae23ccbd6e3c2e2cfa28981914440b3bff07c98ae8d7f6452e917c');
INSERT INTO usuario (id, nombre, usuario, correo, clave) VALUES (2, 'Maria', 'Maria1', 'm@m.com', 'pbkdf2:sha256:260000$lqMnnsIlUrqMnm12$a59d1ed53eae23ccbd6e3c2e2cfa28981914440b3bff07c98ae8d7f6452e917c');
INSERT INTO usuario (id, nombre, usuario, correo, clave) VALUES (3, 'Manuel', 'escalantem', 'escalantem@uninorte.edu.co', 'pbkdf2:sha256:260000$wKvqQssWlQqBGsNe$b4ed9cc008aa9fee4589d1757d5b28e0e14773153923cc4b115c5656d04779ec');
INSERT INTO usuario (id, nombre, usuario, correo, clave) VALUES (6, 'Luis', 'lgomez12', 'lgomez@uninorte.edu.co', 'pbkdf2:sha256:260000$wKmAzL7oidDcFRJX$e1793e833f9ad67d090228743f7265baf322940ad93697a708a08577f651f45f');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
