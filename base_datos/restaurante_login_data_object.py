from base_datos.conexion_sqlite import BD

class DAORestauranteLogin(BD):
    def agregar_usuario_restaurante_db(self, usuario, contrasena):
        BD.cursor.execute(f"SELECT nombre, contrasena FROM RestauranteLogin WHERE nombre = ('{usuario}')")
        
        lista_usuarios_restaurante = self.cursor.fetchall()
        self.contador_usuario_restaurante_repetido = 0
        for i in lista_usuarios_restaurante:
            self.contador_usuario_restaurante_repetido += 1
            print(i)
            print(self.contador_usuario_restaurante_repetido)

        if self.contador_usuario_restaurante_repetido >= 1:
            return False
        else:
            BD.cursor.execute(f"insert into RestauranteLogin (nombre, contrasena) values('{usuario}', '{contrasena}')")
            BD.conexion.commit()
            print('Usuario agregado.')
            return True

    def buscar_usuario_restaurante_db(self, usuario, contrasena):
        BD.cursor.execute(f"SELECT nombre, contrasena FROM RestauranteLogin where nombre = ('{usuario}')")
        
        self.nombre_usuario = self.cursor.fetchall()
        if self.nombre_usuario != []:
            for i in self.nombre_usuario:
                print(i)
        
        self.cursor.execute(f"SELECT nombre, contrasena FROM RestauranteLogin where nombre = ('{usuario}') and contrasena = ('{contrasena}')")
        
        usuario_restaurante_encontrado = self.cursor.fetchone()
        print(usuario_restaurante_encontrado)

        if self.nombre_usuario == []:
            lista = [False, 'error de nombre']
            print('El nombre de usuario no existe, debe registrarse.')
            return lista
        elif usuario_restaurante_encontrado == None:
            lista = [False, 'error de password']
            print('Su contraseña es incorrecta, inténtelo nuevamente.')
            return lista
        else:
            print(f'Usuario de restaurante encontrado: {usuario_restaurante_encontrado}')
            return True