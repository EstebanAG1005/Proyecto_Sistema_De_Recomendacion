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
op1 = 0
op2 = 0
op3 = 0

while not run:
    
    print("1. Realizar una recomendacion\n2.Salir del Programa")
    op = pedirNumeroEntero()

    # Empezar el con el sistema de recomendacion
    if op == 1:
        print("")
        print("Instrucciones: A continuacion se le presentara un listado de preguntas, las cuales esperamos que responda segun sus antojos \n")
        print("")
        print("¿Qué especialidad de comida quisiera comer hoy?")
        print("1. Pizza \n2. Pollo \n3. Hamburguesa \n4. Otros ")
        run1 = False
        while not run1:
          op1 = pedirNumeroEntero()
          if op1 == 1:
            print("--Especialidad Pizza--")
            run1 = True
          elif op1 == 2:
            print("--Especialidad Pollo--")
            run1 = True
          elif op1 == 3:
            print("--Especialidad Hamburguesa--")
            run1 = True
          elif op1 == 4:
            print("--Especialidades Varias--")
            run1 = True
          else:
             print("\n Ingrese un numero entre 1 - 4 \n")
          
          

    elif op == 2:
        print("")
        print("Gracias por utlizar el programa :)\n ")
        run = True
    else:
        print("\n Ingrese un numero entre 1 y 2 \n")
