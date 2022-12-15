
class Usuario:
    def __init__(self, nombreUsuario, mail, contrasenia, tipo):
        self.nombreUsuario = nombreUsuario
        self.mail = mail
        self.contrasenia = contrasenia
        self.tipo = tipo # 0 si es cliente | 1 si es admin

    def __str__(self):
        if self.tipo == 1:
            tipoUsuario = 'Administrador'
        else: 
            tipoUsuario = 'Cliente'
        return(f"Nombre: {self.nombreUsuario}, mail: {self.mail}, tipo de usuario: {tipoUsuario}")

    def insertarEnBD(self):
        pass