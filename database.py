import mysql.connector
from mysql.connector import errorcode

# Configuración de la conexión
db_config = {
    'user': 'u947644991_sebaslt	',
    'password': 'GireiPain9604*',
    'host': 'srv1050.hstgr.io', # O la dirección IP de tu servidor
    'database': 'u947644991_database'
}

try:
    # Crear conexión
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Realizar una consulta
    query = "SELECT * FROM users"
    cursor.execute(query)

    # Imprimir resultados
    for row in cursor.fetchall():
        print(row)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuario o contraseña incorrectos")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe")
    else:
        print(err)
finally:
    # Cerrar cursor y conexión
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexión cerrada")
