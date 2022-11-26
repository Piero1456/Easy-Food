import sqlite3
import sys

class BD():
    contador_conexion = 0
    conexion = None
    cursor = None

    def iniciar_conexion_db(self):
        BD.contador_conexion += 1
        if BD.contador_conexion == 1:
            try:
                BD.conexion = sqlite3.connect('base_datos/EasyFood.db')
                print('Conexion exitosa')
                
            except Exception as ex:
                print(ex)
                sys.exit("error en conexion a base de datos")
            BD.cursor = BD.conexion.cursor()
            print('Cursor creado')

    def finalizar_conexion_db(self):
        BD.cursor.close()
        print('Cursor cerrado')
        BD.conexion.close()
        print('Conexion finalizada')