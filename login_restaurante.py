import tkinter as tk
from tkinter.font import BOLD
import entities.admin as a
from tkinter import ttk as ttk
from tkinter import messagebox
import entities.restaurante_login as r_l
import entities.restaurante as r
import entities.carta_restaurante as cr

class LoginRestaurante(tk.Toplevel):
    contador_frame_interfaz_login = 0
    contador_frame_restaurante = 0
    def __init__(self):
        super().__init__()
        self.geometry('800x500')
        self.title('Easyfood - Inicio de sesión - Restaurante')
        self.config(bg='#fff', padx=20, pady=20)
        self.resizable(False, False)
        self.disenno_interfaz_login()
        self.restaurante_login = r_l.RestauranteLogin()
        self.restaurante = r.Restaurante()

    def fin_programa(self):
        self.destroy()

    def modificar_datos(self):
        if (self.nombre_restaurante.get() and self.razon_social.get() and
        self.ruc.get() and self.direccion.get() and self.telefono.get() and self.horario.get()):
            try:
                int(self.ruc.get())
                int(self.telefono.get())
                if self.restaurante.modificar_datos_restaurante(self.nombre_restaurante.get(), self.razon_social.get(),
                self.ruc.get(), self.direccion.get(), self.telefono.get(), self.horario.get()):
                    messagebox.showinfo('Información', 'Datos modificados correctamente.')
                else:
                    messagebox.showwarning('Advertencia', 'El nombre del restaurante no ha sido registrado.')
            except:
                messagebox.showwarning('Advertencia', 'Verifique los datos ingresados.')
            
        else:
            messagebox.showwarning('Advertencia', 'Rellene todos los campos.')

    def registro_sistema_restaurante(self):
        if not self.nombre_usuario.get() or not self.password.get():
            messagebox.showwarning('Advertencia', 'Rellene los campos para completar su registro.')
        elif self.restaurante_login.registro(self.nombre_usuario.get(), self.password.get()):
            messagebox.showinfo('Información', 'Se ha registrado correctamente.')
        else:
            messagebox.showwarning('Advertencia', 'El nombre de usuario ya está en uso. Intente con otro.')

    def ingresar_sistema_restaurante(self):
        if self.restaurante_login.login(self.nombre_usuario.get(), self.password.get()):
            self.frame_restaurante()
        else:
            messagebox.showwarning('Advertencia', 'Usuario y/o contraseña incorrectos.')

    def frame_restaurante(self):
        LoginRestaurante.contador_frame_restaurante += 1
        if LoginRestaurante.contador_frame_interfaz_login >=  1:
            #self.frame_logo.destroy()
            #self.frame_form.destroy()
            self.frame_interfaz_login.destroy()
        if LoginRestaurante.contador_frame_restaurante > 1:
            self.frame_restaurantes.destroy()

        self.frame_restaurantes = tk.Frame(self, bg='#fcfcfc')
        self.frame_restaurantes.pack()

        self.logo = tk.PhotoImage(file='logo_easy_food.png')
        frame_logo = tk.Frame(self.frame_restaurantes, bd=0, width=350, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=self.logo, bg='#000')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        frame_form = tk.Frame(self.frame_restaurantes, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        boton_atras = tk.Button(frame_form, text="Atrás",
        font=('Times', 15, 'bold'), bg='#343434', bd=0, fg="#fff", command=self.disenno_interfaz_login, padx=20)
        boton_atras.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        boton_atras.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        boton_atras.bind("<Return>", (lambda event: self.disenno_interfaz_login()))
        boton_atras.place(x=300, y=0)
        self.titulo_admin = tk.Label(frame_form, text="Bienvenido, restaurante", font=('Times', 30), fg="#666a88", bg='#fcfcfc')
        self.titulo_admin.grid(row=0, column=0, padx=(20, 0), pady=(35, 0))

        frame_form_top = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.grid(row=1, column=0)

        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.grid(row=2, column=0)

        etiqueta_nombre_restaurante = tk.Label(frame_form_fill, text="Nombre", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_nombre_restaurante.grid(row=0, column=0, pady=(30, 0), padx=(0, 70), sticky=tk.W)

        self.nombre_restaurante = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.nombre_restaurante.grid(row=0, column=1, pady=(30, 0))

        self.label_razon_social = tk.Label(frame_form_fill, text="Razón social", font=('Times', 14), fg="#666a88", bg='#fcfcfc')
        self.label_razon_social.grid(row=1, column=0, pady=(20, 0), sticky=tk.W)

        self.razon_social = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.razon_social.grid(row=1, column=1, pady=(20, 0))

        self.label_ruc = tk.Label(frame_form_fill, text="RUC", font=('Times', 14), fg="#666a88", bg='#fcfcfc')
        self.label_ruc.grid(row=2, column=0, pady=(20, 0), sticky=tk.W)

        self.ruc = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.ruc.grid(row=2, column=1, pady=(20, 0))

        self.label_direccion = tk.Label(frame_form_fill, text="Dirección", font=('Times', 14), fg="#666a88", bg='#fcfcfc')
        self.label_direccion.grid(row=3, column=0, pady=(20, 0), sticky=tk.W)

        self.direccion = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.direccion.grid(row=3, column=1, pady=(20, 0))

        self.label_telefono = tk.Label(frame_form_fill, text="Teléfono", font=('Times', 14), fg="#666a88", bg='#fcfcfc')
        self.label_telefono.grid(row=4, column=0, pady=(20, 0), sticky=tk.W)

        self.telefono = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.telefono.grid(row=4, column=1, pady=(20, 0))

        self.label_horario = tk.Label(frame_form_fill, text="Horario", font=('Times', 14), fg="#666a88", bg='#fcfcfc')
        self.label_horario.grid(row=5, column=0, pady=(20, 0), sticky=tk.W)

        self.horario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.horario.grid(row=5, column=1, pady=(20, 0))

        self.boton_modificar_datos = tk.Button(frame_form_fill, text="Modificar", font=('Times', 15, 'bold'), bg='#343434', bd=0,
                            fg="#fff", command=self.modificar_datos)
        self.boton_modificar_datos.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_modificar_datos.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        self.boton_modificar_datos.grid(row=6, column=0, columnspan=2, pady=(30, 0), ipadx=50)

    def disenno_interfaz_login(self):
        LoginRestaurante.contador_frame_interfaz_login += 1
        if LoginRestaurante.contador_frame_restaurante >=  1:
            self.frame_restaurantes.destroy()
        if LoginRestaurante.contador_frame_restaurante > 1:
            self.frame_interfaz_login.destroy()

        self.logo = tk.PhotoImage(file='logo_easy_food.png')
        
        self.frame_interfaz_login = tk.Frame(self, bg='#000')
        self.frame_interfaz_login.pack(fill=tk.BOTH, expand=True)

        self.frame_logo = tk.Frame(self.frame_interfaz_login, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        self.frame_logo.pack(side="left")
        self.label = tk.Label(self.frame_logo, image=self.logo, bg='#000', width=400, height=420, padx=10)
        self.label.pack(expand=True, fill='both')

        self.frame_form = tk.Frame(self.frame_interfaz_login, bd=0, relief=tk.SOLID, bg='#fcfcfc', padx=30)
        self.frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

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
                        fg="#fff", command=self.ingresar_sistema_restaurante)
        self.inicio.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.inicio.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        self.inicio.grid(row=5, column=0, pady=30, sticky=tk.NSEW)
        self.inicio.bind("<Return>", (lambda event: self.ingresar_sistema_restaurante()))

        self.boton_registro = tk.Button(self.frame_form, text="Registrarse", font=('Times', 15, BOLD), bg='#343434', bd=0,
                        fg="#fff", command=self.registro_sistema_restaurante)
        self.boton_registro.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_registro.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        self.boton_registro.grid(row=6, column=0, sticky=tk.NSEW)
        self.boton_registro.bind("<Return>", (lambda event: self.registro_sistema_restaurante()))