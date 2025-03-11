# DB Insert

# pip install mysql-connector-python
# https://mariadb.org/download/ (mysql -u root)

# Importar la librerías necesarias
import mysql.connector 

conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'data_base_test'
)

cursor = conexion.cursor()

nuevo_usuario = ('Juan', 30)

consulta = 'INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)'

cursor.execute(consulta, nuevo_usuario)

conexion.commit()

print('Registro guardado')

conexion.close()
