# Conexión y operaciones con MySQL

import mysql.connector
from config import config

def obtener_conexion():
    return mysql.connector.connect(
        host=config['localhost'],
        user=config['root'],
        password=config['tupassword'],
        database=config['SkyRoute S.R.L.']
    )
