import base_datos.restaurante_login_data_object as dao_r

class RestauranteLogin:
    def __init__(self):
        self.base_datos_restaurante = dao_r.DAORestauranteLogin()

    def registro(self, usuario, password):
        if self.base_datos_restaurante.agregar_usuario_restaurante_db(usuario, password):
            return True
        else:
            return False
    
    def login(self, usuario, password):
        self.accede_sistema_usuario_restaurante = self.base_datos_restaurante.buscar_usuario_restaurante_db(usuario, password)
        if self.accede_sistema_usuario_restaurante == [False, 'error de nombre']:
            return False
        elif self.accede_sistema_usuario_restaurante == [False, 'error de password']:
            return False
        else:
            return True