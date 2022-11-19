import tkinter as tk
import tkinter.ttk as ttk

class VentanaUsuario(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry('800x500')
        self.title('EasyFood - Usuario')
        self.config(bg='#fff', padx=20, pady=20)
        self.resizable(False, False)
        self.disenno_interfaz()

    def disenno_interfaz(self):
        self.logo = tk.PhotoImage(file='logo_easy_food.png')

        frame_logo = tk.Frame(self, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#000')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=self.logo, bg='#000')
        label.place(x=0, y=0, relwidth=1, relheight=1)

        frame_form = tk.Frame(self, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        self.titulo_admin = tk.Label(frame_form, text="Bienvenido, usuario", font=('Times', 30), fg="#666a88", bg='#fcfcfc')
        self.titulo_admin.grid(row=0, column=0, padx=(50, 0), pady=(40, 0))

        frame_form_top = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.grid(row=1, column=0)

        self.boton_agregar_restaurante = tk.Button(frame_form, text="Restaurantes afiliados", font=('Times', 15, 'bold'), bg='#343434', bd=0,
                            fg="#fff")
        self.boton_agregar_restaurante.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_agregar_restaurante.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        #self.boton_agregar_restaurante.bind("<Return>", (lambda event: self.registro_sistema()))
        self.boton_agregar_restaurante.grid(row=2, column=0, columnspan=2, pady=(50, 0), padx=(50, 0))

        self.boton_agregar_plato = tk.Button(frame_form, text="Carta de restaurantes", font=('Times', 15, 'bold'), bg='#343434', bd=0,
                            fg="#fff")
        self.boton_agregar_plato.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_agregar_plato.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        #self.boton_agregar_plato.bind("<Return>", (lambda event: self.registro_sistema()))
        self.boton_agregar_plato.grid(row=3, column=0, pady=(50, 0), padx=(50, 0))

        self.boton_modificar_plato = tk.Button(frame_form, text="Realizar pedido", font=('Times', 15, 'bold'), bg='#343434', bd=0,
                            fg="#fff")
        self.boton_modificar_plato.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_modificar_plato.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        #self.boton_agregar_plato.bind("<Return>", (lambda event: self.registro_sistema()))
        self.boton_modificar_plato.grid(row=4, column=0, pady=(50, 0), padx=(50, 0))

        self.boton_eliminar_plato = tk.Button(frame_form, text="Información", font=('Times', 15, 'bold'), bg='#343434', bd=0,
                            fg="#fff")
        self.boton_eliminar_plato.bind('<Enter>', lambda e: e.widget.config(bg='#A4A2A2'))
        self.boton_eliminar_plato.bind('<Leave>', lambda e: e.widget.config(bg='#343434'))
        #self.boton_agregar_plato.bind("<Return>", (lambda event: self.registro_sistema()))
        self.boton_eliminar_plato.grid(row=5, column=0, columnspan=2, pady=(50, 0), padx=(50, 0))



if __name__ == '__main__':
    a = VentanaUsuario()
    a.mainloop()