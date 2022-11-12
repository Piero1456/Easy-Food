import pyodbc

class DB():
    def iniciar_conexion_db(self):
        try:
            self.conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=DeliveryRestaurante;UID=lucas;PWD=123')
            print('Conexion exitosa')
            # cursor = connection.cursor()
            # cursor.execute('SELECT @@version')
            # row = cursor.fetchone()
            # print(row)

            # cursor.execute('select * from Paciente')
            # rows = cursor.fetchall()

            # for row in rows:
                # print(row)

            # with connection.cursor() as cursor:
                
            """ cursor.execute('EXEC SEL_EspecialidadesMedicas')
                row = cursor.fetchone()
                while row:
                    # print(row[0])
                    print(row)
                    row = cursor.fetchone() """

            """  cursor.execute('EXEC SEL_HistoriaPaciente 11')
                row = cursor.fetchone()
                while row:
                    print(row)
                    row = cursor.fetchone() """
            """ rows = cursor.fetchall()

                for row in rows:
                    print(row) """

        except Exception as ex:
            print(ex)

        self.cursor = self.conexion.cursor()
        print('Cursor creado')
        # cursor.execute("insert into Medico (nombre, apellido) values('aa', 'XD')")

        # consulta = ("insert into Medico (nombre, apellido) values('aa', 'XD')")
        # cursor.execute(consulta)

        #consulta = ("insert into Usuario (nombre, contrasena) values('a', 'b')")
        #cursor.execute(consulta)
        #self.consulta = ("insert into Usuario (nombre, contrasena) values(?, ?)")
        #print(type(self.consulta))
        #self.cursor.execute(self.consulta, 'aea', 'b')

        #cursor = conexion.cursor()
        #self.cursor.execute('select * from Usuario')
        #rows = self.cursor.fetchall()

        #for row in rows:
            #print(row)

    def agregar_usuario_db(self, usuario, contrasena):
        self.consulta = ("SELECT nombre, contrasena FROM Usuario where nombre = (?)")
        self.cursor.execute(self.consulta, usuario)
        
        aea = self.cursor.fetchall()
        self.contador_usuario_repetido = 0
        for i in aea:
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
        #lista = []
        if self.nombre_usuario != []:
            for i in self.nombre_usuario:
                #lista.append(self.nombre_usuario)
                print(i)
        
        self.consulta = ("SELECT nombre, contrasena FROM Usuario where nombre = (?) and contrasena = (?)")
        self.cursor.execute(self.consulta, usuario, contrasena)
        
        aea = self.cursor.fetchone()
        print(aea)

        if self.nombre_usuario == []:
            lista = [False, 'error de nombre']
            print('El nombre de usuario no existe, debe registrarse.')
            return lista
        elif aea == None:
            lista = [False, 'error de password']
            print('Su contraseña es incorrecta, inténtelo nuevamente.')
            return lista
        else:
            print(f'Usuario encontrado: {aea}')
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