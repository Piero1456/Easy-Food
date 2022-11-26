from base_datos.carta_restaurante_data_object import DAOCartaRestaurante
class CartaRestaurante:
    def __init__(self):
        self.base_datos_carta_restaurante = DAOCartaRestaurante()

    def verificar_existencia_restaurante(self, restaurante):
        return self.base_datos_carta_restaurante.verificar_existencia_restaurante_bd(restaurante)

    def listar_platos_carta_restaurante(self, restaurante):
        return self.base_datos_carta_restaurante.listar_platos_carta_restaurante_bd(restaurante)

    def crear_tabla_carta_restaurante(self, restaurante):
        self.base_datos_carta_restaurante.crear_tabla_carta_restaurante_bd(restaurante)

    def agregar_plato_carta_restaurante(self, restaurante, plato):
        self.base_datos_carta_restaurante.agregar_plato_carta_restaurante_bd(restaurante, plato)

    def modificar_plato_carta_restaurante(self, restaurante, id, plato):
        self.base_datos_carta_restaurante.modificar_plato_carta_restaurante_bd(restaurante, id, plato)

    def eliminar_plato_carta_restaurante(self, restaurante, plato):
        self.base_datos_carta_restaurante.eliminar_plato_carta_restaurante_bd(restaurante, plato)