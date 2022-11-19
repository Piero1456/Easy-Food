import base_datos.usuario_data_object as dao_u

class Usuario:
    def __init__(self):
        self.__nombre_usuario = 'Usuario'
        self.__password = '789'
        self.base_datos_usuario = dao_u.DAOUsuario()

    def registro(self, usuario, password):
        if self.base_datos_usuario.agregar_usuario_db(usuario, password):
            return True
        else:
            return False
        
    #Permite acceder al programa
    """ def login(self, usuario, password):
        self.accede_sistema_usuario = False
        if usuario == self.__nombre_usuario and password == self.__password:
            self.accede_sistema_usuario = True """
    def login(self, usuario, password):
        #self.accede_sistema_usuario = False
        """ if usuario == self.__nombre_usuario and password == self.__password:
            self.accede_sistema_admin = True
        else:
            self.accede_sistema_usuario = self.base_datos_usuario.buscar_usuario_db(usuario, password)
            if self.accede_sistema_usuario == [False, 'error de nombre']:
                return False
            elif self.accede_sistema_usuario == [False, 'error de password']:
                return False
            else:
                return True """

        self.accede_sistema_usuario = self.base_datos_usuario.buscar_usuario_db(usuario, password)
        if self.accede_sistema_usuario == [False, 'error de nombre']:
            return False
        elif self.accede_sistema_usuario == [False, 'error de password']:
            return False
        else:
            return True