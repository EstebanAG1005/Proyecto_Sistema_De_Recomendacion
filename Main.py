import Graph

run = True
op1 = 0
op2 = 0
op3 = 0

while run:

    print("\nSistema de Recomendacion de Restaurantes")
    print("1.Realizar una recomendacion\n2.Agregar Informacion a la Base de Datos\n3.Eliminar "
          "informacion de la base de datos\n4.Salir del Programa")
    op = int(input("Ingrese la opcion a realizar: "))

    # Empezar el con el sistema de recomendacion
    if op == 1:
        print(
            "Instrucciones: A continuacion se le presentara un listado de preguntas, las cuales esperamos que "
            "responda segun sus antojos\n")
        esp = input("¿Qué especialidad de comida quisiera comer hoy? (Opciones: Pizza-Pollo-Hamburguesa-Otros(Ingrese "
                    "Lo que usted busca): ")
        Especialidad = esp.title()
        pe = input("¿En que Rango de Precio le interesa que este su Restaurante? (Opciones: Bajo-Medio-Alto): ")
        Precio = pe.title()
        am = input("¿En que Ambiente le interesa que se encuentre su restaurante? (Opciones: Comida Rapida-Serio) ")
        Ambiente = am.title()

        Graph.Buscar(Especialidad, Precio, Ambiente)

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
        Graph.Add(Nombre, Especialidad, Precio, Ambiente)

    if op == 3:
        print("\n------Eliminar Informacion a la base de datos----------")
        Res = input('Ingrese el nombre del Restaurante que desea eliminar: ')
        Restaurante = Res.title()

        Graph.Borrar(Restaurante)
        Graph.delete(Restaurante)

    if op == 4:
        print("\nGracias por utlizar el programa :)\n ")
        run = False
