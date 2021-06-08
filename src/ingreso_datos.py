from tkinter import *
# from .menu_problema import menu_problema
from .resultado import resultado
import src.nuevo_problema
from .Solucion.Mochila import Mochila
from .Solucion.Item import Item
import src.Manual_usuario
import src.Acerca_de

class ingreso_datos:
    def __init__(self,cant,cap,nom, formulacion = None):
        self.formulacion = formulacion
        if formulacion is None:
            self.cant = cant
            self.cap = cap
            self.nom = nom
        else:
            self.cant = self.formulacion['cantidad_items']
            self.cap = self.formulacion['capacidad']
            self.nom = self.formulacion['nombre']
        # Creacion de la ventana problema
        self.x=420
        self.y=250
        self.ventana = Tk()
        if(self.cant >=2 and self.cant<=6):
            self.x = self.x + (1*self.cant )
            self.y = self.y + (20*self.cant )
        else:
            self.x = self.x + (2*self.cant )
            self.y = self.y + (30*self.cant )

        self.x1=self.ventana.winfo_screenwidth()// 2 - self.x // 2
        self.y1=self.ventana.winfo_screenheight()// 2 - self.y // 2


        self.ventana.geometry(f'{self.x}x{self.y}+{self.x1}+{self.y1}')
        self.ventana.resizable(0,0)
        self.ventana.title("Asignacion caso mochila")
        self.ventana.iconbitmap("src/Imagenes/mochila.ico")
        self.ventana.config(bg="gray12")
      

         # Creacion de la barra de menus
        barra_menu = Menu(self.ventana)

        # Creacion de menus
        archivo = Menu(barra_menu, tearoff=0)
        ayuda = Menu(barra_menu,tearoff=0)

        # Creacion de los comandos para menu archivo
        archivo.add_command(label="Nuevo Problema",command=self.nuevo)
        archivo.add_separator()
        archivo.add_command(label="Salir",command=self.ventana.quit)


        # Creacion de los comandos para menu ayuda
        ayuda.add_command(label="Manual de uso",command=self.manual)
        ayuda.add_separator()
        ayuda.add_command(label="Acerca de",command=self.acerca)

        # Agregar los menus a la barra de menus
        barra_menu.add_cascade(label="Archivo", menu=archivo)
        barra_menu.add_cascade(label="Ayuda", menu=ayuda)
        
        # Agregar la barra a principal
        self.ventana.config(menu=barra_menu)


        self.etiquetas_datos()

        # Creacion del marco matriz
        self.matriz_problema = Frame(self.ventana,bg="gray12")
        self.genera_matriz()
        if not self.formulacion is None:
            self.auto_completar()
        self.matriz_problema.pack()

        #Boton cancelar
        self.cancelar=Button(self.ventana, text="Cancelar",command=self.cancelar,bg="gray12",fg="turquoise3")
        self.cancelar.pack(side=LEFT,padx=65,pady=15)
        

        #Boton correr
        # self.ok=Button(self.ventana, text="Correr",command=self.get_datos_tabla,bg="lavender")
        self.ok=Button(self.ventana, text="Correr",command=self.solucionar_problema,bg="gray12",fg="turquoise3")
        self.ok.pack(side=RIGHT,padx=70,pady=15)
        
        self.ventana.mainloop()

# Creacion de la funcion que genera la matriz 
    def genera_matriz(self):
        self.matriz = []
        for r in (range(0,self.cant)):
            fila = []
            for c in range(0, 3):
                self.celda = Entry(self.matriz_problema, width=12)
                self.validar(c)
                self.celda.grid(padx=1, pady=1, row=r, column=c)
                self.celda.config(fg="turquoise3",    # letras
                            bg="gray12",   # fondo
                            font=("Verdana",12))
                fila.append(self.celda)
            self.matriz.append(fila)

    
    def generar_ventana_solucion(self, soluciones, pesos, utilidad, formulacion,f_pdf):
        print("self cantidad ",self.cant)
        resultado(self.nom,self.cant, soluciones, pesos, utilidad, f_pdf, formulacion)
        
    def get_datos_tabla(self):
        nombres = []
        pesos = []
        utilidades = []
        for fila in self.matriz:
            nombres.append(fila[0].get())
            pesos.append(int(fila[1].get()))
            utilidades.append(int(fila[2].get()))
        return nombres, pesos, utilidades

    def auto_completar(self):
        items = self.formulacion['items']
        for fila, fila_i in zip(self.matriz, items):
            for dato, celda in zip(fila_i, fila):
                celda.insert(0, dato)

    def solucionar_problema(self):
        # self.auto_completar()
        nombres, pesos, utilidades = self.get_datos_tabla()
        items = []
        for n, p, u in zip(nombres, pesos, utilidades):
            items.append(Item(n, p, u))
        self.mochila = Mochila(self.cap, items)
        self.mochila.set_nombre(self.nom)
        self.mochila.crear_etapas()
        self.mochila.resolver()
        soluciones = self.mochila.get_soluciones()
        pesos_sol = self.mochila.get_pesos_sol()
        utilidad_sol = self.mochila.get_utilidad_neta()
        formulacion = self.mochila.get_formulacion_problema_dicc()
        f_pdf= self.mochila.get_formulacion_problema()
        self.ventana.destroy()
        self.generar_ventana_solucion(soluciones, pesos_sol, utilidad_sol, formulacion, f_pdf)

#Creacion de otras Ventanas
    def cancelar(self):
        self.ventana.destroy()


    def etiquetas_datos(self):

        self.etq_nombre=Label(self.ventana, text=f'Nombre del problema : {self.nom}',bg="gray12",fg="turquoise3")
        self.etq_nombre.pack(side=TOP)

        self.etq_capacidad=Label(self.ventana, text=f'Capacidad de la mochila : {self.cap}',bg="gray12",fg="turquoise3")
        self.etq_capacidad.pack(side=TOP)
        
        self.etq_cantidad=Label(self.ventana, text=f'Cantidad de articulos : {self.cant}',bg="gray12",fg="turquoise3")
        self.etq_cantidad.pack(side=TOP)

        self.etq_datos=Label(self.ventana, text="      Articulos                Peso                     Utilidad",bg="gray12",fg="turquoise3")
        self.etq_datos.pack(side=TOP)

    def nuevo(self):
        self.ventana.destroy()
        src.nuevo_problema.nuevo_problema()

    def manual(self):
        # self.ventana.destroy()
        src.Manual_usuario.manual_usuario()

    def acerca(self):
        # self.ventana.destroy()
        src.Acerca_de.acerca_de()
    
    def validar(self,c):
        if not c == 0:
            self.celda.config(validate="key",validatecommand=(self.matriz_problema.register(self.validar_entry), "%S")) 



    def validar_entry(self,text):
    # solo numeros
        return text.isdigit()