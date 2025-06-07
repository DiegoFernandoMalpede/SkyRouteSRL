# Alta, baja, modificación, listado de destinos


from conexion_base_datos import obtener_conexion

def agregar_destino(ciudad, pais, costo_base):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO destinos (ciudad, pais, costo_base) VALUES (%s, %s, %s)", (ciudad, pais, costo_base))
    conexion.commit()
    conexion.close()

def listar_destinos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM destinos")
    destinos = cursor.fetchall()
    conexion.close()
    return destinos

def modificar_destino(id_destino, ciudad, pais, costo_base):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE destinos SET ciudad = %s, pais = %s, costo_base = %s WHERE id = %s", (ciudad, pais, costo_base, id_destino))
    conexion.commit()
    conexion.close()

def eliminar_destino(id_destino):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM destinos WHERE id = %s", (id_destino,))
    conexion.commit()
    conexion.close()
