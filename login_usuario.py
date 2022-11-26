import tkinter as tk
from tkinter.font import BOLD
import entities.admin as a
from tkinter import ttk as ttk
from tkinter import messagebox
import entities.restaurante_login as r
import entities.usuario as u
import entities.restaurante as r
import entities.carta_restaurante as cr

class LoginUsuario(tk.Toplevel):
    contador_interfaz_login = 0
    contador_frame_restaurantes = 0
    contador_frame_usuario = 0
    contador_frame_platos_restaurantes = 0
    def __init__(self):
        super().__init__()
        self.geometry('800x500')
        self.title('Easyfood - Inicio de sesión - Usuario')
        self.config(bg='#fff', padx=20, pady=20)
        self.resizable(False, False)
        self.disenno_interfaz_login()
        self.usuario = u.Usuario()
        self.carta_restaurante = cr.CartaRestaurante()

    def registro_sistema_usuario(self):
        if not self.nombre_usuario.get() or not self.password.get():
            messagebox.showwarning('Advertencia', 'Rellene los campos para completar su registro.')
        elif self.usuario.registro(self.nombre_usuario.get(), self.password.get()):
            messagebox.showinfo('Información', 'Se ha registrado correctamente.')
        else:
            messagebox.showwarning('Advertencia', 'El nombre de usuario ya está en uso. Intente con otro.')

    def ingresar_sistema_usuario(self):
        if self.usuario.login(self.nombre_usuario.get(), self.password.get()):
            self.frame_usuario()
        else:
            messagebox.showwarning('Advertencia', 'Usuario y/o contraseña incorrectos.')

    def tabla_platos_restaurante_afiliados(self):
        self.id_plato = None
        self.tabla_platos_restaurante = ttk.Treeview(self.frame_platos_restaurantes, columns=('Plato'), height=7) 
        
        self.tabla_platos_restaurante.column('#0', width=50, anchor=tk.W)
        self.tabla_platos_restaurante.column('Plato', width=600, anchor=tk.CENTER)

        self.tabla_platos_restaurante.grid(row=1, column=0, columnspan=2, padx=(40, 0), pady=(20, 0))

        self.tabla_platos_restaurante.heading('#0', text='ID', anchor=tk.CENTER)
        self.tabla_platos_restaurante.heading('#1', text='Plato')

        scroll_vertical_tabla_platos_restaurante = tk.Scrollbar(self.frame_platos_restaurantes, command=self.tabla_platos_restaurante.yview)
        scroll_vertical_tabla_platos_restaurante.grid(row=1, column=2, sticky=tk.NS, padx=(0, 10), pady=(20, 0))
        self.tabla_platos_restaurante.configure(yscrollcommand=scroll_vertical_tabla_platos_restaurante.set)

        self.platos_carta_restaurante = self.carta_restaurante.listar_platos_carta_restaurante(self.nombre_restaurante)
        for plato in self.platos_carta_restaurante:
            self.tabla_platos_restaurante.insert('', tk.END, text=plato[0], values=(plato[1],))
            print(plato)

    def frame_platos_restaurantes_afiliados(self):
        LoginUsuario.contador_frame_platos_restaurantes += 1
        if LoginUsuario.contador_frame_usuario >= 1:
            self.frame_restaurantes.destroy()
        
        self.frame_platos_restaurantes = tk.Frame(self, bg='#fcfcfc')
        self.frame_platos_restaurantes.pack(expand=True, fill=tk.BOTH)

        boton_atras = tk.Button(self.frame_platos_restaurantes, text="Atrás",
        font=('Times', 15, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.frame_restaurantes_afiliados, padx=20)
        boton_atras.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        boton_atras.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        boton_atras.bind("<Return>", (lambda event: self.frame_restaurantes_afiliados()))
        boton_atras.place(x=600, y=0)

        self.label_platos_restaurantes_afiliados = tk.Label(self.frame_platos_restaurantes, text=f'Platos del restaurante {self.nombre_restaurante}',
        font=('Times', 18), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.label_platos_restaurantes_afiliados.grid(row=0, column=0, columnspan=3)
        self.tabla_platos_restaurante_afiliados()
        self.logo_platos_restaurantes_afiliados = tk.PhotoImage(file='platos_restaurantes.png')
        self.logo_platos_restaurantes_afiliados = self.logo_platos_restaurantes_afiliados.subsample(3)
        self.label_logo_platos_restaurantes_afiliados = tk.Label(self.frame_platos_restaurantes, image=self.logo_platos_restaurantes_afiliados)
        self.label_logo_platos_restaurantes_afiliados.grid(row=2, column=0, columnspan=3, pady=(20, 0))


    def tabla_restaurantes_afiliados(self):
        self.nombre_restaurante = None
        self.tabla_restaurantes = ttk.Treeview(self.frame_restaurantes, columns=('Restaurante', 'Horario'), height=7)
        
        self.tabla_restaurantes.column('#0', width=50, anchor=tk.W)
        self.tabla_restaurantes.column('Restaurante', width=200, anchor=tk.CENTER)
        self.tabla_restaurantes.column('Horario', width=400, anchor=tk.CENTER)

        self.tabla_restaurantes.grid(row=1, column=0, columnspan=2, padx=(40, 0), pady=(20, 0))

        self.tabla_restaurantes.heading('#0', text='ID', anchor=tk.CENTER)
        self.tabla_restaurantes.heading('#1', text='Restaurante')
        self.tabla_restaurantes.heading('#2', text='Horario')

        scroll_vertical_tabla_restaurantes = tk.Scrollbar(self.frame_restaurantes, command=self.tabla_restaurantes.yview)
        scroll_vertical_tabla_restaurantes.grid(row=1, column=2, sticky=tk.NS, padx=(0, 10), pady=(20, 0))
        self.tabla_restaurantes.configure(yscrollcommand=scroll_vertical_tabla_restaurantes.set)

        self.restaurante = r.Restaurante()
        for restaurante in self.restaurante.listar_restaurantes():
            self.tabla_restaurantes.insert('', tk.END, text=restaurante[0],
            values=(restaurante[1], restaurante[6]))
            print(restaurante)

        def restaurante_seleccionado(event):
            self.boton_platos_restaurantes_afiliados.config(state=tk.NORMAL)
            registro_seleccionado = self.tabla_restaurantes.focus()
            if not registro_seleccionado:
                return None
            data = self.tabla_restaurantes.item(registro_seleccionado)
            (self.id_plato) = data["text"]
            (self.nombre_restaurante, horario) = data["values"]
        self.tabla_restaurantes.bind("<<TreeviewSelect>>", restaurante_seleccionado)

    def frame_restaurantes_afiliados(self):
        LoginUsuario.contador_frame_restaurantes += 1
        if LoginUsuario.contador_frame_usuario >= 1:
            self.frame_interfaz_usuario.destroy()
        if LoginUsuario.contador_frame_restaurantes > 1:
            self.frame_restaurantes.destroy()
        if LoginUsuario.contador_frame_platos_restaurantes >= 1:
            self.frame_platos_restaurantes.destroy()
        
        self.frame_restaurantes = tk.Frame(self, bg='#fcfcfc')
        self.frame_restaurantes.pack()

        boton_atras = tk.Button(self.frame_restaurantes, text="Atrás",
        font=('Times', 15, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.frame_usuario, padx=20)
        boton_atras.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        boton_atras.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        boton_atras.bind("<Return>", (lambda event: self.frame_usuario()))
        boton_atras.place(x=600, y=0)

        self.label_restaurantes_afiliados = tk.Label(self.frame_restaurantes, text='Restaurantes afiliados',
        font=('Times', 18), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.label_restaurantes_afiliados.grid(row=0, column=0, columnspan=3)
        self.tabla_restaurantes_afiliados()
        self.boton_platos_restaurantes_afiliados = tk.Button(self.frame_restaurantes, text='Platos del restaurante seleccionado',
        font=('Times', 15, 'bold'), bg='#343434', bd=0, fg="#fff",command=self.frame_platos_restaurantes_afiliados, state=tk.DISABLED)
        self.boton_platos_restaurantes_afiliados.grid(row=2, column=0, pady=(20, 0))

        self.logo_restaurantes_afiliados = tk.PhotoImage(file='restaurantes_afiliados.png')
        self.logo_restaurantes_afiliados = self.logo_restaurantes_afiliados.subsample(3)
        self.label__logo_restaurantes_afiliados = tk.Label(self.frame_restaurantes, image=self.logo_restaurantes_afiliados)
        self.label__logo_restaurantes_afiliados.grid(row=2, column=1, pady=(20, 0))

    def frame_usuario(self):
        LoginUsuario.contador_frame_usuario += 1
        if LoginUsuario.contador_frame_usuario >=  1:
            self.frame_logo.destroy()
            self.frame_form.destroy()
        if LoginUsuario.contador_frame_restaurantes >= 1:
            self.frame_restaurantes.destroy()

        self.frame_interfaz_usuario = tk.Frame(self, bg='#fcfcfc')
        self.frame_interfaz_usuario.pack()

        self.logo = tk.PhotoImage(file='logo_easy_food.png')
        frame_logo = tk.Frame(self.frame_interfaz_usuario, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=self.logo, bg='#000')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        frame_form = tk.Frame(self.frame_interfaz_usuario, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        boton_atras = tk.Button(frame_form, text="Atrás",
        font=('Times', 15, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.disenno_interfaz_login, padx=20)
        boton_atras.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        boton_atras.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        boton_atras.bind("<Return>", (lambda event: self.disenno_interfaz_login()))
        boton_atras.place(x=250, y=0)

        self.titulo_usuario = tk.Label(frame_form, text="Bienvenido, usuario", font=('Times', 30), fg="#666a88", bg='#fcfcfc')
        self.titulo_usuario.grid(row=0, column=0, padx=(50, 0), pady=(40, 0))

        frame_form_top = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.grid(row=1, column=0)

        self.boton_restaurantes_afiliados = tk.Button(frame_form, text="Restaurantes afiliados",
        font=('Times', 15, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.frame_restaurantes_afiliados)
        self.boton_restaurantes_afiliados.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_restaurantes_afiliados.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        self.boton_restaurantes_afiliados.bind("<Return>", (lambda event: self.frame_restaurantes_afiliados()))
        self.boton_restaurantes_afiliados.grid(row=2, column=0, columnspan=2, pady=(50, 0), padx=(50, 0))

        self.boton_realizar_pedido = tk.Button(frame_form, text="Realizar pedido", font=('Times', 15, 'bold'), bg='#343434', bd=0,
                            fg="#fff")
        self.boton_realizar_pedido.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_realizar_pedido.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        self.boton_realizar_pedido.grid(row=3, column=0, pady=(80, 0), padx=(50, 0))

        self.boton_informacion = tk.Button(frame_form, text="Información", font=('Times', 15, 'bold'), bg='#343434', bd=0,
                            fg="#fff")
        self.boton_informacion.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_informacion.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        self.boton_informacion.grid(row=4, column=0, columnspan=2, pady=(80, 0), padx=(50, 0))

    def disenno_interfaz_login(self):
        LoginUsuario.contador_interfaz_login += 1
        if LoginUsuario.contador_interfaz_login > 1:
            self.frame_interfaz_usuario.destroy()
        self.logo = tk.PhotoImage(file='logo_easy_food.png')
        
        self.frame_logo = tk.Frame(self, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        self.frame_logo.grid(row=0, column=0)
        self.label = tk.Label(self.frame_logo, image=self.logo, bg='#000', width=380, height=420)
        self.label.pack(expand=True, fill='both')

        self.frame_form = tk.Frame(self, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form.grid(row=0, column=1, padx=50)

        self.frame_form_top = tk.Frame(self.frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        self.frame_form_top.grid(row=0, column=0)
        self.title = tk.Label(self.frame_form_top, text="Inicio de sesión", font=('Times', 30), fg="#666a88", bg='#fcfcfc',
                        pady=30)
        self.title.pack(expand=tk.YES, fill=tk.BOTH)

        self.etiqueta_usuario = tk.Label(self.frame_form, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        self.etiqueta_usuario.grid(row=1, column=0, sticky=tk.W)
        self.nombre_usuario = ttk.Entry(self.frame_form, font=('Times', 14), width=30)
        self.nombre_usuario.grid(row=2, column=0, sticky=tk.W)

        self.etiqueta_password = tk.Label(self.frame_form, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                    anchor="w")
        self.etiqueta_password.grid(row=3, column=0, sticky=tk.W, pady=(30, 0))
        self.password = ttk.Entry(self.frame_form, font=('Times', 14), width=30)
        self.password.grid(row=4, column=0, sticky=tk.W)
        self.password.config(show="*")

        self.inicio = tk.Button(self.frame_form, text="Iniciar sesion", font=('Times', 15, BOLD), bg='#343434', bd=0,
                        fg="#fff", command=self.ingresar_sistema_usuario)
        self.inicio.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.inicio.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        self.inicio.grid(row=5, column=0, pady=30, sticky=tk.NSEW)
        self.inicio.bind("<Return>", (lambda event: self.ingresar_sistema_usuario()))

        self.boton_registro = tk.Button(self.frame_form, text="Registrarse", font=('Times', 15, BOLD), bg='#343434', bd=0,
                        fg="#fff", command=self.registro_sistema_usuario)
        self.boton_registro.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_registro.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        self.boton_registro.grid(row=6, column=0, sticky=tk.NSEW)
        self.boton_registro.bind("<Return>", (lambda event: self.registro_sistema_usuario()))