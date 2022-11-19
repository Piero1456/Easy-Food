class Admin:
    def __init__(self):
        self.__usuario = 'Admin'
        self.__password = '123'
        #self.base_datos = bd.BD()
        #self.base_datos.iniciar_conexion_db()

    def registro(self, usuario, password):
        if self.base_datos.agregar_usuario_db(usuario, password):
            return True
        else:
            return False
        
    #Permite acceder al programa
    def login(self, usuario, password):
        self.accede_sistema_admin = False
        if usuario == self.__usuario and password == self.__password:
            self.accede_sistema_admin = True
