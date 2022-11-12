import tkinter as tk
from tkinter import *

class MasterPanel():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('EasyFood')
        self.ventana.geometry("960x540")
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(False,False)

        logo = PhotoImage(file="logo.png")

        label = tk.Label( self.ventana, image=logo,bg='#3a7ff6' )
        label.place(x=0,y=0,relwidth=1, relheight=1)

        self.ventana.mainloop()


