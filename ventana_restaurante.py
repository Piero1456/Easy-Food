import tkinter as tk
import tkinter.ttk as ttk

class VentanaRestaurante(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry('800x500')
        self.title('EasyFood - Restaurante')
        self.config(bg='#fff', padx=20, pady=20)
        self.resizable(False, False)
        self.disenno_interfaz()
        self.protocol("WM_DELETE_WINDOW",self.destroy)

    def disenno_interfaz(self):
        self.logo = tk.PhotoImage(file='logo_easy_food.png')

        frame_logo = tk.Frame(self, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=self.logo, bg='#000')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        frame_form = tk.Frame(self, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.titulo_admin = tk.Label(frame_form, text="Bienvenido, restaurante", font=('Times', 30), fg="#666a88", bg='#fcfcfc')
        self.titulo_admin.grid(row=0, column=0, padx=(20, 0), pady=(10, 0))

        frame_form_top = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg='black')
        #frame_form_top.pack(side="top", fill=tk.X)
        frame_form_top.grid(row=1, column=0)

        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        #frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)
        frame_form_fill.grid(row=2, column=0)

        etiqueta_nombre_restaurante = tk.Label(frame_form_fill, text="Nombre", font=('Times', 14), fg="#666a88", bg='#fcfcfc', anchor="w")
        #etiqueta_usuario_password.pack(fill=tk.X, padx=20, pady=5)
        etiqueta_nombre_restaurante.grid(row=0, column=0, pady=(30, 0), padx=(0, 70), sticky=tk.W)

        self.nombre_restaurante = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.nombre_restaurante.grid(row=0, column=1, pady=(30, 0))

        self.label_razon_social = tk.Label(frame_form_fill, text="Razón social", font=('Times', 14), fg="#666a88", bg='#fcfcfc')
        self.label_razon_social.grid(row=1, column=0, pady=(30, 0), sticky=tk.W)

        self.razon_social = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.razon_social.grid(row=1, column=1, pady=(30, 0))

        self.label_ruc = tk.Label(frame_form_fill, text="RUC", font=('Times', 14), fg="#666a88", bg='#fcfcfc')
        self.label_ruc.grid(row=2, column=0, pady=(30, 0), sticky=tk.W)

        self.ruc = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.ruc.grid(row=2, column=1, pady=(30, 0))

        self.label_direccion = tk.Label(frame_form_fill, text="Dirección", font=('Times', 14), fg="#666a88", bg='#fcfcfc')
        self.label_direccion.grid(row=3, column=0, pady=(30, 0), sticky=tk.W)

        self.direccion = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.direccion.grid(row=3, column=1, pady=(30, 0))

        self.label_telefono = tk.Label(frame_form_fill, text="Teléfono", font=('Times', 14), fg="#666a88", bg='#fcfcfc')
        self.label_telefono.grid(row=4, column=0, pady=(30, 0), sticky=tk.W)

        self.telefono = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.telefono.grid(row=4, column=1, pady=(30, 0))

        self.boton_modificar_datos = tk.Button(frame_form_fill, text="Modificar", font=('Times', 15, 'bold'), bg='#343434', bd=0,
                            fg="#fff")
        self.boton_modificar_datos.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_modificar_datos.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        #self.boton_modificar_datos.bind("<Return>", (lambda event: self.registro_sistema()))
        self.boton_modificar_datos.grid(row=5, column=0, columnspan=2, pady=(40, 0), ipadx=50)


if __name__ == '__main__':
    a = VentanaRestaurante()
    a.mainloop()