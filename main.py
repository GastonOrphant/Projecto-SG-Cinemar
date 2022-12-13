import cliente
import administracion
from plugins.conexion import Conexion_BD
from tkinter import *


#En la base de datos se reconocera a un administrador si la variable rol es igual a 1
def crearAdmin(datos):
    conn.consult(f'INSERT INTO usuario VALUES (NULL, {datos}, 1)')
    conn.commit()

def crearCliente(datos):
    conn.consult(f'INSERT INTO usuario VALUES (NULL, {datos}, 0)')
    conn.commit()

#PRUEBITA
conn = Conexion_BD('database/Cinemar.db')
crearAdmin('"Gaston", "gaston.orphant@gmail.com", "admin"')
crearCliente('"Hernan", "programadorHernan@gmail.com", "usuario"')
conn.commit()
datos = conn.consult('SELECT * FROM usuario').fetchall()
for dato in datos:
    print(dato)
conn.close()