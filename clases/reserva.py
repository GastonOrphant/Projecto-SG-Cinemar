from database.conexion import Conexion_BD

class Reserva:
    def __init__(self, idCliente, idSala, fecha):
        self.idCliente = idCliente
        self.idSala = idSala
        self.fecha = fecha

    def insertarReservaEnBD(self):
        '''Insertar una reserva en la base de datos'''
        conn = Conexion_BD()
        conn.consult(f'INSERT INTO reserva VALUES ({self.idCliente}, {self.idSala}, {self.fecha}')
        conn.commit()
        conn.close()

    def mostrarReservasPorUsuario(self, idCliente):
        conn = Conexion_BD()
        reservas = conn.consult(f'SELECT * FROM reserva WHERE idCliente = {idCliente}').fetchall()
        conn.close()    
        return reservas

    def eliminarReserva(self, idReserva):
        conn = Conexion_BD()
        if conn.consult(f'SELECT * FROM reserva WHERE idReserva = {idReserva}'):
            conn.consult(f'DELETE FROM reserva WHERE idReserva = {idReserva}')
            conn.commit()
        conn.close()        