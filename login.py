import tkinter as tk
from tkinter.font import BOLD
import entities.admin as a
from tkinter import ttk as ttk
from tkinter import messagebox
import base_datos.conexion_sqlite as bd
import login_usuario as lg_u
import login_restaurante as lg_r
import entities.restaurante as r
import entities.carta_restaurante as cr

class Login(tk.Tk):
    contador_interfaz_admin = 0
    contador_frame_admin = 0
    contador_frame_platos = 0
    def __init__(self):
        super().__init__()
        self.geometry('800x500')
        self.title('Easyfood - Inicio de sesión')
        self.config(bg='#fff', padx=20, pady=20)
        self.resizable(False, False)
        self.disenno_interfaz_login()
        self.protocol("WM_DELETE_WINDOW",self.fin_programa)
        self.base_datos = bd.BD()
        self.base_datos.iniciar_conexion_db()
        self.admin = a.Admin()
        self.restaurante = r.Restaurante()
        self.carta_restaurante = cr.CartaRestaurante()

    def agregar_restaurante(self):
        if not self.nombre_restaurante.get():
            messagebox.showwarning('Advertencia', 'Rellene los campos para completar su registro.')
        elif self.restaurante.agregar_restaurante(self.nombre_restaurante.get()):
            self.carta_restaurante.crear_tabla_carta_restaurante(self.nombre_restaurante.get())
            messagebox.showinfo('Información', 'Se ha registrado correctamente.')
        else:
            messagebox.showwarning('Advertencia', 'El nombre de usuario del restaurante ya está en uso. Intente con otro.')

    def agregar_plato(self):
        for plato in self.platos_carta_restaurante:
            if plato[1] == self.nombre_plato.get():
                messagebox.showwarning('Advertencia', 'El plato ya ha sido agregado.')
                return None
        if not self.nombre_plato.get():
            messagebox.showwarning('Advertencia', 'Rellene el campo.')
        else:
            self.carta_restaurante.agregar_plato_carta_restaurante(self.nombre_carta_restaurante.get(),self.nombre_plato.get())
            self.actualizar_tabla_platos()

    def modificar_plato(self):
        for plato in self.platos_carta_restaurante:
            if plato[1] == self.nombre_plato.get():
                messagebox.showwarning('Advertencia', 'El plato ingresado ya existe.')
                return None
        if not self.nombre_plato.get():
            messagebox.showwarning('Advertencia', 'Rellene el campo.')
        else:
            self.carta_restaurante.modificar_plato_carta_restaurante(self.nombre_carta_restaurante.get(), self.id_plato, self.nombre_plato.get())
            self.actualizar_tabla_platos()

    def eliminar_plato(self):
        for plato in self.platos_carta_restaurante:
            if plato[1] != self.nombre_plato.get():
                plato_existe = False
            else:
                plato_existe = True
                break
        if not self.nombre_plato.get():
            messagebox.showwarning('Advertencia', 'Rellene el campo.')
        elif plato_existe == False:
            messagebox.showwarning('Advertencia', 'El plato ingresado no existe.')
            return None
        else:
            self.carta_restaurante.eliminar_plato_carta_restaurante(self.nombre_carta_restaurante.get(), self.nombre_plato.get())
            self.actualizar_tabla_platos()

    def actualizar_tabla_platos(self):
        if self.carta_restaurante.verificar_existencia_restaurante(self.nombre_carta_restaurante.get()):
            self.id_plato = None
            self.nombre_plato.config(state=tk.NORMAL)
            self.boton_agregar_plato.config(state=tk.NORMAL)
            self.boton_modificar_plato.config(state=tk.NORMAL)
            self.boton_eliminar_plato.config(state=tk.NORMAL)
            self.tabla_platos()
            self.platos_carta_restaurante = self.carta_restaurante.listar_platos_carta_restaurante(self.nombre_carta_restaurante.get())
            for plato in self.platos_carta_restaurante:
                self.tabla_platos_restaurante.insert('', tk.END, text=plato[0], values=(plato[1],))
                print(plato[1])

            def plato_seleccionado(event):
                registro_seleccionado = self.tabla_platos_restaurante.focus()
                if not registro_seleccionado:
                    return None
                data = self.tabla_platos_restaurante.item(registro_seleccionado)
                (self.id_plato) = data["text"]
                (plato) = data["values"]

                self.nombre_plato.delete('0', 'end')
                self.nombre_plato.insert(0, plato)

            self.tabla_platos_restaurante.bind("<<TreeviewSelect>>", plato_seleccionado)
        else:
            messagebox.showwarning('Advertencia', 'El restaurante ingresado no existe.')

    def tabla_platos(self):
        self.tabla_platos_restaurante = ttk.Treeview(self.frame_platos_admin, columns=('Plato'), height=5)
        
        self.tabla_platos_restaurante.column('#0', width=50, anchor=tk.W)
        self.tabla_platos_restaurante.column('Plato', width=500, anchor=tk.CENTER)
        self.tabla_platos_restaurante.grid(row=3, column=0, columnspan=3, padx=(40, 0), pady=(20, 0))

        self.tabla_platos_restaurante.heading('#0', text='ID', anchor=tk.CENTER)
        self.tabla_platos_restaurante.heading('#1', text='Plato')

        scroll_vertical_tabla_platos_restaurante = tk.Scrollbar(self.frame_platos_admin, command=self.tabla_platos_restaurante.yview)
        scroll_vertical_tabla_platos_restaurante.grid(row=3, column=3, sticky=tk.NS, padx=(0, 10), pady=(20, 0))
        self.tabla_platos_restaurante.configure(yscrollcommand=scroll_vertical_tabla_platos_restaurante.set)

    def frame_platos(self):
        Login.contador_frame_platos += 1
        if Login.contador_frame_platos >  1:
            self.frame_platos_admin.destroy()
        if Login.contador_frame_admin >= 1:
            self.frame_interfaz_admin.destroy()

        self.frame_platos_admin = tk.Frame(self, bg='#fcfcfc')
        self.frame_platos_admin.pack(fill=tk.BOTH, expand=True)

        boton_atras = tk.Button(self.frame_platos_admin, text="Atrás",
        font=('Times', 15, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.frame_admin, padx=20)
        boton_atras.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        boton_atras.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        boton_atras.bind("<Return>", (lambda event: self.frame_admin()))
        boton_atras.place(x=650, y=0)

        self.label_carta_restaurante = tk.Label(self.frame_platos_admin, text='Nombre del restaurante', font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.label_carta_restaurante.grid(row=0, column=0, columnspan=3, padx=300)
        self.nombre_carta_restaurante = ttk.Entry(self.frame_platos_admin, font=('Times', 14))
        self.nombre_carta_restaurante.grid(row=1, column=0, columnspan=3)
        self.boton_carta_restaurante = tk.Button(self.frame_platos_admin, text="Ver carta del restaurante",
        font=('Times', 14, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.actualizar_tabla_platos)
        self.boton_carta_restaurante.grid(row=2, column=0, columnspan=3, pady=(20, 0))

        self.label_nombre_plato = tk.Label(self.frame_platos_admin, text='Nombre del plato',font=('Times', 14), fg="#666a88",
        bg='#fcfcfc', anchor="w")
        self.label_nombre_plato.grid(row=4, column=0, columnspan=3, pady=(30, 0))
        self.nombre_plato = ttk.Entry(self.frame_platos_admin, font=('Times', 14), width=20, state=tk.DISABLED)
        self.nombre_plato.grid(row=5, column=0, columnspan=3)

        self.boton_agregar_plato = tk.Button(self.frame_platos_admin, text="Agregar plato",
        font=('Times', 14, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.agregar_plato, state=tk.DISABLED)
        self.boton_agregar_plato.grid(row=6, column=0, pady=(20, 0), padx=(0, 20))
        self.boton_modificar_plato = tk.Button(self.frame_platos_admin, text="Modificar plato",
        font=('Times', 14, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.modificar_plato, state=tk.DISABLED)
        self.boton_modificar_plato.grid(row=6, column=1, pady=(20, 0), padx=20)
        self.boton_eliminar_plato = tk.Button(self.frame_platos_admin, text="Eliminar plato",
        font=('Times', 14, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.eliminar_plato, state=tk.DISABLED)
        self.boton_eliminar_plato.grid(row=6, column=2, pady=(20, 0), padx=(20, 0))

    def frame_admin(self):
        Login.contador_frame_admin += 1
        if Login.contador_frame_admin > 1:
            self.frame_interfaz_admin.destroy()
        if Login.contador_frame_platos >= 1:
            self.frame_platos_admin.destroy()
        #if Login.contador_interfaz_admin >= 1:
            #self.interfaf

        self.logo = tk.PhotoImage(file='logo_easy_food.png')

        self.frame_interfaz_admin = tk.Frame(self, bg='#fcfcfc')
        self.frame_interfaz_admin.pack()

        frame_logo = tk.Frame(self.frame_interfaz_admin, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=self.logo, bg='#000')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        frame_form = tk.Frame(self.frame_interfaz_admin, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.titulo_admin = tk.Label(frame_form, text="Bienvenido, administrador", font=('Times', 30), fg="#666a88", bg='#fcfcfc')
        self.titulo_admin.grid(row=0, column=0, padx=(20, 0), pady=(40, 0))

        boton_atras = tk.Button(frame_form, text="Atrás",
        font=('Times', 15, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.disenno_interfaz_login, padx=20)
        boton_atras.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        boton_atras.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        boton_atras.bind("<Return>", (lambda event: self.disenno_interfaz_login()))
        boton_atras.place(x=350, y=0)

        frame_form_top = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.grid(row=1, column=0)

        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.grid(row=2, column=0)

        etiqueta_nombre_restaurante = tk.Label(frame_form_fill, text="Nombre del restaurante", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_nombre_restaurante.grid(row=0, column=0, pady=(30, 0), padx=(0, 20))

        self.nombre_restaurante = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.nombre_restaurante.grid(row=0, column=1, pady=(30, 0))

        self.boton_agregar_restaurante = tk.Button(frame_form_fill, text="Agregar restaurante", font=('Times', 15, 'bold'), bg='#343434', bd=0,
                            fg="#fff", command=self.agregar_restaurante)
        self.boton_agregar_restaurante.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_agregar_restaurante.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        self.boton_agregar_restaurante.grid(row=1, column=0, columnspan=2, pady=(30, 0))
        

        self.frame_plato_carta = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_plato_carta.grid(row=3, column=0, columnspan=2)

        self.imagen_platos = tk.PhotoImage(file='comida.png')
        self.imagen_platos = self.imagen_platos.subsample(4)
        self.label_imagen_platos = tk.Label(self.frame_plato_carta, image=self.imagen_platos)
        self.label_imagen_platos.grid(row=1, column=0, pady=(30, 0))

        self.boton_lista_platos = tk.Button(self.frame_plato_carta, text="Ver lista de platos", font=('Times', 15, 'bold'), bg='#343434', bd=0,
                            fg="#fff", command=self.frame_platos)
        self.boton_lista_platos.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_lista_platos.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        self.boton_lista_platos.grid(row=2, column=0, pady=(20, 0))

    def ingresar_sistema_admin(self):
        self.admin.login(self.nombre_usuario.get(), self.password.get())
        
        if self.admin.accede_sistema_admin:
            self.interfaz_admin.destroy()
            self.frame_admin()
            #self.withdraw()
            #self.ventana_principal = m1.VentanaAdmin()
            #self.ventana_principal.protocol("WM_DELETE_WINDOW",self.fin_programa)
        else:
            messagebox.showwarning('Advertencia', 'Usuario y/o contraseña incorrectos.')

    def ingresar_ventana_login_usuario(self):
        self.withdraw()
        self.ventana_login_usuario = lg_u.LoginUsuario()
        self.ventana_login_usuario.protocol("WM_DELETE_WINDOW",self.fin_programa)

    def ingresar_ventana_login_restaurante(self):
        self.withdraw()
        self.ventana_login_usuario = lg_r.LoginRestaurante()
        self.ventana_login_usuario.protocol("WM_DELETE_WINDOW",self.fin_programa)

    def fin_programa(self):
        self.destroy()
        self.base_datos.finalizar_conexion_db()

    def disenno_interfaz_login(self):
        if Login.contador_frame_admin >= 1:
            self.frame_interfaz_admin.destroy()
        self.interfaz_admin = tk.Frame(self, bg='#fcfcfc')
        self.interfaz_admin.pack()
        boton_login_restaurante = tk.Button(self.interfaz_admin, text='Restaurante', font=('Times', 15, BOLD), bg='#343434', bd=0,
                fg="#fff", command=self.ingresar_ventana_login_restaurante)
        boton_login_restaurante.place(x=460, y=0)

        boton_login_usuario = tk.Button(self.interfaz_admin, text='Usuario', font=('Times', 15, BOLD), bg='#343434', bd=0,
                fg="#fff", padx=20, command=self.ingresar_ventana_login_usuario)
        boton_login_usuario.place(x=610, y=0)

        self.logo = tk.PhotoImage(file='logo_easy_food.png')
    
        frame_logo = tk.Frame(self.interfaz_admin, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        frame_logo.grid(row=0, column=0)
        label = tk.Label(frame_logo, image=self.logo, bg='#000', width=380, height=420)
        label.pack(expand=True, fill='both')

        frame_form = tk.Frame(self.interfaz_admin, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.grid(row=0, column=1, padx=50)

        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.grid(row=0, column=0)
        title = tk.Label(frame_form_top, text="Inicio de sesión", font=('Times', 30), fg="#666a88", bg='#fcfcfc',
                pady=30)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.grid(row=1, column=0, sticky=tk.W)
        self.nombre_usuario = ttk.Entry(frame_form, font=('Times', 14), width=30)
        self.nombre_usuario.grid(row=2, column=0, sticky=tk.W)

        etiqueta_password = tk.Label(frame_form, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                            anchor="w")
        etiqueta_password.grid(row=3, column=0, sticky=tk.W, pady=(30, 0))
        self.password = ttk.Entry(frame_form, font=('Times', 14), width=30)
        self.password.grid(row=4, column=0, sticky=tk.W)
        self.password.config(show="*")

        inicio = tk.Button(frame_form, text="Iniciar sesion", font=('Times', 15, BOLD), bg='#343434', bd=0,
                fg="#fff", command=self.ingresar_sistema_admin)
        inicio.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        inicio.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        inicio.grid(row=5, column=0, pady=40, sticky=tk.NSEW)
        inicio.bind("<Return>", (lambda event: self.ingresar_sistema_admin()))