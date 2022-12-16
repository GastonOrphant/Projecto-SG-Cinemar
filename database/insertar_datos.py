from database.conexion import Conexion_BD

def insertar_usuario(conn, usuario):
    cur = conn.cursor()
    sql = "INSERT INTO usuario VALUES(?, ?, ?, ?)"
    cur.execute(sql, usuario)
    conn.commit()

def insertar_sala(conn, sala):
    print('sala insertada')

conn = Conexion_BD('database/cinemar.db')  