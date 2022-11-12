import pyodbc

class DB():
    def iniciar_conexion_db(self):
        try:
            self.conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(local);DATABASE=DeliveryRestaurante;UID=sa;PWD=123')
            print('Conexion exitosa')

        except Exception as ex:
            print(ex)

        self.cursor = self.conexion.cursor()
        print('Cursor creado')
        
    def agregar_usuario_db(self, usuario, contrasena):
        self.consulta = ("SELECT nombre, contrasena FROM Usuario where nombre = (?)")
        self.cursor.execute(self.consulta, usuario)
        
        lista_usuarios = self.cursor.fetchall()
        self.contador_usuario_repetido = 0
        for i in lista_usuarios:
            self.contador_usuario_repetido += 1
            print(i)
            print(self.contador_usuario_repetido)

        if self.contador_usuario_repetido >= 1:
            return False
        else:
            self.consulta = ("insert into Usuario (nombre, contrasena) values(?, ?)")
            self.cursor.execute(self.consulta, usuario, contrasena)
            self.cursor.commit()
            return True

    def buscar_usuario_db(self, usuario, contrasena):
        self.consulta = ("SELECT nombre, contrasena FROM Usuario where nombre = (?)")
        self.cursor.execute(self.consulta, usuario)
        
        self.nombre_usuario = self.cursor.fetchall()
        
        if self.nombre_usuario != []:
            for i in self.nombre_usuario:
                print(i)
        
        self.consulta = ("SELECT nombre, contrasena FROM Usuario where nombre = (?) and contrasena = (?)")
        self.cursor.execute(self.consulta, usuario, contrasena)
        
        usuario_contra = self.cursor.fetchone()

        if self.nombre_usuario == []:
            lista = [False, 'error de nombre']
            print('El nombre de usuario no existe, debe registrarse.')
            return lista
        elif usuario_contra == None:
            lista = [False, 'error de password']
            print('Su contraseña es incorrecta, inténtelo nuevamente.')
            return lista
        else:
            print(f'Usuario encontrado: {usuario_contra}')
            return True

    def finalizar_conexion_db(self):
        self.cursor.close()
        print('Cursor cerrado')
        self.conexion.close()
        print('Conexion finalizada')

if __name__ == '__main__':
    bd = DB()
    bd.iniciar_conexion_db()
    bd.agregar_usuario_db('', '')
    bd.buscar_usuario_db('', '')
    bd.finalizar_conexion_db()
