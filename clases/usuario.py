
class Usuario:
    def __init__(self, nombreUsuario, mail, contrasenia, tipo,pelicula[]):
        self._nombreUsuario = nombreUsuario
        self._mail = mail
        self._contrasenia = contrasenia
        self._tipo = tipo # 0 si es cliente | 1 si es admin
        self._pelicula=pelicula

    def __str__(self):
        if self._tipo == 1:
            tipoUsuario = 'Administrador'
        else: 
            tipoUsuario = 'Cliente'
        return(f"Nombre: {self.nombreUsuario}, mail: {self.mail}, tipo de usuario: {tipoUsuario}")

    def insertarEnBD(self):
        pass
    def modificar_usurio(self, nombreUsuario, mail, contrasenia):
        if (self._nombreUsuario== nombreUsuario) and (self.contrasenia==contrasenia):
            self._nombreUsuario=nombreUsuario
            self._contrasenia=contrasenia
        else:
            return ("El correo no pertenece a una cuenta")
    def consulta_pelicula (self,pelicula):
        for elemento in pelicula:
            return (f"Sus peliculas son: {elemento}")


