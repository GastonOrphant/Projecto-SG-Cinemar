class administracion ():
    def __init__(self,descuentos,clientes=[],peliculas=[],salas=[]):
        self._clientes=clientes
        self._peliculas=peliculas
        self._salas=salas
        self._descuentos=descuentos

    def consulta_reserva_particular(self,cliente,clientes=[]):
        for i in range(len(clientes)):
            if self._clientes[i]==cliente:
                return self._clientes[i]
            else:
                return -1
    def consulta_clientes (self, clientes=[]):
        for i in range(len(clientes)):
            return self._clientes[i]

    def creacion_lista_peliculas (self,peliculas=[]):
        cant=int(input("ingresar cantidad de peliculas: "))
        for i in cant:
            peliculas[i]=input("Ingresa {1}° pelicula: ")
        return peliculas
    def crear_sala (self,peliculas=[],sala=[8]):
        print ("ORDEN PELICULAS")
        for i in range (len(peliculas)):
            print (f"{i}- {peliculas [i]}")
        for i in range (len(sala)):
            (f"SALA {i}")
            sala[i]=input("ingresar pelicula: ")
            
    def descuentos():
        pass
    