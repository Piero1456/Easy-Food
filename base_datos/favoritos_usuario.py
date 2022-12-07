import base_datos.conexion_sqlite as bd
#from base_datos.conexion_sqlite import BD

class FavUsuario(bd.BD):
    def crear_tabla_fav_usuario(self, usuario):
        bd.BD.cursor.execute(f"""CREATE TABLE Favoritos{usuario}(
                                id INTEGER,  
                                plato TEXT NOT NULL,
                                PRIMARY KEY(id AUTOINCREMENT))""")
        bd.BD.conexion.commit()
        print('Tabla de favoritos creada.')

    def agregar_plato_db(self, usuario, plato):
        bd.BD.cursor.execute(f"SELECT * FROM Favoritos{usuario} WHERE plato = '{plato}'")
        
        lista_platos = self.cursor.fetchall()
        self.contador_plato_repetido = 0
        for i in lista_platos:
            self.contador_plato_repetido += 1
            print(i)
            print(self.contador_plato_repetido)

        if self.contador_plato_repetido >= 1:
            return False
        else:
            bd.BD.cursor.execute(f"insert into Favoritos{usuario} (plato) values('{plato}')")
            bd.BD.conexion.commit()
            print('Plato agregado.')
            return True

    def listar_platos_tabla_fav_usuario_bd(self, usuario):
        bd.BD.cursor.execute(f"SELECT * FROM Favoritos{usuario}")

        lista_platos = self.cursor.fetchall()
        for plato in lista_platos:
            print(plato)
        
        return lista_platos

if __name__ == '__main__':
    b = bd.BD()
    b.iniciar_conexion_db()
    a = FavUsuario()
    #a.crear_tabla_fav_usuario('putamare')
    print(a.listar_platos_tabla_fav_usuario_bd('putamare'))
    a.agregar_plato_db('putamare', 'aea')
    b.finalizar_conexion_db()