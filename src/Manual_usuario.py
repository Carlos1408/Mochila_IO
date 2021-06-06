from tkinter import *
from PIL import ImageTk, Image
class manual_usuario:
    def __init__(self):
        self.ventana = Tk()
        ancho=450
        alto=180
        x=self.ventana.winfo_screenwidth()// 2 - ancho // 2
        y=self.ventana.winfo_screenheight()// 2 - alto // 2
        self.ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
        self.ventana.resizable(0,0)
        self.ventana.title("Manual de Usuario")
        
        img = ImageTk.PhotoImage(Image.open("src/Imagenes/mochila.png"))
        panel = Label(self.ventana, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")