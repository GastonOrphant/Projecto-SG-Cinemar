from clases.usuario import Usuario
import administracion
from BDD.conexion import Conexion_BD
from tkinter import ttk
from datetime import date

#En la base de datos se reconocerá a un administrador si la variable tipoUsuario es igual a 1
def crearAdmin(datos):
    conn.consult(f'INSERT INTO usuario VALUES (NULL, {datos}, 1)')
    conn.commit()

def crearCliente(datos):
    conn.consult(f'INSERT INTO usuario VALUES (NULL, {datos}, 0)')
    conn.commit()

def imprimirClientes():
    datos = conn.consult('SELECT * FROM usuario').fetchall()
    for dato in datos:
        print(dato)
     
#Administracion

#Manejo de descuentos

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



#PRUEBITA
conn = Conexion_BD('database/Cinemar.db')
#Formato: Nombre, mail, password
crearAdmin('"Gaston", "gaston.orphant@gmail.com", "admin"')
crearCliente('"Hernan", "programadorHernan@gmail.com", "usuario"')
imprimirClientes()
conn.close()


