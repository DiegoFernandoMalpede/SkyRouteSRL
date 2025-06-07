# Registrar ventas y botón de arrepentimiento


from conexion_base_datos import obtener_conexion
from datetime import datetime, timedelta

def registrar_venta(id_cliente, id_destino, costo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    ahora = datetime.now()
    cursor.execute(
        "INSERT INTO ventas (id_cliente, id_destino, fecha, costo, estado) VALUES (%s, %s, %s, %s, 'Activa')",
        (id_cliente, id_destino, ahora, costo)
    )
    conexion.commit()
    conexion.close()

def listar_ventas():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT v.id, c.razon_social, d.ciudad, v.fecha, v.costo, v.estado
        FROM ventas v
        JOIN clientes c ON v.id_cliente = c.id
        JOIN destinos d ON v.id_destino = d.id
        ORDER BY v.fecha DESC
    """)
    ventas = cursor.fetchall()
    conexion.close()
    return ventas

def anular_venta_si_es_reciente(id_venta):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT fecha FROM ventas WHERE id = %s AND estado = 'Activa'", (id_venta,))
    resultado = cursor.fetchone()
    if resultado:
        fecha_venta = resultado[0]
        ahora = datetime.now()
        if ahora - fecha_venta <= timedelta(minutes=5):
            cursor.execute("UPDATE ventas SET estado = 'Anulada', anulada_en = %s WHERE id = %s", (ahora, id_venta))
            conexion.commit()
            print("✅ Venta anulada con éxito.")
        else:
            print("⛔ No se puede anular: han pasado más de 5 minutos.")
    else:
        print("⛔ Venta no encontrada o ya anulada.")
    conexion.close()
