class RestauranteLogin:
    def __init__(self):
        self.__nombre_usuario = 'Restaurante'
        self.__password = '456'

    def login(self, usuario, password):
        self.accede_sistema_restaurante = False
        if usuario == self.__nombre_usuario and password == self.__password:
            self.accede_sistema_restaurante = True