class Admin:
    def __init__(self):
        self.__usuario = 'Admin'
        self.__password = '123'
        
    def login(self, usuario, password):
        self.accede_sistema_admin = False
        if usuario == self.__usuario and password == self.__password:
            self.accede_sistema_admin = True