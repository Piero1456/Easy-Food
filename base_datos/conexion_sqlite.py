import sqlite3
import sys

class BD():
    contador_conexion = 0
    conexion = None
    cursor = None
    conexion_exitosa = None
    conexion_finalizada = None

    def iniciar_conexion_db(self):
        BD.contador_conexion += 1
        if BD.contador_conexion == 1:
            try:
                BD.conexion = sqlite3.connect('base_datos/EasyFood.db')
                print('Conexion exitosa')
                BD.conexion_exitosa = True
                BD.cursor = BD.conexion.cursor()
                print('Cursor creado')
                
            except Exception as ex:
                print(ex)
                BD.conexion_exitosa = False
                sys.exit("error en conexion a base de datos")
            

    def finalizar_conexion_db(self):
        BD.cursor.close()
        #BD.cursor.close()
        print('Cursor cerrado')
        BD.conexion.close()
        print('Conexion finalizada')
        BD.conexion_finalizada = True