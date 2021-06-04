from tkinter import *
from tkinter import filedialog as fd
import os
from nuevo_problema import nuevo_problema

class principal:
    def __init__(self):
        #Creacion de otras Ventanas
            
        # Creacion de la ventana principal
        
        self.principal = Tk()
        ancho=600
        alto=400
        x=self.principal.winfo_screenwidth()// 2 - ancho // 2
        y=self.principal.winfo_screenheight()// 2 - alto // 2
        self.principal.geometry(f'{ancho}x{alto}+{x}+{y}')
        self.principal.resizable(0,0)
        self.principal.title("Ventana principal")
        self.principal.config(bg="linen")

        # Creacion de la barra de menus
        self.barra_menu = Menu(self.principal)

        # Creacion de menus
        self.archivo = Menu(self.barra_menu)
        self.acerca_de = Menu(self.barra_menu)

        # Creacion de los comandos para menu archivo
        self.archivo.add_command(label="Nuevo Problema", command=self.abrir_nuevo)
        self.archivo.add_command(label="Cargar problema", command= self.recuperar)
        self.archivo.add_command(label="Guardar", command=self.guardar)
        self.archivo.add_command(label="Salir")

        # Agregar los menus a la barra de menus
        self.barra_menu.add_cascade(label="Archivo", menu=self.archivo)
        self.barra_menu.add_cascade(label="Acerca de", menu=self.acerca_de)

        # Agregar la barra a principal
        self.principal.config(menu=self.barra_menu)

        self.principal.mainloop()


    #Creacion de otras funciones
    def abrir_nuevo(self):
        self.principal.destroy()
        nuevo_problema()

    def guardar(self):
        nombre_archivo=fd.asksaveasfilename(initialdir = os.getcwd() ,title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombre_archivo!='':
            archivo=open(nombre_archivo + ".txt", "w", encoding="utf-8")
            archivo.write(self.scrolledtext1.get("1.0", END))
            archivo.close()

    def recuperar(self):
        nombre_archivo=fd.askopenfilename(initialdir = os.getcwd() ,title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombre_archivo!='':
            archivo=open(nombre_archivo, "r", encoding="utf-8")
            contenido=archivo.read()
            archivo.close()
            self.scrolledtext1.delete("1.0", END) 
            self.scrolledtext1.insert("1.0", contenido)