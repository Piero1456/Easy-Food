import base_datos.restaurante_data_object as r_dao

class Restaurante:
    def __init__(self) -> None:
        self.base_datos_restaurante = r_dao.DAORestaurante()

    def listar_restaurantes(self):
        return self.base_datos_restaurante.lista_restaurantes_db()

    def agregar_restaurante(self, nombre):
        if self.base_datos_restaurante.agregar_restaurante_db(nombre):
            return True
        else:
            return False

    def modificar_datos_restaurante(self, nombre, razon_social, ruc, direccion, telefono, horario):
        if self.base_datos_restaurante.buscar_restaurante_db(nombre):
            self.base_datos_restaurante.modificar_datos_restaurante_db(nombre, razon_social, ruc, direccion, telefono, horario)
            return True
        else:
            return False