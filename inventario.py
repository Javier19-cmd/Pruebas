"""
@Auth: Javier Sebastián Valle Balsells 
@Date: 2/11/20201
@Proposal: Inventario de cosas.

Sección de Referencias:
Crear una ventana desde un método: https://www.youtube.com/watch?v=LbcVdgFUslk&ab_channel=LuisAlvarado
Crear gráficos con Mathplotlib: https://www.youtube.com/watch?v=5OKzCXha4Co&t=104s&ab_channel=MagnoEfren
"""
from tkinter import * #Importando todo lo de tkinter por prevención.
import pandas as pd #Importando pandas para estadísticas. 
import openpyxl
import csv
import matplotlib.pyplot as plt #Nuevo import
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #Nuevo import.

#Propieades de la ventana que ingresa los datos al csv.
ventana = Tk()
ventana.config(bg="black")
ventana.geometry("560x388")
ventana.resizable(0,0)
ventana.title("Guardar entrada del inventario de venta de caballos")

"""
#wb = openyxl.Workbook()
#Propieades de la ventana que ingresa los datos al csv.
ventana2 = Tk()
ventana2.config(bg="white")
ventana2.geometry("560x388")
ventana2.resizable(0,0)
ventana2.title("Ver el inventario de venta de caballos")
"""

#Listas de los objetos.
tipo_objeto, talla_objeto, color_objeto, id_objeto = [],[],[],[] 

#Agregar dato al inventario.
def agregar_datos():
    #Variables globales de las listas.
    global tipo_objeto, talla_objeto, color_objeto, id_objeto 

    #Agregando lo que ingresó el usuario en los textboxes a las listas.
    tipo_objeto.append(ingresa_tipo.get())
    talla_objeto.append(ingresa_talla.get())
    color_objeto.append(ingresa_color.get())
    id_objeto.append(ingresa_ide.get())

    
    #Eliminando el texto que ya se agregó anteriormente.
    ingresa_tipo.delete(0, END)
    ingresa_talla.delete(0, END)
    ingresa_color.delete(0, END)
    ingresa_ide.delete(0, END)

#Guardando datos
def guardar_datos():
    #Variables globales de las listas.
    global tipo_objeto, talla_objeto, color_objeto, id_objeto

    datos = [{"Tipo":tipo_objeto, "Talla":talla_objeto, "Color":color_objeto, "Id":id_objeto}] #Datos a enviar al excel.
    nom_excel = "D:\Javier Valle\Documents\Documentos\Python\Pruebas con Tkinter\Prueba 2\datos.csv" #Directorio exacto del archivo.
    
    try: 
        #Abriendo el archivo.
        with open(nom_excel, 'w') as File:
            field = ["Tipo", "Talla", "Color", "Id"] #Encabezado del inventario.
            writer = csv.DictWriter(File, field)
            writer.writeheader() #Escribiendo el encabezado.

            #Imprimiendo los datos.
            for dato in datos:
                writer.writerows(datos) #Escribiendo los datos.
                print(dato) #Corroborando los datos.
    
    except  IOError:
        print("Error")
    #File.close() #Cerrando el archivo.

    #print("Hoja activa")
    #wb = openpyxl.Workbook(nom_excel)
    #hoja = wb.active #Activando el libro y la hoja en el índice 0.
    
   # df = pd.DataFrame(datos, columns = ["Tipo", "Talla", "Color", "Id"])
   # df.to_csv(nom_excel) #Enviando al Excel.
    

    #nombre_archivo.delete(0, END)

def ver_contenido():
    #Este método solo servirá para ver el contenido del csv.
    with open("D:\Javier Valle\Documents\Documentos\Python\Pruebas con Tkinter\Prueba 2\Pruebas\datos.csv", newline="") as File: 
        reader = csv.reader(File)
        for fila in reader: 
            print(fila)
    
    #Creando la ventana para ver las estadísticas en este método.
    ventana2=Toplevel()
    ventana2.geometry('380x300')
    #ventana2.configure(background='dark turquoise')
    ventana2.title("Inventario")
    #Nuevas cosas.
    frame = Frame(ventana2, bg='blue')
    frame.grid(column=0,row=0,sticky='nsew')
    
    #Pruebas de la gráfica
    nombres = ['Azul','Rojo','Verde','Magenta','Negro']
    colores = ['blue','red','green','magenta','black']
    tamano = [15,25,10,20,30]

    #Configurando gráfica
    fig, axs = plt.subplots(1,3, figsize=(13,4), sharey=True, facecolor="#00f9f844")

    #Título de la gráfica
    fig.suptitle("Gráficas con Mathplotlib")

    axs[0].bar(nombres, tamano, color = colores)
    axs[1].scatter(nombres, tamano, color = colores)
    axs[2].plot(nombres, tamano, color = "m")

    #Configurando el canvas.
    canvas = FigureCanvasTkAgg(fig, master = frame) #Crea el área de dibujo en Tkinter.
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=0, rowspan=3)
    
#Propiedades de la ventana que ingresa el formulario al csv.
frame1 = Frame(ventana, bg="gray15")
frame1.grid(column=0, row=0, sticky="nsew")
frame2 = Frame(ventana, bg="gray16")
frame2.grid(column=1, row=0, sticky="nsew")


"""
#Propiedades de la ventana que ve el contenido del csv.
frame3 = Frame(ventana2, bg="gray15")
frame3.grid(column=0, row=0, sticky="nsew")
frame4 = Frame(ventana2, bg="gray16")
frame4.grid(column=1, row=0, sticky="nsew")
"""

#Dando formato a los textboxes que se usarán para ingresar datos.

#Tipo
tipo = Label(frame1, text = "Tipo del objeto", width=10).grid(column=0, row=0, pady=20, padx= 10) #Formato para el tipo de objeto.
ingresa_tipo = Entry(frame1, width=20, font =("Arial", 12)) #Formato para el tipo de objeto.
ingresa_tipo.grid(column=1, row=0) #Columna y fila del tipo de objeto.

#Talla
talla = Label(frame1, text = "Talla del objeto", width=10).grid(column=0, row=1, pady=20, padx= 10) #Formato para la talla objeto.
ingresa_talla = Entry(frame1, width=20, font =("Arial", 12)) #Formato para la talla.
ingresa_talla.grid(column=1, row=1) #Columna y fila de la talla.

#Color
color = Label(frame1, text = "Color del objeto", width=10).grid(column=0, row=2, pady=20, padx= 10) #Formato para el color del objeto.
ingresa_color = Entry(frame1, width=20, font =("Arial", 12)) #Formato para el color del objeto.
ingresa_color.grid(column=1, row=2) #Columna y fila del color de objeto.

#Id
id = Label(frame1, text = "Id", width=10).grid(column=0, row=3, pady=20, padx= 10) #Formato para el id del objeto.
ingresa_ide = Entry(frame1, width=20, font =("Arial", 12)) #Formato para el id del objeto.
ingresa_ide.grid(column=1, row=3) #Columna y fila del id de objeto.

#Dando formato a los botones.

#Botón de agregar.
agregar = Button(frame1, width=20, font = ("Arial", 12, "bold"), text= "Agregar", bg="orange", bd=5, command =agregar_datos)
agregar.grid(columnspan=2, pady=20, padx= 10)

#Label.
archivo = Label(frame2, text = " Guardar en el archivo ", width=25, bg="gray16", font = ("Arial", 12, "bold"), fg="white")
archivo.grid(column=0, row=0, pady=1, padx=10)

#Nombre del archivo.
#nombre_archivo = Entry(frame2, width=23, font = ("Arial", 12),highlightbackground= "green", highlightthickness=4)
#nombre_archivo.grid(column=0, row=1, pady=1, padx=10)

#Botón para guardar el archivo.
guardar = Button(frame2, width=23, font = ("Arial",12, "bold"), text="Guardar", bg="green2",bd=5, command =guardar_datos)
guardar.grid(column=0, row=2, pady=20, padx= 10)

#Botón para enseñar el contenido del archivo.
ver = Button(frame2, width=23, font = ("Arial",12, "bold"), text="Ver contenido del archivo", bg="green2",bd=5, command =ver_contenido)
ver.grid(column=0, row=3, pady=20, padx= 10)

ventana.mainloop()