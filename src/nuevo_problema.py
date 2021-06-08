from tkinter import *
import src.ingreso_datos
from tkinter import messagebox as mb

class nuevo_problema:

    def __init__(self):
        # Creacion de la ventana nuevo problema
        self.ventana = Tk()
        ancho=500
        alto=200
        x=self.ventana.winfo_screenwidth()// 2 - ancho // 2
        y=self.ventana.winfo_screenheight()// 2 - alto // 2
        self.ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
        self.ventana.resizable(0,0)
        self.ventana.title("Nuevo problema")
        self.ventana.iconbitmap("src/Imagenes/mochila.ico")
        self.ventana.config(bg="gray12")

        #Etiqueta nombre problema
        self.nombre=Label(self.ventana, text="Nombre del problema",bg="gray12",fg="turquoise3")
        self.nombre.grid(column=0,row=0,padx=8,pady=8)
        
        #Caja de texto nombre problema
        self.texto_nombre=Entry(self.ventana)
        self.texto_nombre.grid(column=1,row=0,padx=8,pady=8)


        #Etiqueta capacidad
        self.etiqueta_capacidad=Label(self.ventana, text="Capacidad de la mochila",bg="gray12",fg="turquoise3")
        self.etiqueta_capacidad.grid(column=0,row=2,padx=8,pady=8)
        
        #Caja de texto capacidad
        self.texto_capacidad=Entry(self.ventana,validate="key",validatecommand=(self.ventana.register(self.validar_entry), "%S"))
        self.texto_capacidad.grid(column=1,row=2,padx=8,pady=8)

        #Etiqueta cantidad
        self.etiqueta_cantidad=Label(self.ventana, text="Cantidad de articulos a asignar",bg="gray12",fg="turquoise3")
        self.etiqueta_cantidad.grid(column=0,row=1,padx=8,pady=8)
        
        #Caja de texto cantidad
        self.texto_cantidad=Entry(self.ventana,validate="key",validatecommand=(self.ventana.register(self.validar_entry), "%S"))
        self.texto_cantidad.grid(column=1,row=1,padx=8,pady=8)

        #Boton ok
        self.ok=Button(self.ventana, text="OK",command=self.llenado,bg="gray12",fg="turquoise3",width=15)
        self.ok.grid(column=0,row=5,padx=1,pady=8)

        #Boton cancelar
        self.salir=Button(self.ventana, text="Salir",command = self.ventana.quit,bg="gray12",fg="turquoise3",width=15)
        self.salir.grid(column=1,row=5,padx=4,pady=8)

        self.ventana.mainloop()

    #Creacion de otras Ventanas

    def generar_ingreso_datos(self):
        cantidad = self.texto_cantidad.get()
        capacidad = self.texto_capacidad.get()
        nombre = self.texto_nombre.get()
        print('CANTIDAD ', cantidad)
        print('CAPACIDAD ', capacidad)
        print('NOMBRE ', nombre)
        self.ventana.destroy()
        src.ingreso_datos.ingreso_datos(int(cantidad), int(capacidad), nombre)

    def validar_entry(self,text):
    # solo numeros
        return text.isdecimal()    

    def llenado(self):
        if self.texto_nombre.get() == "" or self.texto_cantidad.get() == "" or self.texto_capacidad.get()== "" :
           mb.showinfo(message="Debe llenar todos los campos", title="Mensaje")
           self.ventana.destroy()
           nuevo_problema()
        else:
            self.generar_ingreso_datos()
