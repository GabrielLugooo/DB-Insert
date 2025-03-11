<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# DB INSERT

<a href="https://github.com/GabrielLugooo/DB-Insert" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20DB%20Insert-000000" alt="English DB Insert" /></a>
<a href="https://github.com/GabrielLugooo/DB-Insert/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20DB%20Insert-green" alt="Spanish DB Insert" /></a>

### Objective

This project aims to demonstrate how to insert data into a `MySQL` database using `MariaDB` and `Python`. A connection to the database is established, a `SQL` query is executed to insert a new user, and the transaction is committed to save the changes.

It also provides a basic framework for handling database operations in `Python`, serving as a starting point for more advanced projects that require data manipulation in `MySQL`.

### Skills Learned

- Connecting to a MySQL database from Python.
- Running SQL queries with `mysql-connector-python`.
- Using transactions with `commit()` to commit changes to the database.
- Creating databases and tables in MariaDB.
- Inserting data into SQL tables.
- Handling cursors to execute SQL commands in Python.
- Closing database connections to optimize resources.

### Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)
![Static Badge](https://img.shields.io/badge/MySQL-000000?logo=mysql&logoSize=auto)
![Static Badge](https://img.shields.io/badge/MariaDB-000000?logo=mariadb&logoSize=auto)
![Static Badge](https://img.shields.io/badge/SQL-000000?logo=sql&logoSize=auto)
![Static Badge](https://img.shields.io/badge/Bash%20CMD-000000?logo=bash&logoSize=auto)

- Python Primary programming language.
- MySQL / MariaDB Relational database management system.
- `mysql-connector-python` Library to connect Python with MySQL/MariaDB.
- SQL Structured query language to manage databases.
- CMD (Windows) Command console to manage the database.

### Project

#### Code with Comments (English)

- **Python code to insert data into MySQL**

```python
# DB Insert

# Install the required library:
# pip install mysql-connector-python
# Ensure MySQL/MariaDB is running: mysql -u root

# Import the MySQL connection library
import mysql.connector

# Establish a connection to the database
conexion = mysql.connector.connect(
    host='localhost',   # Local server
    user='root',        # MySQL username
    password='',        # Password (empty by default on localhost)
    database='data_base_test'  # Database name
)

# Create a cursor to execute SQL queries
cursor = conexion.cursor()

# Data to insert (name and age)
new_user = ('Juan', 30)

# SQL query to insert data into the "usuarios" table
query = 'INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)'

# Execute the query with the provided data
cursor.execute(query, new_user)

# Commit the transaction to save changes
conexion.commit()

print('Record saved')  # Success message

# Close the database connection
conexion.close()
```

- **SQL code to create the database and table in MariaDB**

```sql
-- Log in to MySQL as root user
mysql -u root

-- Create the database
CREATE DATABASE data_base_test;

-- Verify that the database was created successfully
SHOW DATABASES LIKE 'data_base_test';

-- Use the newly created database
USE data_base_test;

-- Create the "usuarios" table with id, name, and age columns
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Auto-increment ID as primary key
    nombre VARCHAR(255) NOT NULL, -- User's name (mandatory field)
    edad INT -- User's age
);

-- Verify the structure of the created table
DESCRIBE usuarios;

-- Query all records from the "usuarios" table
SELECT * FROM usuarios;
```

#### SQL code preview in MariaDB (all by Windows CMD)

<img align="center" src="https://i.imgur.com/ZO9TsjB.jpeg" alt="Database01" />
<img align="center" src="https://i.imgur.com/G4rKQV8.jpeg" alt="Database02" />
<img align="center" src="https://i.imgur.com/zypP0gc.jpeg" alt="Database03" />
<img align="center" src="https://i.imgur.com/i2KFgMd.jpeg" alt="Database04" />

### Limitations

Db Insert it's just for educational purpose under the MIT License.

---

<h3 align="left">Connect with me</h3>

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
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20views&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
