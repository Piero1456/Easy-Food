import base_datos.conexion_sqlite as bd

class DAORestaurante(bd.BD):
    def lista_restaurantes_db(self):
        bd.BD.cursor.execute(f"SELECT * FROM Restaurante")
        return self.cursor.fetchall()

    def agregar_restaurante_db(self, nombre):
        bd.BD.cursor.execute(f"SELECT * FROM Restaurante WHERE nombre = ('{nombre}')")
        
        lista_restaurantes = self.cursor.fetchall()
        self.contador_restaurante_repetido = 0
        for i in lista_restaurantes:
            self.contador_restaurante_repetido += 1
            print(i)
            print(self.contador_restaurante_repetido)

        if self.contador_restaurante_repetido >= 1:
            return False
        else:
            bd.BD.cursor.execute(f"insert into Restaurante (nombre) values('{nombre}')")
            bd.BD.conexion.commit()
            print('Restaurante agregado.')
            return True

    def buscar_restaurante_db(self, nombre):
        bd.BD.cursor.execute(f"SELECT * FROM Restaurante WHERE nombre = ('{nombre}')")
        
        self.restaurante = self.cursor.fetchall()
        if self.restaurante != []:
            for i in self.restaurante:
                print(i)

        if self.restaurante == []:
            print('El restaurante no ha sido encontrado.')
            return False
        else:
            print(f'Restaurante encontrado: {self.restaurante}')
            return True

    def modificar_datos_restaurante_db(self, nombre, razon_social, ruc, direccion, telefono, horario):
        bd.BD.cursor.execute(f"""UPDATE Restaurante SET razon_social = '{razon_social}', ruc = {ruc},
        direccion = '{direccion}', telefono = {telefono}, horario = '{horario}' WHERE nombre = '{nombre}'""")

        bd.BD.conexion.commit()
        print(f'Datos del restaurante {nombre} modificados.')