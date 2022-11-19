import tkinter as tk
from tkinter.font import BOLD
import entities.admin as a
from tkinter import ttk as ttk
from tkinter import messagebox
import ventana_admin as m1
import ventana_restaurante as m2
import ventana_usuario as m3
import base_datos.conexion_sqlite as bd
import entities.restaurante_login as r
import entities.usuario as u
from ventana_restaurante import VentanaRestaurante

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
        self.restaurante = r.RestauranteLogin()
        self.usuario = u.Usuario()

    def registro(self):
        if not self.nombre_usuario.get() or not self.nombre_usuario.get():
            messagebox.showwarning('Advertencia', 'Rellene los campos.')
        elif self.usuario.registro(self.nombre_usuario.get(), self.password.get()):
            messagebox.showinfo('Información', 'Se ha registrado correctamente.')
        else:
            messagebox.showwarning('Advertencia', 'El usuario ya ha sido registrado.')

    def ingresar_sistema_admin(self):
        self.admin.login(self.nombre_usuario.get(), self.password.get())
        self.restaurante.login(self.nombre_usuario.get(), self.password.get())
        
        if self.admin.accede_sistema_admin:
            self.withdraw()
            self.ventana_principal = m1.VentanaAdmin()
            self.ventana_principal.protocol("WM_DELETE_WINDOW",self.fin_programa)
        elif self.restaurante.accede_sistema_restaurante:
            self.withdraw()
            self.ventana_principal = m2.VentanaRestaurante()
            self.ventana_principal.protocol("WM_DELETE_WINDOW",self.fin_programa)
        elif self.usuario.login(self.nombre_usuario.get(), self.password.get()):
            self.withdraw()
            self.ventana_principal = m3.VentanaUsuario()
            self.ventana_principal.protocol("WM_DELETE_WINDOW",self.fin_programa)
        else:
            messagebox.showwarning('Advertencia', 'Usuario y/o contraseña incorrectos.')

    def fin_programa(self):
        self.destroy()
        self.base_datos.finalizar_conexion_db()

    def disenno_interfaz_login(self):
        self.logo = tk.PhotoImage(file='logo_easy_food.png')
        
        frame_logo = tk.Frame(self, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=self.logo, bg='#000')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        frame_form = tk.Frame(self, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion", font=('Times', 30), fg="#666a88", bg='#fcfcfc',
                        pady=40)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.nombre_usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.nombre_usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                    anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill, text="Iniciar sesion", font=('Times', 15, BOLD), bg='#343434', bd=0,
                        fg="#fff", command=self.ingresar_sistema_admin)
        inicio.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        inicio.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.ingresar_sistema_admin()))

        registro = tk.Button(frame_form_fill, text="Registrarse", font=('Times', 15, BOLD), bg='#343434', bd=0,
                        fg="#fff", command=self.registro)
        registro.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        registro.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        registro.pack(fill=tk.X, padx=20, pady=20)
        registro.bind("<Return>", (lambda event: self.registro()))

def main():
    raiz = Login()
    raiz.mainloop()

if __name__=='__main__':
    main()