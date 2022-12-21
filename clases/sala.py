class sala ():
    def __init__ (self, pelicula,capacidadSala, horario):
        self.pelicula=pelicula
        self.capacidadSala=capacidadSala
        self.horario=horario

    def insertarSala (self, pelicula,capacidad,horario):
        if capacidad != "":
            sala.append(self.pelicula)
            capacidad=self.capacidadSala
            sala_horaria={
                "1":"12:00 - 14:30",
                "2":"16:00 - 18:30",
                "3":"19:00 - 21:30",
                "4":"22:00 - 00:00"
            }
    def eliminarSala (self,idsala):
        sala.remove(idsala)




    