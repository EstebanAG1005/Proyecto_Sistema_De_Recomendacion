#from DataBase import *
#import Usuarios as usuarios
#usuarios.datos()

print("---------- Bienvenid@ ----------")

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Ingrese la opción que desee: "))
            correcto=True
        except ValueError:
            print(' \n Error, introduce un numero entero \n')
     
    return num
 
run = False
op = 0

while not run:
    
    print("1. Realizar una recomendacion\n2.Salir del Programa")
    op = pedirNumeroEntero()

    # Empezar el con el sistema de recomendacion
    if op == 1:
        print("")
        print("Procesando opciones\n")

    elif op == 2:
        print("")
        print("Gracias por utlizar el programa :)\n ")
        run = True
    else:
        print("\n Ingrese un numero entre 1 y 2 \n")
