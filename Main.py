from DataBase import *

run = True

while run:
    print("Sistema de Recomendacion de Restaurantes")
    print("1. Realizar una recomendacion\n2.Salir del Programa")
    op = input("Ingrese la opcion a realizar: ")

    # Empezar el con el sistema de recomendacion
    if op == "1":
        print("Procesando opciones\n")

    if op == "2":
        print("Gracias por utlizar el programa :)\n ")
        run = False
