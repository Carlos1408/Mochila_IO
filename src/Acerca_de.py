from tkinter import *

class acerca_de:
    def __init__(self):
        self.ventana = Tk()
        ancho=450
        alto=180
        x=self.ventana.winfo_screenwidth()// 2 - ancho // 2
        y=self.ventana.winfo_screenheight()// 2 - alto // 2
        self.ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
        self.ventana.resizable(0,0)
        self.ventana.title("Acerca de")