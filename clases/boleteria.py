class boleteria:
    def __init__ (self,cliente=cliente[],nombre,pelicula,hora,sala,silla,modo_pago):
        self._cliente=cliente
        self._nombre=nombre
        self._pelicula=pelicula
        self._hora=hora
        self._sala=sala
        self._silla=silla
        self._modo_pago=modo_pago
    
    def __str__ (self):
        cadena= f"\nNombre: {self.__nombre}"
        cadena+= f"\nPelicula: {self.__pelicula}"
        cadena+= f"\nhora: {self.__hora}"
        cadena+= f"\nDNI: {self.__sala}"
        cadena+=f"\nSilla:{self._silla}"
        return cadena

    def venta_entrada():
        pass
    def descuento():
        pass
    