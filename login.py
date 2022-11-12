import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import Usuario as u
from master import MasterPanel
from tkinter import messagebox
import conexion_sqlserver as db

class Login(Tk):

    def cerrar_ventana(self):
        self.destroy()
        self.base_datos.finalizar_conexion_db()

    def registro_sistema(self):
        if not self.nombre_usuario.get() or not self.password.get():
            messagebox.showwarning('Advertencia', 'Rellene los campos para completar su registro.')
        elif self.usuario.registro(self.nombre_usuario.get(), self.password.get(), self.base_datos):
            messagebox.showinfo('Información', 'Se ha registrado correctamente.')
        else:
            messagebox.showwarning('Advertencia', 'El nombre de usuario ya está en uso. Intente con otro.')

    def ingresar_sistema(self):
        if not self.nombre_usuario.get() or not self.password.get():
            messagebox.showwarning('Advertencia', 'Rellene los campos para ingresar.')
        elif not self.usuario.login(self.nombre_usuario.get(), self.password.get(), self.base_datos):
            if self.usuario.login_admitido == [False, 'error de nombre']:
                messagebox.showwarning('Advertencia', 'El nombre de usuario no existe, debe registrarse.')
            else:
                messagebox.showwarning('Advertencia', 'Su contraseña es incorrecta, inténtelo nuevamente.')
        else:
            self.destroy()
            MasterPanel()


    def __init__(self) -> None:
        super().__init__()
        self.title('Inicio de sesion')
        self.geometry('800x500')
        self.config(bg='#000')
        self.resizable(True, True)
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.base_datos = db.DB()
        self.base_datos.iniciar_conexion_db()
        self.usuario = u.Usuario()

        logo = PhotoImage(file='logo.PNG')
        # frame_logo
        frame_logo = Frame(self, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#000')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        frame_form = Frame(self, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesion", font=('Times', 30), fg="#666a88", bg='#fcfcfc',
                         pady=50)
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
                           fg="#fff", command=self.ingresar_sistema)
        inicio.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        inicio.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.ingresar_sistema()))

        inicio = tk.Button(frame_form_fill, text="Registrarse", font=('Times', 15, BOLD), bg='#343434', bd=0,
                           fg="#fff", command=self.registro_sistema)
        inicio.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        inicio.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        inicio.pack(fill=tk.X, padx=20, pady=0)
        inicio.bind("<Return>", (lambda event: self.registro_sistema()))



        self.mainloop()


def main():
    raiz = Login()

    raiz.mainloop()


if __name__ == '__main__':
    Login()
