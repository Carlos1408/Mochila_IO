from tkinter import *
from .nuevo_problema import *
from .menu_problema import *

class resultado:
    def __init__(self,nom, cant, soluciones, pesos, utilidad, formulacion, indice = 0):
       
        # Creacion de la ventana solucion
        self.nom =nom
        self.soluciones=soluciones
        self.cant=cant
        self.utilidad=utilidad
        self.pesos=pesos
        self.formulacion = formulacion
        self.indice = indice

        self.ventana = Tk()
        self.x=550
        self.y=250
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
        self.ventana.config(bg="linen")

        #Llamada al menu problema
        menu_problema(self.ventana, self.formulacion)
       
        self.renderizar_soluciones()

        estado_btn_sgte = DISABLED if self.indice == len(self.soluciones)-1 else ACTIVE
        estado_btn_ant = DISABLED if self.indice == 0 else ACTIVE
        self.btn_anterior=Button(self.ventana, text="anterior",bg="lavender", command=self.ant_solucion, state=estado_btn_ant)
        self.btn_siguiente=Button(self.ventana, text="siguiente",bg="lavender", command=self.sgte_solucion, state=estado_btn_sgte)
        self.btn_anterior.pack(side=LEFT,padx=65,pady=15)
        self.btn_siguiente.pack(side=RIGHT,padx=70,pady=15)

        self.ventana.mainloop()


    def actualizar_ventana(self):
        self.ventana.destroy()
        self.__init__(self.nom,self.cant, self.soluciones, self.pesos, self.utilidad, self.indice)

    def sgte_solucion(self):
        self.indice += 1
        self.actualizar_ventana()

    def ant_solucion(self):
        self.indice -=1
        self.actualizar_ventana()

    def renderizar_soluciones(self):
        datos_sol = f'Nombre del problema: {self.nom}\nSolucion: {self.indice + 1} \nUtilidad total de las soluciones: {self.utilidad} \nProducto            Cantidad                 Peso                Utilidad'
        etiqueta_sol=Label(self.ventana, text=datos_sol, bg="linen")
        self.matriz = Frame(self.ventana)
        self.renderizar_matriz()
        self.etiqueta_peso =Label(self.ventana,bg="linen")
        self.etiqueta_peso.config(text = f'Peso usado: {self.pesos[self.indice]}')
        etiqueta_sol.pack()
        self.matriz.pack()
        self.etiqueta_peso.pack()

    def renderizar_matriz(self):
        solucion = self.soluciones[self.indice]
        for r in range(0,self.cant):
            for c in range(0,4):
                celda = Label(self.matriz, width=12)
                celda.grid(padx=5, pady=5, row=r, column=c)
                celda.config(fg="white",    # letra
                            bg="skyblue",   # caja
                            font=("Verdana",12),
                            text=solucion[r][c])

    