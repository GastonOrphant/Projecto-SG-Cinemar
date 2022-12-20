from database.conexion import Conexion_BD
class Usuario:
    def __init__(self, nombreUsuario, mail, contrasenia, tipo, tarjeta):
        self.nombreUsuario = nombreUsuario
        self.mail = mail
        self.contrasenia = contrasenia
        self.tipo = tipo # 0 si es cliente | 1 si es admin
        self.tarjeta = tarjeta # 0 si no tiene | 1 si tiene

    def __str__(self):
        if self.tipo == 1:
            tipoUsuario = 'Administrador'
        else: 
            tipoUsuario = 'Cliente'
        return(f"Nombre: {self.nombreUsuario}, mail: {self.mail}, tipo de usuario: {tipoUsuario}")

    def insertarEnBD(self):
        '''Inserta un usuario en la base de datos'''
        conn = Conexion_BD()
        conn.consult(f'INSERT INTO usuario VALUES ({self.nombreUsuario} ,{self.mail}, {self.contrasenia}, {self.tipo}, {self.tarjeta})')
        conn.commit()

    def usuarioEstaEnBD(self, mail):
        '''Retorna True or False dependiendo de si el mail está o no en la base de datos'''
        conn = Conexion_BD()
        usuario = conn.consult(f"SELECT mail FROM usuario WHERE mail = '{mail}'").fetchone()
        conn.close()
        return usuario != None

    def validarUsuario(self, mail, contrasenia):
        conn= Conexion_BD()
        usuario=conn.consult(f"SELECT idUsuario, tipoUsuario, contrasenia FROM usuario WHERE mail = '{mail}'").fetchone()
        if usuario != None and usuario[2] == contrasenia:
            return usuario[0], usuario[1]
        conn.close()  
