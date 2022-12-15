import sqlite3


def select_usuario_nombre(conn, nombre):
    cur = conn.cursor()
    cur.execute(f"SELECT nombre FROM usuario WHERE nombre = {nombre}")
    filas = cur.fetchall()
    return filas

def select_usuario_id(conn, id):
    cur = conn.cursor()
    cur.execute(f"SELECT idUsuario FROM usuario WHERE id = {id}")
    filas = cur.fetchall()
    return filas

def select_usuario_admin(conn):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM usuario WHERE tipoUsuario = 1")
    filas = cur.fetchall()
    return filas        
    
def select_usuario_mail(conn, mail):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM usuario WHERE mail = {mail}")
    filas = cur.fetchall()
    return filas