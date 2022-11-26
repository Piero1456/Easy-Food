import base_datos.usuario_data_object as dao_u

class Usuario:
    def __init__(self):
        self.base_datos_usuario = dao_u.DAOUsuario()

    def registro(self, usuario, password):
        if self.base_datos_usuario.agregar_usuario_db(usuario, password):
            return True
        else:
            return False
    
    def login(self, usuario, password):
        self.accede_sistema_usuario = self.base_datos_usuario.buscar_usuario_db(usuario, password)
        if self.accede_sistema_usuario == [False, 'error de nombre']:
            return False
        elif self.accede_sistema_usuario == [False, 'error de password']:
            return False
        else:
            return True