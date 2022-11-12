from email.errors import MessageError
from tkinter import StringVar, messagebox
from tkinter import *

class Usuario:
    def registro(self, usuario, password, bd):
        if bd.agregar_usuario_db(usuario, password):
            return True
        else:
            return False
        
    #Permite acceder al programa
    def login(self, usuario, password, bd):
        self.login_admitido = bd.buscar_usuario_db(usuario, password)
        if self.login_admitido == [False, 'error de nombre']:
            return False
        elif self.login_admitido == [False, 'error de password']:
            return False
        else:
            return True
    
