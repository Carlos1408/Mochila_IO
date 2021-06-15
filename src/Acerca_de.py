from tkinter import *

class acerca_de:
    '''Creacion del constructor donde se realiza la creacion de la ventana,
       configuracion de su tamaño,colores, icono y posicion de apertura;Creacion de 
       los labels donde se muestran los datos de los integrantes e informacion
       de las herammientas utilizadas para realizar el proyecto'''
    def __init__(self):
       
        self.ventana = Tk()
        ancho=600
        alto=600
        x=self.ventana.winfo_screenwidth()// 2 - ancho // 2
        y=self.ventana.winfo_screenheight()// 2 - alto // 2
        self.ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
        self.ventana.resizable(0,0)
        self.ventana.title("Acerca de")
        self.ventana.iconbitmap("src/Imagenes/mochila.ico")
        self.ventana.config(bg="gray12")

        #Creacion de titulo
        dinamica=Label(self.ventana,fg="turquoise3",bg= "gray12",font=("Arial",20),width=50)
        dinamica.config(text="Programacion Dinamica: Asignacion Mochila")
        dinamica.pack()


        #Creacion datos integrantes
        self.lb_datos=Label(self.ventana,text="Integrantes",width=20,fg="turquoise3",bg= "gray12",font=("Arial",20))
        self.lb_datos.pack()
        integrantes=Label(self.ventana,fg="turquoise3",bg= "gray12",width=30)
        integrantes.config(text="Alvarez Bustillos Willy Sebastian\nCalle Zapata Raquel Veranda\nClaure Vargas Carlos Manuel\nDiaz Ballejos Edwin")
        integrantes.pack()
 

        #Creacion texto repositorio GitHub
        self.lb_imagenes=Label(self.ventana, text="Repositorio en GitHub",width=30,fg="turquoise3",bg="gray12",font=("Arial",20))
        self.lb_imagenes.pack()
        self.fondo=Entry(self.ventana,width=36)
        self.fondo.config(bg="gray12",fg="turquoise3")
        self.fondo.insert(0,'https://github.com/Carlos1408/Mochila_IO')
        self.fondo.config(state='readonly')
        self.fondo.pack()
        

        #Creacion datos lenguajes, librerias y archivos
        self.lb_lenguaje=Label(self.ventana,text="Lenguaje de Programacion",width=40,fg="turquoise3",bg= "gray12",font=("Arial",20))
        self.lb_lenguaje.pack()
        self.lbl_lenguaje=Label(self.ventana,fg="turquoise3",bg= "gray12",width=40)
        self.lbl_lenguaje.config(text="Python")
        self.lbl_lenguaje.pack()

        self.lb_librerias=Label(self.ventana,text="Librerias",width=40,fg="turquoise3",bg= "gray12",font=("Arial",20))
        self.lb_librerias.pack()
        self.lbl_librerias=Label(self.ventana,fg="turquoise3",bg= "gray12",width=40)
        self.lbl_librerias.config(text="Resolucion del ejercicio: numpy\nInterfaz grafica: tkinter\nPara archivos txt: os\nPara archivos pdf: reportlab")
        self.lbl_librerias.pack()

        self.lb_archivos=Label(self.ventana,text="Archivos",width=40,fg="turquoise3",bg= "gray12",font=("Arial",20))
        self.lb_archivos.pack()
        self.lbl_archivos=Label(self.ventana,fg="turquoise3",bg= "gray12",width=40)
        self.lbl_archivos.config(text="Archivos txt para recuperar y guardar ejercicio\nArchivos pdf para exportar ejercicio")
        self.lbl_archivos.pack()
       

        self.ventana.mainloop()
    
