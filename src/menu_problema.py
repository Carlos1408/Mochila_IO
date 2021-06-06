from tkinter import*
from tkinter import filedialog as fd
import os
import src.principal
import src.nuevo_problema
import src.ingreso_datos
# import src.Solucion.PDF

class menu_problema:
    def __init__(self,v):

        self.ven= Tk()
        self.ven.destroy()
        self.ven= v

        # Creacion de la barra de menus
        barra_menu = Menu(self.ven)

        # Creacion de menus
        archivo = Menu(barra_menu, tearoff=0)
        exportar = Menu(barra_menu,tearoff=0)
        ayuda = Menu(barra_menu,tearoff=0)

        # Creacion de los comandos para menu archivo
        archivo.add_command(label="Nuevo Problema",command=self.nuevo)
        archivo.add_command(label="Cargar problema",command=self.recuperar)
        archivo.add_command(label="Guardar", command=self.guardar)
        archivo.add_separator()
        archivo.add_command(label="Salir",command=self.salir)

        # Creacion de los comandos para menu exportar
        exportar.add_command(label="Como PDF")

        # Creacion de los comandos para menu ayuda
        ayuda.add_command(label="Manual de uso",command=self.ayuda)
        ayuda.add_separator()
        ayuda.add_command(label="Acerca de")

        # Agregar los menus a la barra de menus
        barra_menu.add_cascade(label="Archivo", menu=archivo)
        barra_menu.add_cascade(label="Exportar", menu=exportar)
        barra_menu.add_cascade(label="Ayuda", menu=ayuda)
        
        # Agregar la barra a principal
        self.ven.config(menu=barra_menu)




    def guardar(self):
            nombre_archivo=fd.asksaveasfilename(initialdir = os.getcwd() ,title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
            if nombre_archivo!='':
                archivo=open(nombre_archivo + ".txt", "w", encoding="utf-8")
                print(str(src.ingreso_datos.ingreso_datos.datos()))
                archivo.write(str(src.ingreso_datos.ingreso_datos.datos()))
                archivo.close()
               

    def recuperar(self):
        nombre_archivo=fd.askopenfilename(initialdir = os.getcwd() ,title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        if nombre_archivo!='':
            archivo=open(nombre_archivo, "r", encoding="utf-8")
            contenido=archivo.read()
            archivo.close()

    def salir(self):
        self.ven.destroy()

    def ayuda(self):
        self.ven.destroy()
        src.principal.principal()

    def nuevo(self):
        self.ven.destroy()
        src.nuevo_problema.nuevo_problema()

    # def pdf(self):
    #     src.Solucion.PDF.generarPDF()


    
    
        