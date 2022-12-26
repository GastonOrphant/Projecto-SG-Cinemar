import tkinter as tk
from clases.usuario import Usuario
from administracion import *
from cliente import *

PRECIO_ENTRADA = 500

def login():
    '''crear la ventana principal para el login'''
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x200")
    
    mail_label = tk.Label(root, text="Mail:")
    mail_label.pack()
    mail_field = tk.Entry(root)
    mail_field.pack()

    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_field = tk.Entry(root, show="*")
    password_field.pack()

    # boton de ingresar
    def handle_submit():
        # toma los valores ingresados en las fields
        mail = mail_field.get()
        password = password_field.get()
        # verifica que el mail ingresado este en la base de datos
        if Usuario.usuarioEstaEnBD("", mail):
            validacion = Usuario.validarUsuario("",mail, password)
            if validacion != None:
                if Usuario.esAdmin("",Usuario.idUsuario("",mail)):
                    root.destroy()
                    admin()
                else:
                    root.destroy()
                    cliente(validacion[0])          # validacion[0] contiene el idCliente
        else:
            print("El usuario no existe en la base de datos")
    submit_button = tk.Button(root, text="Ingresar", command=handle_submit)
    submit_button.pack()  

    # Boton de Registro
    def handle_register():
        root.destroy()
        registro()
    register_button = tk.Button(root, text="Registrarse!", command=handle_register)  
    register_button.pack() 
    # mainloop
    root.mainloop()

def registro():
    '''Realiza el registro de un usuario'''
    root = tk.Tk()
    root.title("Registro de usuario")
    root.geometry("640x480")

    nombre_label = tk.Label(root, text="Ingrese un nombre de usuario:")
    nombre_label.pack()
    nombre_field = tk.Entry(root)
    nombre_field.pack()

    mail_label = tk.Label(root, text="Ingrese un Mail para registrarse:")
    mail_label.pack()
    mail_field = tk.Entry(root)
    mail_field.pack()

    password_label = tk.Label(root, text="Ingrese una contraseña: ")
    password_label.pack()
    password_field = tk.Entry(root, show="*")
    password_field.pack()

    tipo_usuario_label = tk.Label(root, text="Ingrese su tipo de usuario (0 = Cliente, 1 = Admin):")  #Cambiar a botón mas adelante
    tipo_usuario_label.pack()
    tipo_usuario_field = tk.Entry(root)
    tipo_usuario_field.pack()

    tarjeta_label = tk.Label(root, text="Cuenta con tarjeta de descuentos(0: No, 1: Si): ")
    tarjeta_label.pack()
    tarjeta_field = tk.Entry(root)
    tarjeta_field.pack()

    def handle_submit():
        # toma los valores ingresados en las fields
        nombre = nombre_field.get()
        mail = mail_field.get()
        contrasenia = password_field.get()
        tipo = tipo_usuario_field.get()
        tarjeta = tarjeta_field.get()
        usuario = Usuario(nombre, mail, contrasenia, tipo, tarjeta)
        if usuario.usuarioEstaEnBD(mail):
            print("Usuario ya registrado.")
        else:    
            usuario.insertarUsuarioEnBD()
            print("Usuario registrado con exito!")
    submit_button = tk.Button(root, text="Registrarse", command=handle_submit)        
    submit_button.pack()
    # start the main loop
    root.mainloop()        
    
if __name__ == "__main__":
    login()
    