
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
            

#Pruebas
Gaston = Usuario("Gaston", "gaston@gmail.com", "asd123", 1)
print(Gaston.__str__())

