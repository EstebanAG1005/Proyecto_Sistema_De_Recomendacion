import Graph 
run = True
op1 = 0
op2 = 0
op3 = 0

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

    print("\nSistema de Recomendacion de Restaurantes")
    print("1.Realizar una recomendacion\n2.Agregar Informacion a la Base de Datos\n3.Eliminar "
          "informacion de la base de datos\n4.Salir del Programa")
    op = pedirNumeroEntero()

    # Empezar el con el sistema de recomendacion
    if op == 1:
        print(
            "\nInstrucciones: A continuacion se le presentara un listado de preguntas, las cuales esperamos que "
            "responda segun sus antojos\n")
        esp = input("¿Qué especialidad de comida quisiera comer hoy? (Opciones: Pizza-Pollo-Hamburguesa-Otros(Ingrese "
                    "Lo que usted busca): ")
        Especialidad = esp.title()
        pe = input("¿En que Rango de Precio le interesa que este su Restaurante? (Opciones: Bajo-Medio-Alto): ")
        Precio = pe.title()
        am = input("¿En que Ambiente le interesa que se encuentre su restaurante? (Opciones: Comida Rapida-Serio) ")
        Ambiente = am.title()

        Graph.Buscar(Especialidad, Precio, Ambiente)

    elif op == 2:
        print("\n------Agregar Informacion a la base de datos----------")
        nom = input("Ingrese el nombre del Restaurante que desea agregar: ")
        Nombre = nom.title()
        Espe = input("Ingrese la Especialidad de este restaurante: (Opciones: Pizza-Pollo-Hamburguesas-Otros)")
        Especialidad = Espe.title()
        pe = input("Ingrese el Precio de promedio de este restaurante (Bajo)(Medio)(Alto): ")
        Precio = pe.title()
        am = input("Ingrese el Ambiente de este restaurante (Comida Rapida) (Serio) ")
        Ambiente = am.title()

        Graph.Agregar(Nombre, Especialidad, Precio, Ambiente)
        print("")
        print("Informacion Agregada con Exito")
        print("")

    elif op == 3:
        print("\n------Eliminar Informacion a la base de datos----------")
        Res = input('Ingrese el nombre del Restaurante que desea eliminar: ')
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
