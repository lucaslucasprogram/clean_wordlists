import sys
import time
from os import name, system

for file in sys.argv[1:]:
    archivo = file

    def clear():
        # For windows
        if name == 'nt':
            _ = system('cls')
        # For linux or mac
        else:
            _ = system('clear')

    def min_char(archivo):
        start = time.time()
        print(archivo)
        cuantos_caracteres = input("De cuantos caracteres minimos tiene que ser la contraseña?: ")
        try:
            cuantos_caracteres = int(cuantos_caracteres)
        except:
            print("Ey! La cantidad de caracteres tiene que ser un número entero!")

        print("Input correcto, abriendo archivo")

        file = open(archivo, "r", encoding='utf-8')

        new_file_name = str(archivo) + "_min" + str(cuantos_caracteres) + "char"

        print(f"Archivo encontrado, creando nuevo archivo -> {new_file_name}...")

        lineas_totales = 0
        lines_finales = 0
        for password in file:
            lineas_totales += 1
            if len(password) >= cuantos_caracteres:
                lines_finales += 1
                # print(password)
                try:
                    new_file = open(new_file_name, "a")
                    new_file.write(password)
                except UnicodeEncodeError:
                    print("Encontre una contraseña que no está codeada en utf-8, no puedo leerla :(")
        file.close()
        end = time.time()
        tiempo_final = end-start

        print(f"\n\n"
              f"Listo :)"
              f"\n·Archivo creado '{new_file_name}'"
              f"\n·Contraseñas leidas: {lineas_totales}"
              f"\n·Contraseñas con minimo {cuantos_caracteres} caracteres: {lines_finales}"
              f"\n·Tiempo de lectura y reescritura: {tiempo_final:.2f} seg.")


    min_char(archivo)