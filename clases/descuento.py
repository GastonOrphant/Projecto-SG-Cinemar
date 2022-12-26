from database.conexion import Conexion_BD

class Descuento:
    def __init__(self, dia, descuento):
        self.dia = dia
        self.descuento = descuento


    def modificarDescuento(dia, nuevodescuento):
        conn = Conexion_BD()
        conn.consult(f"UPDATE descuento SET descuento = '{nuevodescuento}' WHERE dia = '{dia}'")
        conn.commit()
        conn.close()

    def mostrarDescuentos():
        conn = Conexion_BD()
        descuentos = conn.consult("SELECT * FROM descuento").fetchall()
        conn.close()
        return descuentos



        
#def descuento(): 
#   PRECIO_ENTRADA - PRECIO_ENTRADA*descuento             
