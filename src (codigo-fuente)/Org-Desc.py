# automatización
import os
import time
import shutil
import pathlib
from tkinter import*
from threading import *
from tkinter import messagebox, filedialog


# Función para abrir carpeta a organizar
def abrir_archivo(): 
    global ruta_descargas2
    global ruta_descargas
    global b
    ruta_descargas= filedialog.askdirectory(initialdir="/",title="Seleccionar carpeta")# Abre ventana para seleccionar carrpeta a organizar
    ruta_descargas2= ruta_descargas + "/" 
    print("\nRuta seleccionada: ",ruta_descargas2) #Imprime carpeta seleccionada
    print("\n")

    b=os.listdir(ruta_descargas) #listar todos los archivos que hay en la ubicación

    if ruta_descargas == "": #Marcar error si no se selecciona ninguna
        messagebox.showinfo("Organizador de Descargas","No se a seleccionado una ruta_descargas valida") 
        time.sleep(5)
        ven.destroy() #Cerrar ventana
    else:
        messagebox.showinfo("Organizador de Descargas", "Ubicación seleccionada: " + ruta_descargas) #Mostrar carpeta seleccionada

def creardir(): #Crear Carpetas
    carpeta= "Fotos","Texto","PDFS","Programa","Video","Zip","Música","Python","Otros" #Nombres
    existen= False 
    for dir in carpeta:    
        ruta_descargas2 =ruta_descargas + "/" + dir 
        print(ruta_descargas2) 
        if os.path.exists(ruta_descargas2): #Verificar si existen o no 
            print("Ya existe")
            existen = True #Marcar que si existen 
        else: #Si no existen se crean
            try:
                os.mkdir(ruta_descargas2) #Crear carpetas con la dirección antes seleccionada
            except OSError: #Marcar si hubo algún fallo 
                print("La creación del directorio %s falló" % ruta_descargas2)
                messagebox.showinfo("Organizador de Descargas","La creación del directorio %s falló" % ruta_descargas2) #Mostrar que hubo un fallo en la creación
            else: #Si nada a fallado llega aquí
                print("Se ha creado el directorio: %s " % ruta_descargas2) 
                messagebox.showinfo("Organizador de Descargas","Se ha creado el directorio: %s " % ruta_descargas2) #Mostrar que se han creado las carpetas
    if existen == True: #Si ya existen, mostrar que ya existen
        messagebox.showinfo("Organizador de Descargas","Ya existen las carpetas")
    else: #Si no, mostar que se estan creando las carpetas
        messagebox.showinfo("Organizador de Descargas","Creando carpetas")

#Crear ventana grafica 
ven= Tk()
ven.geometry("800x500")
ven.resizable(False,False)
ven.configure(bg = "#0c3f36")
ven.title("Organizador de las descargas") 


texto0= Label(ven,text="ORG - DESC By Martin Perez",bg="#cad5d5",font=("tahoma",25)).place(x=208,y=50)
texto4= Label(ven,text="Seleccionar ubicación de la carpeta descarga",bg="#cad5d5",font=15).place(x=210,y=120)
texto5= Label(ven,text="Crear categorías de carpetas",bg="#cad5d5",font=15).place(x=280,y=230)

# tipos de archivos de categoría
ext_texto = ['.docx', '.txt', '.doc','.xlsx', '.pptx']
ext_pdf= [".pdf"]
ext_fotos = ['.jpg', '.jpeg', '.png', '.gif']
ext_software = ['.exe', '.pkg', '.lnk']
ext_zip= [".zip", ".rar",".7z",".gz"]
ext_video= [".mov", ".mp4"]
ext_música= [".mp3",".ogg"]
ext_sfk= [".sfk"]
ext_py= [".whl", ".json", ".py", ".xml"]

# Función de hilos(evitar problemas al ejecutarse el programa al ejecutarse)
def hilos():
    global t1
    t1= Thread(target=ordenar2)
    t1.start()

# Inicie proceso de clasificar archivos
def ordenar(archivo, ext):
    for i in ext_texto:
        if ext == i :
            shutil.move(ruta_descargas2 + archivo, ruta_descargas2 + "Texto")
    for i in ext_música:
        if ext == i :
            shutil.move(ruta_descargas2 + archivo, ruta_descargas2 + "Música")
    for i in ext_pdf:
        if ext == i :
            shutil.move(ruta_descargas2 + archivo, ruta_descargas2 + "PDFS")
    for i in ext_fotos:
        if ext == i :
            shutil.move(ruta_descargas2 + archivo, ruta_descargas2 + "Fotos")
    for i in ext_software:
        if ext == i :
            shutil.move(ruta_descargas2 + archivo, ruta_descargas2 + "Programa")
    for i in ext_video:
        if ext == i :
            shutil.move(ruta_descargas2 + archivo, ruta_descargas2 + "Video")
    for i in ext_zip:
        if ext == i :
            shutil.move(ruta_descargas2 + archivo, ruta_descargas2 + "Zip")
    for i in ext_py:
        if ext == i :
            shutil.move(ruta_descargas2 + archivo, ruta_descargas2 + "Python")

    if ext != "":
        for i in b:
            print("\n")
            print("b:",i)

            unir= ruta_descargas +"/"+ i 
            print("Unir:",unir)

            path1= pathlib.Path(unir)
            print("Path1:",ruta_descargas)

            xD= path1.suffix
            print("Extensión archivo:",xD)

            if xD != "":
                print("No Carpeta")
                print("\n")
                try:
                    shutil.move(ruta_descargas2 + archivo, ruta_descargas2 + "Otros")
                    print("Movido")
                except Exception as e:
                    error1= ("Error mover otros:", e)
                    print("Error 1:",error1)
                    print("Archivo no tiene categoria")
            else:
                print("Carpeta")

def ordenar2():
    if ruta_descargas == "":
        messagebox.showinfo("Organizador de Descargas","No se a seleccionado una ubicación valida")
        time.sleep(5)
        ven.destroy()
    else:
        for archivo in os.listdir(ruta_descargas2):
            nombre_archivo, ext= os.path.splitext(archivo)
            ordenar(archivo, ext)
        time.sleep(3)
        messagebox.showinfo("Organizador de Descargas","LISTO, Carpetas Organizadas")
        time.sleep(2)
        os.startfile(ruta_descargas2)
        time.sleep(2)
        ven.destroy()

bton1= Button(ven, text="Ubicación",command= abrir_archivo).place(x=340,y=160,width=135,height=25)
bton2= Button(ven,text="Crear Carpeta",command=creardir).place(x=340,y=270,width=135,height=25)
bton= Button(ven, text="Organizar",bg="#3CEB7D",command= hilos).place(x=340,y=350,width=135,height=25)

ven.mainloop()
