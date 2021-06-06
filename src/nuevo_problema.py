from tkinter import *
from .ingreso_datos import ingreso_datos
# from principal import principal

class nuevo_problema:

    def __init__(self):
        # Creacion de la ventana nuevo problema
        self.ventana = Tk()
        ancho=450
        alto=180
        x=self.ventana.winfo_screenwidth()// 2 - ancho // 2
        y=self.ventana.winfo_screenheight()// 2 - alto // 2
        self.ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
        self.ventana.resizable(0,0)
        self.ventana.title("Nuevo problema")

        #Etiqueta nombre problema
        self.nombre=Label(self.ventana, text="Nombre del problema")
        self.nombre.grid(column=0,row=0,padx=4,pady=4)
        
        #Caja de texto nombre problema
        self.caja_nombre=StringVar()
        self.texto_nombre=Entry(self.ventana, textvariable = self.caja_nombre)
        self.texto_nombre.grid(column=1,row=0,padx=4,pady=4)


        #Etiqueta capacidad
        self.etiqueta_capacidad=Label(self.ventana, text="Capacidad de la mochila")
        self.etiqueta_capacidad.grid(column=0,row=2,padx=4,pady=4)
        
        #Caja de texto capacidad
        self.caja_capacidad=IntVar()
        self.texto_capacidad=Entry(self.ventana, textvariable = self.caja_capacidad)
        self.texto_capacidad.grid(column=1,row=2,padx=4,pady=4)

        #Etiqueta cantidad
        self.etiqueta_cantidad=Label(self.ventana, text="Cantidad de articulos a asignar")
        self.etiqueta_cantidad.grid(column=0,row=1,padx=4,pady=4)
        
        #Caja de texto cantidad
        self.caja_cantidad=IntVar()
        self.texto_cantidad=Entry(self.ventana, textvariable= self.caja_cantidad)
        self.texto_cantidad.grid(column=1,row=1,padx=4,pady=4)

        #Boton ok
        self.ok=Button(self.ventana, text="OK",command=self.generar_ingreso_datos)
        self.ok.grid(column=0,row=5,padx=1,pady=4)

        #Boton cancelar
        self.cancelar=Button(self.ventana, text="Cancelar",command = self.cancelar)
        self.cancelar.grid(column=1,row=5,padx=4,pady=4)

        self.ventana.mainloop()

    #Creacion de otras Ventanas
    def cancelar(self):
        self.ventana.destroy()
            

    def generar_ingreso_datos(self):
        cantidad = self.caja_cantidad.get()
        capacidad = self.caja_capacidad.get()
        nombre = self.caja_nombre.get()
        print('CANTIDAD ', cantidad)
        print('CAPACIDAD ', capacidad)
        print('NOMBRE ', nombre)
        self.ventana.destroy()
        ingreso_datos(cantidad, capacidad, nombre)
        