from tkinter import *
from tkinter import filedialog as fd
import os
import src.ingreso_datos
from .nuevo_problema import nuevo_problema
from ast import literal_eval
from .Manual_usuario import manual_usuario
from .Acerca_de import acerca_de


class principal:
    def __init__(self):
            
        # Creacion de la ventana principal
        
        self.principal = Tk()
        ancho=400
        alto=350
        x=self.principal.winfo_screenwidth()// 2 - ancho // 2
        y=self.principal.winfo_screenheight()// 2 - alto // 2
        self.principal.geometry(f'{ancho}x{alto}+{x}+{y}')
        self.principal.resizable(0,0)
        self.principal.title("Ventana principal")
        self.principal.iconbitmap("src/Imagenes/mochila.ico")
        self.principal.config(bg="gray12")

        #Creacion Botones
        self.nuevo=Button(self.principal, text="Nuevo Problema",command=self.nuevo,bg="gray12",fg="turquoise3",width=25)
        self.nuevo.pack(pady=15)
        self.cargar=Button(self.principal, text="Cargar Problema",command=self.recuperar,bg="gray12",fg="turquoise3",width=25)
        self.cargar.pack(pady=15)
        self.manual=Button(self.principal, text="Manual de Usuario",command=self.manual,bg="gray12",fg="turquoise3",width=25)
        self.manual.pack(pady=15)
        self.acerca=Button(self.principal, text="Acerca de",command=self.acerca,bg="gray12",fg="turquoise3",width=25)
        self.acerca.pack(pady=15)
        self.salir=Button(self.principal, text="salir", command=self.principal.quit,bg="gray12",fg="turquoise3",width=12)
        self.salir.pack(side=RIGHT,padx=15)
        
        self.principal.mainloop()

    def nuevo(self):
        self.principal.destroy()
        nuevo_problema()

    def recuperar(self):
        nombre_archivo=fd.askopenfilename(initialdir = os.getcwd() ,title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombre_archivo!='':
            archivo=open(nombre_archivo, "r", encoding="utf-8")
            contenido=archivo.read()
            print(contenido)
            archivo.close()
        print('RECUPERACION DE DATOS')
        src.ingreso_datos.ingreso_datos(0, 0, 0, literal_eval(contenido))

    def manual(self):
        # self.principal.destroy()
        path = 'src/Solucion/Anvorgueso.pdf'
        os.system(path)

    def acerca(self):
        # self.principal.destroy()
        acerca_de()
        
        