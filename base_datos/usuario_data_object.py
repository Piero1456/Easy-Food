import base_datos.conexion_sqlite as bd
class DAOUsuario(bd.BD):
    def agregar_usuario_db(self, usuario, contrasena):
        bd.BD.cursor.execute(f"SELECT nombre, contrasena FROM Usuario WHERE nombre = ('{usuario}')")
        
        lista_usuarios = self.cursor.fetchall()
        self.contador_usuario_repetido = 0
        for i in lista_usuarios:
            self.contador_usuario_repetido += 1
            print(i)
            print(self.contador_usuario_repetido)

        if self.contador_usuario_repetido >= 1:
            return False
        else:
            bd.BD.cursor.execute(f"insert into Usuario (nombre, contrasena) values('{usuario}', '{contrasena}')")
            bd.BD.conexion.commit()
            print('Usuario agregado.')
            return True

    def buscar_usuario_db(self, usuario, contrasena):
        bd.BD.cursor.execute(f"SELECT nombre, contrasena FROM Usuario where nombre = ('{usuario}')")
        
        self.nombre_usuario = self.cursor.fetchall()
        if self.nombre_usuario != []:
            for i in self.nombre_usuario:
                print(i)
        
        self.cursor.execute(f"SELECT nombre, contrasena FROM Usuario where nombre = ('{usuario}') and contrasena = ('{contrasena}')")
        
        usuario_encontrado = self.cursor.fetchone()
        print(usuario_encontrado)

        if self.nombre_usuario == []:
            lista = [False, 'error de nombre']
            print('El nombre de usuario no existe, debe registrarse.')
            return lista
        elif usuario_encontrado == None:
            lista = [False, 'error de password']
            print('Su contraseña es incorrecta, inténtelo nuevamente.')
            return lista
        else:
            print(f'Usuario encontrado: {usuario_encontrado}')
            return True