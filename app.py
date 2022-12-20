import tkinter as tk
from clases.usuario import Usuario 

def login():
    # crear la ventana principal para el login
    root = tk.Tk()
    root.wm_iconbitmap('assets/favicon.png')
    root.title("Login")
    # labels
    mail_label = tk.Label(root, text="Mail:")
    password_label = tk.Label(root, text="Password:")
    # forms
    mail_field = tk.Entry(root)
    password_field = tk.Entry(root, show="*")
    # boton de ingresar
    submit_button = tk.Button(root, text="Ingresar")
    def handle_submit():
        # toma los valores ingresados en las fields
        mail = mail_field.get()
        password = password_field.get()
        # verifica que el mail ingresado este en la base de datos
        if Usuario.usuarioEstaEnBD(mail):
            if Usuario.validarUsuario(mail, password):
                # realiza el login y pasa a ventana de reservas
                pass
        else:
            pass
            # CARTEL USUARIO INCORRECTO
    # Bindea el boton submit a la funcion handle_submit
    submit_button.bind("<Button-1>", handle_submit)
    # Boton de Registro
    register_button = tk.Button(root, text="Registrarse!")
    def handle_register():
        root.quit()
        registro()
    register_button.bind("<Button-1>", handle_register)   
    # posicionar los widgets
    mail_label.grid(row=0, column=0)
    mail_field.grid(row=0, column=1)
    password_label.grid(row=1, column=0)
    password_field.grid(row=1, column=1)
    submit_button.grid(row=2, column=1)
    register_button.grid(row=2, column=0)
    # start the main loop
    root.mainloop()


# Realiza el registro de un usuario
def registro():
    root = tk.Tk()
    root.wm_iconbitmap('assets/favicon.png')
    root.title("Registro de usuario")
    nombre_label = tk.Label(root, text="Ingrese un nombre de usuario:")
    mail_label = tk.Label(root, text="Ingrese un Mail para registrarse:")
    password_label = tk.Label(root, text="Ingrese una contraseña: ")
    tipo_usuario_label = tk.Label(root, text="Ingrese su tipo de usuario (0 = Cliente, 1 = Admin):")  #Cambiar a botón mas adelante
    tarjeta_label = tk.Label(root, text="Cuenta con tarjeta de descuentos(0: No, 1: Si): ")
    nombre_field = tk.Entry(root)
    mail_field = tk.Entry(root)
    password_field = tk.Entry(root, show="*")
    tipo_usuario_field = tk.Entry(root)
    tarjeta_field = tk.Entry(root)
    submit_button = tk.Button(root, text="Registrarse")
    def handle_submit():
        # toma los valores ingresados en las fields
        nombre = nombre_field.get()
        mail = mail_field.get()
        contrasenia = password_field.get()
        tipo = tarjeta_field.get()
        usuario = Usuario(nombre, mail, contrasenia, tipo)
        if usuario.usuarioEstaEnBD(mail):
            print("Usuario ya registrado.")
        else:    
            usuario.insertarEnBD()
    # bind the submit button to the submit function
    submit_button.bind("<Button-1>", handle_submit)
    # posicionar los widgets
    nombre_label.grid(row=0, column=0)
    nombre_field.grid(row=0, column=1)
    mail_label.grid(row=1, column=0)
    mail_field.grid(row=1, column=1)
    password_label.grid(row=2, column=0)
    password_field.grid(row=2, column=1)
    tipo_usuario_label.grid(row=3, column=0)
    tipo_usuario_field.grid(row=3, column=1)
    tarjeta_label.grid(row=4, column=0)
    tarjeta_field.grid(row=4, column=1)
    submit_button.grid(row=5, column=1)
    # start the main loop
    root.mainloop()        

def descuentos(precioEntrada, fecha):
    '''Lunes y Miércoles: 20% | Martes y Jueves: 15% | Viernes, Sábados y Domingos: 10% 
                    Siendo modificable según los directivos.'''
    if (fecha == 'Lunes') or (fecha == 'Miercoles'):
        descuento = 0.2
    elif (fecha == 'Martes') or (fecha == 'Jueves'):
        descuento = 0.15
    else:
        descuento = 0.1
    return(precioEntrada - precioEntrada*descuento)             


if __name__ == "__main__":
    login()