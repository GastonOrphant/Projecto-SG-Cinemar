from database.conexion import Conexion_BD

class Sala:
    def __init__(self, pelicula, capacidadSala, horario):
        self.pelicula = pelicula
        self.capacidadSala = capacidadSala
        self.horario = horario

    def insertarSalaEnBD(self):
        conn = Conexion_BD()
        conn.consult(f'INSERT INTO sala (pelicula, capacidadSala, horario) VALUES ("{self.pelicula}", "{self.capacidadSala}", "{self.horario}"')
        conn.commit()
        conn.close()

    def eliminarSala(self, idSala):
        conn =  Conexion_BD()
        conn.consult(f'DELETE FROM sala WHERE idSala = "{idSala}"')        
        conn.commit()
        conn.close()