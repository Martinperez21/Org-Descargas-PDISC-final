import os
import time
import shutil
import pathlib
''' Obtener y mostrar las extensiones unicas de archivos existentes 
en una carpeta.
'''
def main():
    ruta = pathlib.Path('.')

    for archivo in ruta.iterdir():
        print(archivo.suffix)

if __name__ == '__main__':
    main()
