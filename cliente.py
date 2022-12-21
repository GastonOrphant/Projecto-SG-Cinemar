import tkinter as tk
from clases.reserva import Reserva
from clases.sala import Sala

def cliente(id):
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Panel de Cliente")

    idCliente = id
    # BOTONES
    def crear_reserva():
        root = tk.Tk()
        root.title("Creación de reservas")
        salas = Sala.verTodas()
        listbox = tk.Listbox(root)
        for sala in salas:
            listbox.insert(tk.END, sala)
        listbox.pack()
        pregunta_label = tk.Label(root, text= "Ingrese la id de la sala en la cual quiere realizar su reserva: ")
        pregunta_label.pack()
        pregunta_field = tk.Entry(root)
        pregunta_field.pack()

        fecha_label = tk.Label(root, text= "Ingrese fecha de la funcion")
        fecha_label.pack()
        fecha_field = tk.Entry(root)
        fecha_field.pack()

        def handle_submit():
            idSala = pregunta_field.get()
            fecha = fecha_field.get()
            if Sala.salaEstaEnBD(idSala):
                reserva = Reserva(idCliente, idSala, fecha)
                reserva.insertarReservaEnBD()
                succes_label = tk.Label(root, text= "Reserva creada con exito!")
                succes_label.pack()
            else:
                error_label = tk.Label(root, text= "La sala ingresada no existe!")
                error_label.pack()    
        submit_button = tk.Button(root, text= "Aceptar", command= handle_submit)
        submit_button.pack()    
    crear_reserva_button = tk.Button(root, text="Crear Reserva", command=crear_reserva)
    crear_reserva_button.pack()

    def ver_mis_reservas():
        root = tk.Tk()
        root.title("Tus Reservas")
        reservas = Reserva.mostrarReservasPorUsuario(idCliente)
        listbox = tk.Listbox(root)
        for reserva in reservas:
            listbox.insert(tk.END, reserva)
        listbox.pack()       
    ver_mis_reservas_button = tk.Button(root, text="Ver mis reservas", command=ver_mis_reservas)
    ver_mis_reservas_button.pack()

    def modificar_reserva():
        root = tk.Tk()
        root.title = "Modificación de Reservas"
        ver_mis_reservas()
        id_label = tk.Label(root, text="Ingrese el id de la reserva a modificar: ")
        id_label.pack()
        id_field = tk.Entry(root)
        id_field.pack()
        def handle_aceptar():
            idReserva = id_field.get()
            salas = Sala.verTodas()
            listbox = tk.Listbox(root)
            for sala in salas:
                listbox.insert(tk.END, sala)
            listbox.pack()
            nueva_sala_label = tk.Label(root, text="Ingrese el id de su nueva sala")
            nueva_sala_label.pack()
            nueva_sala_field = tk.Entry(root)
            nueva_sala_field.pack()
            fecha_label = tk.Label(root, text= "Ingrese fecha de la funcion")
            fecha_label.pack()
            fecha_field = tk.Entry(root)
            fecha_field.pack()
            def handle_submit():
                idSala = nueva_sala_field.get()
                fecha = fecha_field.get()
                if Sala.salaEstaEnBD(idSala):
                    Reserva.modificarReserva(idReserva, idSala, fecha)
                    succes_label = tk.Label(root, text= "Reserva creada con exito!")
                    succes_label.pack()
                else:
                    error_label = tk.Label(root, text= "La sala ingresada no existe!")
                    error_label.pack()
                root.destroy()        
            submit_button = tk.Button(root, text= "Aceptar", command= handle_submit)
            submit_button.pack()  
        aceptar_button = tk.Button(root, text="Aceptar", command=handle_aceptar)
        aceptar_button.pack()
    modificar_reserva_button = tk.Button(root, text="Modificar Reserva", command=modificar_reserva)
    modificar_reserva_button.pack()

    def ver_salas():
        root = tk.Tk()
        root.title("SALAS")
        salas = Sala.verTodas()
        listbox = tk.Listbox(root)
        for sala in salas:
            listbox.insert(tk.END, sala)
        listbox.pack()    
    ver_salas_button = tk.Button(root, text="Ver salas", command=ver_salas)
    ver_salas_button.pack()    



    def historico_entradas(idCliente):
        # IMPLEMENTAR
        pass
    
    root.mainloop()