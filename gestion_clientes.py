# Alta, baja, modificación, listado de clientes

from conexion_base_datos import obtener_conexion

def agregar_cliente(razon_social, cuit, email):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (razon_social, cuit, email) VALUES (%s, %s, %s)", (razon_social, cuit, email))
    conexion.commit()
    conexion.close()

def listar_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conexion.close()
    return clientes

def modificar_cliente(id_cliente, razon_social, cuit, email):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE clientes SET razon_social = %s, cuit = %s, email = %s WHERE id = %s", (razon_social, cuit, email, id_cliente))
    conexion.commit()
    conexion.close()

def eliminar_cliente(id_cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
    conexion.commit()
    conexion.close()
