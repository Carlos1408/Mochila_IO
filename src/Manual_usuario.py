from tkinter import *

class manual_usuario:
    def __init__(self):
        self.ventana = Tk()
        ancho=915
        alto=600
        x=self.ventana.winfo_screenwidth()// 2 - ancho // 2
        y=self.ventana.winfo_screenheight()// 2 - alto // 2
        self.ventana.geometry(f'{ancho}x{alto}+{x}+{y}')
        self.ventana.resizable(0,0)
        self.ventana.title("Manual de Usuario")
        self.ventana.iconbitmap("src/Imagenes/mochila.ico")
        self.ventana.config(bg="gray12")
        
        self.scroll=Scrollbar(self.ventana)
        self.scroll.pack(side="right", fill="y") 

        self.manual=Listbox(self.ventana,yscrollcommand=self.scroll.set)
        # self.manual.config(bg="gray12", fg="turqouise3")
        self.manual.pack(expand=YES, fill=BOTH)
        self.manual.insert(END,"BIENVENIDO AL MANUAL DE USUARIO",
            "Aqui aprenderas a usar el programa de la manera correcta :)",
            "-Como crear un nuevo problema",
            "Para crear un nuevo problema debes dirigirte a la parte superior izquierda de la pantalla la que contieie una",
            "pestaña archivo la cual se despliega en un menu de opciones con las siguientes opciones:",
            "*Nuevo problema",
            "*Cargar problema",
            "*Guardar",
            "*Salir",
            "Para crear un nuevo problema hacemos click en la opcion nuevo problema.",
            "Posteriormente nos saldra una ventana para ponerle nombre a nuestro problema y definir la capacidad de la ",
            "mochila y la cantidad de articulos que incluye el problema.",
            "Posteriormente nos aparece una ventana con una matriz para llenar los datos sobre el nombre de los articulos, su",
            "pero y el beneficio que conlleva cada articulo.",
            "Finalmente precionamos el boton de ok para resolver el problema el cual nos muestra todas las soluciones posibles",
            " en caso de haber mas de una por las que podemos navegar con los botones de anterior y siguiente.",
            "-Como guardar los datos de tu problema",
            "Para guardarun nuevo problema debes dirigirte a la parte superior izquierda de la pantalla y en el menu",
            "desplegable de archivo debemos hacer click en la opcion guardar.",
            "Porteriormente nos abrira una ventana que nos muestra una barra para ponerle nombre al archivo, tambien nos",
            "ubicara donde se guardara el archivo de nuestro problema.",
            "-Como cargar datos de un problema anteriormente guardado",
            "Para guardarun nuevo problema debes dirigirte a la parte superior izquierda de la pantalla y en el menu ",
            "desplegable de archivo debemos hacer click en la opcion cargar problema.",
            "Esto nos abrira una ventana que nos mostrara la ubicacion donde por defecto donde se guardan los problemas y",
            "debemos seleccionar el archivo con el nombre que le pusimos al archivo guardado, y hacemos click en abrir.",
            "Posteriormente nos mostrar la ventana donde cargamos datos pero con todos los datos del problema que acabamos",
            "de cargar, entonces solo debemos precionar en ok para que se resuelva y poder tener todas las soluciones",
            "correspondientes.",
            "-como exportar un archivo pdf con el problema y las soluciones posibles",
            "Dentro de la ventana de resultados del problema nos dirigimos a la parte superior izquierda a la pestaña",
            "exportar, en esta pestaña seleccionamos la opcion pdf para que nos genere un archivo pdf con el problema y sus",
            "resultados.", 
            "Este archivo se guardara en la ubicacion por defecto donde se guardan los archivos del problema.")
              
        self.scroll.config(command=self.manual.yview)