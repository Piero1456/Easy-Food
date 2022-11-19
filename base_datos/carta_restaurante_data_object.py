from conexion_sqlite import BD
from entities.restaurante import Restaurante
from entities.carta_restaurante import CartaRestaurante

class DAOCartaRestaurante(BD):
    def crear_tabla_carta_restaurante(self, restaurante):
        BD.cursor.execute(f"""CREATE TABLE Carta{restaurante}(
                                plato TEXT NOT NULL)""")
        BD.conexion.commit()
        print('Carta de restaurante creada.')

    def agregar_plato_carta_restaurante(self, restaurante, plato):
        BD.cursor.execute(f"INSERT INTO Carta{restaurante} (plato) values ('{plato}')")
        BD.conexion.commit()
        print('Plato agregado.')

if __name__ == '__main__':
    conexion = BD()
    conexion.iniciar_conexion_db()
    restaurante = Restaurante('Norky\'s')
    plato = CartaRestaurante('Tallarines verdes')
    dao_carta_restaurante = DAOCartaRestaurante()
    dao_carta_restaurante.crear_tabla_carta_restaurante()
    dao_carta_restaurante.agregar_plato_carta_restaurante(restaurante.nombre, plato.nombre_plato)
    conexion.finalizar_conexion_db()