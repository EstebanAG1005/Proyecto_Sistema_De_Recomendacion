from DataBase import *
import Usuarios as usuarios

run = True
usuarios.datos()
while run:
    
    print("---------- Bienvenid@ ----------")
    print("1. Realizar una recomendacion\n2.Salir del Programa")
    op = input("Ingrese la opcion a realizar: ")

    # Empezar el con el sistema de recomendacion
    if op == "1":
        print("")
        print("Procesando opciones\n")

    if op == "2":
        print("")
        print("Gracias por utlizar el programa :)\n ")
        run = False
