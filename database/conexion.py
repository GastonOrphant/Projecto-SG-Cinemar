import sqlite3

class Conexion_BD():
    def __init__(self):
        self.conexion = sqlite3.connect('cinemar.db')
        self.cursor = self.conexion.cursor()

    def consult(self, consulta):
      if consulta.upper().startswith("SELECT"):
        data = self.cursor.execute(consulta)
        return data
      else:
        self.cursor.execute(consulta)

    def commit(self):
        self.conexion.commit()

    def close(self):
        self.conexion.close()

        