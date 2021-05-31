import Graph

run = True
op1 = 0
op2 = 0
op3 = 0

while run:
    try:
        print("\nSistema de Recomendacion de Restaurantes")
        print("1.Realizar una recomendacion\n2.Agregar Informacion a la Base de Datos\n3.Eliminar "
              "informacion de la base de datos\n4.Salir del Programa")
        op = int(input("Ingrese la opcion a realizar: "))

        # Empezar el con el sistema de recomendacion
        if op == 1:
            print(
                "Instrucciones: A continuacion se le presentara un listado de preguntas, las cuales esperamos que "
                "responda segun sus antojos \n")
            print("")
            print("¿Qué especialidad de comida quisiera comer hoy?")
            print("1. Pizza \n2. Pollo \n3. Hamburguesa \n4. Otros ")
            op1 = int(input())
            run1 = False
            while not run1:
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

        if op == 2:
            print("\n------Agragar Informacion a la base de datos----------")
            nom = input("Ingrese el nombre del Restaurante que desea agregar: ")
            Nombre = nom.title()
            Espe = input("Ingrese la Especialidad de este restaurante: ")
            Especialidad = Espe.title()
            pe = input("Ingrese el Precio de promedio de este restaurante (Bajo)(Medio)(Alto): ")
            Precio = pe.title()
            am = input("Ingrese el Ambiente de este restaurante (Comida Rapida) (Serio) ")
            Ambiente = am.title()

            Graph.Agregar(Nombre, Especialidad, Precio, Ambiente)

        if op == 3:
            print("\n------Eliminar Informacion a la base de datos----------")
            Res = input('Ingrese el nombre del Restaurante que desea eliminar: ')
            Restaurante = Res.title()

            Graph.Borrar(Restaurante)

        if op == 4:
            print("\nGracias por utlizar el programa :)\n ")
            run = False
    except:
        print("Error se ha ingresado un valor no numerico")
    else:
        print("Ingrese un numero que este en el rango correspondiente ")
