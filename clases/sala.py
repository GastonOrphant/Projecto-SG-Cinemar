from database.conexion import Conexion_BD

class Sala:
    def __init__(self, pelicula, capacidadSala, horario):
        self.pelicula = pelicula
        self.capacidadSala = capacidadSala
        self.horario = horario

    def insertarSalaEnBD(self):
        conn = Conexion_BD()
        conn.consult(f'INSERT INTO sala (pelicula, capacidadSala, horario) VALUES ("{self.pelicula}", {self.capacidadSala}, "{self.horario}")')
        conn.commit()
        conn.close()

    def eliminarSala(idSala):
        conn =  Conexion_BD()
        conn.consult(f'DELETE FROM sala WHERE idSala = "{idSala}"')        
        conn.commit()
        conn.close()

    def salaPorPelicula(pelicula):
        conn = Conexion_BD()
        sala = conn.consult(f"SELECT * FROM sala WHERE pelicula = '{pelicula}'").fetchone()
        conn.close()
        return sala[0], sala[1], sala[2], sala[3]

    def modificarSala(idSala, nuevapelicula, nuevacapacidad, nuevohorario):
        conn = Conexion_BD()
        conn.consult(f"UPDATE sala SET pelicula = '{nuevapelicula}', capacidadSala = '{nuevacapacidad}', horario = '{nuevohorario}'  WHERE idSala = {idSala}")
        conn.commit()
        conn.close()

    def verTodas():
        conn = Conexion_BD()
        salas = conn.consult(f"SELECT * FROM sala").fetchall()
        conn.close()
        return salas

    def salaEstaEnBD(idSala):
        conn = Conexion_BD()
        sala = conn.consult(f"SELECT * FROM sala WHERE idSala = {idSala}").fetchone()
        conn.close()
        return (sala != None)