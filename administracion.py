import tkinter as tk
from clases.reserva import Reserva
from clases.usuario import Usuario
from clases.sala import Sala

def admin():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Panel de Administrador")
    # BOTONES
    def ver_todas_reservas():
        root = tk.Tk()
        listbox = tk.Listbox(root)
        reservas = Reserva.mostrarTodasLasReservas("")
        for reserva in reservas:
            listbox.insert(tk.END, reserva)
        listbox.pack()  
    ver_todas_reservas_button = tk.Button(root, text="Ver todas las reservas", command=ver_todas_reservas)
    ver_todas_reservas_button.pack()

    def ver_reservas_usuario():
        root = tk.Tk()
        usuario_label = tk.Label(root, text="Ingrese el mail de un usuario:")
        usuario_label.pack()
        usuario_field = tk.Entry(root)
        usuario_field.pack()
        def handle_submit():
            usuario = usuario_field.get()
            if Usuario.usuarioEstaEnBD("", usuario):
                idUsuario = Usuario.idUsuario("", usuario)
                reservas = Reserva.mostrarReservasPorUsuario(idUsuario)
                listbox = tk.Listbox(root)
                for reserva in reservas:
                    listbox.insert(tk.END, reserva)
                listbox.pack()
            else:
                error_label = tk.Label(root, text="El usuario no se encuentra en la base de datos!")
                error_label.pack()    
        submit_button = tk.Button(root, text="Ver usuario", command=handle_submit)        
        submit_button.pack()
    ver_reservas_usuario_button = tk.Button(root, text="Ver reservas de un usuario", command=ver_reservas_usuario)
    ver_reservas_usuario_button.pack()

    def crear_sala():
        root = tk.Tk()
        pelicula_label = tk.Label(root, text="Ingrese el nombre de la pelicula a ingresar")
        pelicula_label.pack()
        pelicula_field = tk.Entry(root)
        pelicula_field.pack()
        horario_label = tk.Label(root, text="Seleccione un horario para la pelicula")
        horario_label.pack()
        listbox = tk.Listbox(root)
        horarios=["10:30", "14:30", "15:30", "16:30", "17:30", "18:30", "20:30", "22:30"]
        for horario in horarios:
            listbox.insert(tk.END, horario)
        listbox.pack()
        horario_field = tk.Entry(root)
        horario_field.pack()
        def handle_submit():
            if horario_field.get() not in horarios:
                error_label = tk.Label(root, text="Ingrese un horario valido")
                error_label.pack()
            else:
                sala = Sala(pelicula_field.get(), 100,horario_field.get())    #100 es capacidad de sala
                sala.insertarSalaEnBD()
                root = tk.Tk()
                sala_label = tk.Label(root, text="Sala creada con exito!")
                sala_label.pack()
        submit_button = tk.Button(root, text="Aceptar", command=handle_submit)        
        submit_button.pack()    
    crear_sala_button = tk.Button(root, text="Crear una sala", command=crear_sala)
    crear_sala_button.pack()

    def modificar_sala():
        root = tk.Tk()
        pelicula_label = tk.Label(root, text="Ingrese el nombre de la pelicula cuya sala quiere modificar")
        pelicula_label.pack()
        pelicula_field = tk.Entry(root)
        pelicula_field.pack()
        def handle_sala():
            sala = Sala.salaPorPelicula(pelicula_field.get())
            if sala != None:
                root = tk.Tk()
                nuevapeli_label = tk.Label(root, text="Ingrese el nombre de la nueva pelicula: ")
                nuevapeli_label.pack()
                nuevapeli_field = tk.Entry(root)
                nuevapeli_field.pack()

                nuevohorario_label = tk.Label(root, text="Ingrese su horario: ")
                nuevohorario_label.pack()
                nuevohorario_field = tk.Entry(root)
                nuevohorario_field.pack()

                capacidad_label = tk.Label(root, text= "Ingrese la capacidad de la sala")
                capacidad_label.pack()
                capacidad_field = tk.Entry(root)
                capacidad_field.pack()

                def handle_submit():
                    nuevapeli = nuevapeli_field.get()
                    nuevohorario = nuevohorario_field.get()
                    nuevacapacidad = capacidad_field.get()
                    if nuevapeli != None:
                        Sala.modificarSala(sala[0], nuevapeli, nuevacapacidad, nuevohorario)
                        success_label = tk.Label(root, text= "Sala modificada con exito")
                        success_label.pack()
                    else:
                        pass
                submit_button = tk.Button(root, text="Aceptar", command=handle_submit)        
                submit_button.pack()  
            else:
                root = tk.Tk()
                error_label = tk.Label(root, text="La pelicula no puede estar vacia")
                error_label.pack()
        sala_button = tk.Button(root, text="Aceptar", command=handle_sala)
        sala_button.pack()      
    modificar_button = tk.Button(root, text="Modificar una sala", command=modificar_sala)
    modificar_button.pack()

    def eliminar_sala():
        root = tk.Tk()
        sala_label = tk.Label(root, text="Ingrese pelicula a eliminar")
        sala_label.pack()
        sala_field = tk.Entry(root)
        sala_field.pack()
        def handle_accept():
            root = tk.Tk()
            pelicula = sala_field.get()
            sala = Sala.salaPorPelicula(pelicula)
            if sala != None:
                Sala.eliminarSala(sala[0])
                eliminado_label = tk.Label(root, text="Sala eliminada con exito!")
                eliminado_label.pack()
            else:
                no_label = tk.Label(root, text="La sala no existe.")
                no_label.pack()
        aceptar_button= tk.Button(root, text="Aceptar", command=handle_accept)
        aceptar_button.pack()
    eliminar_button = tk.Button(root, text="Eliminar una sala", command=eliminar_sala) 
    eliminar_button.pack()   



    def modificar_descuentos():
        # IMPLEMENTAR
        pass


    root.mainloop()
         