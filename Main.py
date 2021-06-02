# Guatemala, 4 de Junio del 2021
# Universidad del Valle de Guatemala
#-------------------------------------------------------------------------
# Ingeniería en Ciencias de la Computación y Tecnologías de la Información
# Algoritmos y Estructura de Datos
# Tercer Semestre
#-------------------------------------------------------------------------
# @Autores
# Esteban Aldana Guerra 20591
# Rolando Natanael Girón 20029
# Kenneth Eduardo Gálvez 20079
#-------------------------------------------------------------------------
# Clase Main.py
# Clase que será la encargada de la interacción con el Usuario
#-------------------------------------------------------------------------

import Graph
import Usuarios as Usuarios
run = True
op1 = 0
op2 = 0
op3 = 0

Usuarios.datos()
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

op = 0


while run:

    print("\n                     Sistema de Recomendacion de Restaurantes")
    print("\n1.Realizar una recomendacion\n2.Agregar Informacion a la Base de Datos\n3.Eliminar "
          "informacion de la base de datos\n4.Salir del Programa")
    op = pedirNumeroEntero()

    # Empezar el con el sistema de recomendacion
    if op == 1:
        print(
            "\nInstrucciones: A continuacion se le presentara un listado de preguntas, las cuales esperamos que "
            "responda segun sus antojos\n")
        esp = input("¿Qué especialidad de comida quisiera comer hoy? (Ejemplo: Pizza-Pollo-Hamburguesas...) ")
        Especialidad = esp.title()
        conf = True
        while conf:  
          pe = input("¿En que Rango de Precio le interesa que este su Restaurante? (Opciones: Bajo-Medio-Alto): ")
          if (pe != "Bajo") and (pe != "Medio") and (pe != "Alto"):
            print ("\n Unicamente se permite la opcion de Bajo, Medio y Alto \n")
          else: 
            Precio = pe.title()
            conf = False
        conf2 = True
        while conf2:
          am = input("¿En que Ambiente le interesa que se encuentre su restaurante? (Opciones: Comida Rapida-Serio): ")
          if (am != "Comida Rapida") and (am != "Serio"):
            print ("\n Unicamente se permite la opcion de Comida Rapida y Serio \n")
          else: 
            Ambiente = am.title()
            conf2 = False

        Graph.Buscar(Especialidad, Precio, Ambiente)

    elif op == 2:
        print("\n------Agregar Informacion a la base de datos----------")
        nom = input(" \n Ingrese el nombre del Restaurante que desea agregar: ")
        Nombre = nom.title()
        Espe = input(" \n Ingrese la Especialidad de este restaurante: (Opciones: Pizza-Pollo-Hamburguesas-...): ")
        Especialidad = Espe.title()
        conf = True
        while conf:  
          pe = input(" \nIngrese el Precio promedio de este restaurante (Bajo)(Medio)(Alto): ")
          if (pe != "Bajo") and (pe != "Medio") and (pe != "Alto"):
            print ("\n Unicamente se permite la opcion de Bajo, Medio y Alto \n")
          else: 
            Precio = pe.title()
            conf = False
        conf2 = True
        while conf2:
          am = input(" \nIngrese el Ambiente de este restaurante (Comida Rapida) (Serio): ")
          if (am != "Comida Rapida") and (am != "Serio"):
            print ("\n Unicamente se permite la opcion de Comida Rapida y Serio \n")
          else: 
            Ambiente = am.title()
            conf2 = False
            

        Graph.Agregar(Nombre, Especialidad, Precio, Ambiente)
        print("")
        print("Informacion Agregada con Exito")
        print("")

    elif op == 3:
        print("\n------Eliminar Informacion a la base de datos----------")
        Res = input('\nIngrese el nombre del Restaurante que desea eliminar: ')
        Restaurante = Res.title()

        Graph.Borrar(Restaurante)

        print("")
        print("Informacion Eliminada con Exito")
        print("")

    elif op == 4:
        print("\nGracias por utlizar el programa :)\n ")
        run = False
    else:
      print("\n Ingrese un numero entre 1 y 4 \n")
