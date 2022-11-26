from base_datos.conexion_sqlite import BD

class DAOCartaRestaurante(BD):
    def verificar_existencia_restaurante_bd(self, restaurante):
        BD.cursor.execute(f"SELECT * FROM Restaurante where nombre = '{restaurante}'")

        restaurantes = self.cursor.fetchall()
        restaurante_existe = False
        for r in restaurantes:
            print(r[1])
            if r[1] == restaurante:
                restaurante_existe = True

        print(restaurante_existe)
        
        if restaurante_existe:
            return True
        else:
            return False

    def listar_platos_carta_restaurante_bd(self, restaurante):
        BD.cursor.execute(f"SELECT * FROM Carta{restaurante}")

        lista_platos = self.cursor.fetchall()
        for plato in lista_platos:
            print(plato)
        
        return lista_platos

    def crear_tabla_carta_restaurante_bd(self, restaurante):
        BD.cursor.execute(f"""CREATE TABLE Carta{restaurante}(
                                id INTEGER,  
                                plato TEXT NOT NULL,
                                PRIMARY KEY(id AUTOINCREMENT))""")
        BD.conexion.commit()
        print('Carta de restaurante creada.')

    def agregar_plato_carta_restaurante_bd(self, restaurante, plato):
        BD.cursor.execute(f"INSERT INTO Carta{restaurante} (plato) values ('{plato}')")
        BD.conexion.commit()
        print('Plato agregado.')

    def modificar_plato_carta_restaurante_bd(self, restaurante, id, plato):
        BD.cursor.execute(f"UPDATE Carta{restaurante} SET plato = '{plato}' WHERE id = {id}")
        BD.conexion.commit()
        print('Plato modificado.')

    def eliminar_plato_carta_restaurante_bd(self, restaurante, plato):
        BD.cursor.execute(f"DELETE FROM Carta{restaurante} WHERE plato = '{plato}'")
        BD.conexion.commit()
        print('Plato eliminado.')