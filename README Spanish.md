<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1749686400&v=beta&t=hBmszzzG0Zu-m7ZxeCdU5VxgDWqIZuWB0vnrMycuqY4" alt="gabriellugo" />

# DB INSERT

<a href="https://github.com/GabrielLugooo/DB-Insert/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/DB%20Insert%20Español-000000" alt="DB Insert Español" /></a>
<a href="https://github.com/GabrielLugooo/DB-Insert" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/DB%20Insert%20Inglés-green" alt="DB Insert Inglés" /></a>

### Objetivos

Este proyecto tiene como objetivo demostrar cómo insertar datos en una base de datos `MySQL` utilizando `MariaDB` y `Python`. Se establece una conexión con la base de datos, se ejecuta una consulta `SQL` para insertar un nuevo usuario y se confirma la transacción para guardar los cambios.

Además, proporciona una estructura básica para manejar operaciones de base de datos en `Python`, sirviendo como punto de partida para proyectos más avanzados que requieran la manipulación de datos en `MySQL`.

### Habilidades Aprendidas

- Conexión a una base de datos MySQL desde Python.
- Ejecución de consultas SQL con `mysql-connector-python`.
- Uso de transacciones con `commit()` para confirmar cambios en la base de datos.
- Creación de bases de datos y tablas en MariaDB.
- Inserción de datos en tablas SQL.
- Manejo de cursores para ejecutar comandos SQL en Python.
- Cierre de conexiones a bases de datos para optimizar recursos.

### Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)
![Static Badge](https://img.shields.io/badge/MySQL-000000?logo=mysql&logoSize=auto)
![Static Badge](https://img.shields.io/badge/MariaDB-000000?logo=mariadb&logoSize=auto)
![Static Badge](https://img.shields.io/badge/SQL-000000?logo=sql&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Bash%20CMD-000000?logo=bash&logoSize=auto)

- Python Lenguaje de programación principal.
- MySQL / MariaDB Sistema de gestión de bases de datos relacionales.
- `mysql-connector-python` Biblioteca para conectar Python con MySQL/MariaDB.
- SQL Lenguaje de consulta estructurado para manejar bases de datos.
- CMD (Windows) Consola de comandos para administrar la base de datos.

### Proyecto

#### Código con Comentarios (Español)

- **Código en Python para insertar datos en MySQL**

```python
# DB Insert

# Instalar la librería si no está instalada:
# pip install mysql-connector-python

# Asegurarse de tener MySQL/MariaDB corriendo: mysql -u root

# Importar la librería para conectarse a MySQL
import mysql.connector

# Establecer la conexión con la base de datos
conexion = mysql.connector.connect(
    host='localhost',   # Servidor local
    user='root',        # Usuario de MySQL
    password='',        # Contraseña (vacía por defecto en localhost)
    database='data_base_test'  # Nombre de la base de datos
)

# Crear un cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Datos a insertar (nombre y edad)
nuevo_usuario = ('Juan', 30)

# Consulta SQL para insertar datos en la tabla "usuarios"
consulta = 'INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)'

# Ejecutar la consulta con los datos proporcionados
cursor.execute(consulta, nuevo_usuario)

# Confirmar la transacción para guardar los cambios
conexion.commit()

print('Registro guardado')  # Mensaje de éxito

# Cerrar la conexión con la base de datos
conexion.close()
```

- **Código SQL para crear la base de datos y la tabla en MariaDB**

```sql
-- Iniciar sesión en MySQL como usuario root
mysql -u root

-- Crear la base de datos
CREATE DATABASE data_base_test;

-- Verificar que la base de datos fue creada correctamente
SHOW DATABASES LIKE 'data_base_test';

-- Usar la base de datos recién creada
USE data_base_test;

-- Crear la tabla "usuarios" con columnas id, nombre y edad
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY, -- ID autoincremental como clave primaria
    nombre VARCHAR(255) NOT NULL, -- Nombre del usuario (campo obligatorio)
    edad INT -- Edad del usuario
);

-- Verificar la estructura de la tabla creada
DESCRIBE usuarios;

-- Consultar todos los registros de la tabla "usuarios"
SELECT * FROM usuarios;
```

#### Vista Previa del código SQL en MariaDB (todo por Windows CMD)

<img align="center" src="https://i.imgur.com/ZO9TsjB.jpeg" alt="Database01" />
<img align="center" src="https://i.imgur.com/G4rKQV8.jpeg" alt="Database02" />
<img align="center" src="https://i.imgur.com/zypP0gc.jpeg" alt="Database03" />
<img align="center" src="https://i.imgur.com/i2KFgMd.jpeg" alt="Database04" />

### Limitaciones

Db Insert es solo para fines educativos bajo la licencia MIT.

---

<h3 align="left">Conecta Conmigo</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
