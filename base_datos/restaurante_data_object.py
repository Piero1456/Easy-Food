from conexion_sqlite import BD
from entities.restaurante import Restaurante
from entities.carta_restaurante import CartaRestaurante

class DAORestaurante(BD):
    def agregar_restaurante(self, restaurante):
        BD.cursor.execute(f"INSERT INTO Restaurante (nombre) values ('{restaurante}')")
        BD.conexion.commit()
        print('Restaurante agregado.')

if __name__ == '__main__':
    conexion = BD()
    conexion.iniciar_conexion_db()
    restaurante = Restaurante('Pardos')
    dao_restaurante = DAORestaurante()
    plato = CartaRestaurante('Lomo saltado')
    dao_restaurante.agregar_restaurante(restaurante.nombre)
    conexion.finalizar_conexion_db()