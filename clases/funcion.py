from database.conexion import Conexion_BD

class Funcion:
    def __init__(self, idSala, fecha, horario, estado):
        self.idSala = idSala
        self.fecha = fecha
        self.horario = horario
        self.estado = estado

    def insertarFuncionEnBD(self):
        conn = Conexion_BD()
        conn.consult(f'INSERT INTO funcion (idSala, fecha, horario, estado) VALUES ("{self.idSala}", "{self.fecha}", "{self.horario}", "{self.estado}")')
        conn.commit()
        conn.close()

    def mostrarFunciones(self):
        conn = Conexion_BD()
        funciones = conn.consult(f'SELECT * FROM funcion').fetchall()
        conn.commit()
        conn.close()    
        return funciones

    def mostrarUnaFuncion(self, idFuncion):
        conn = Conexion_BD()
        funcion = conn.consult(f'SELECT * FROM funcion WHERE idFuncion = "{idFuncion}"').fetchone()
        conn.commit()
        conn.close()
        return funcion

    def eliminarUnaFuncion(self, idFuncion):
        conn = Conexion_BD()
        if conn.consult(f'SELECT * FROM funcion WHERE idFuncion = "{idFuncion}"').fetchall():
            conn.consult(f'DELETE FROM funcion WHERE idFuncion = "{idFuncion}"')
            conn.commit()
            conn.close()