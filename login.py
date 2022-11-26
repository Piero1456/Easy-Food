import tkinter as tk
from tkinter.font import BOLD
import entities.admin as a
from tkinter import ttk as ttk
from tkinter import messagebox
import ventana_admin as m1
import base_datos.conexion_sqlite as bd
import login_usuario as lg_u
import login_restaurante as lg_r

class Login(tk.Tk):
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

    def ingresar_sistema_admin(self):
        self.admin.login(self.nombre_usuario.get(), self.password.get())
        
        if self.admin.accede_sistema_admin:
            self.withdraw()
            self.ventana_principal = m1.VentanaAdmin()
            self.ventana_principal.protocol("WM_DELETE_WINDOW",self.fin_programa)
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
        boton_login_restaurante = tk.Button(self, text='Restaurante', font=('Times', 15, BOLD), bg='#343434', bd=0,
                fg="#fff", command=self.ingresar_ventana_login_restaurante)
        boton_login_restaurante.place(x=460, y=0)

        boton_login_usuario = tk.Button(self, text='Usuario', font=('Times', 15, BOLD), bg='#343434', bd=0,
                fg="#fff", padx=20, command=self.ingresar_ventana_login_usuario)
        boton_login_usuario.place(x=610, y=0)

        self.logo = tk.PhotoImage(file='logo_easy_food.png')
    
        frame_logo = tk.Frame(self, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        frame_logo.grid(row=0, column=0)
        label = tk.Label(frame_logo, image=self.logo, bg='#000', width=380, height=420)
        label.pack(expand=True, fill='both')

        frame_form = tk.Frame(self, bd=0, relief=tk.SOLID, bg='#fcfcfc')
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