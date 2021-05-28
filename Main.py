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

            print("")
            print("¿Qué nivel de precios relativos estaria dispuesto a pagar?")
            print("1. Alto (Q.71+) \n2. Medio (Q.51 - Q.70) \n3. Bajo(Q.1 - Q.50)")
            run2 = False
            while not run2:
              op2 = pedirNumeroEntero()

              if op2 == 1:
                print("--Especialidad Pizza, Precio Alto--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Pizza, Precio Alto, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Pizza, Precio Alto, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")
                    

              elif op2 == 2:
                print("--Especialidad Pizza, Precio Medio--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Pizza, Precio Medio, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Pizza, Precio Medio, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")

              elif op2 == 3:
                print("--Especialidad Pizza, Precio Bajo--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Pizza, Precio Bajo, Ambiente Serio--")
                    run3 = True
                    run = True
                  if op3 == 2:
                    print("--Especialidad Pizza, Precio Bajo, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")


              else:
                print("\n Ingrese un numero entre 1 - 3 \n")


          elif op1 == 2:
            print("--Especialidad Pollo--")
            run1 = True
            print("")
            print("¿Qué nivel de precios relativos estaria dispuesto a pagar?")
            print("1. Alto (Q.71+) \n2. Medio (Q.51 - Q.70) \n3. Bajo(Q.1 - Q.50)")

            run2 = False
            while not run2:
              op2 = pedirNumeroEntero()

              if op2 == 1:
                print("--Especialidad Pollo, Precio Alto--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Pollo, Precio Alto, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Pollo, Precio Alto, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")


              elif op2 == 2:
                print("--Especialidad Pollo, Precio Medio--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Pollo, Precio Medio, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Pollo, Precio Medio, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")


              elif op2 == 3:
                print("--Especialidad Pollo, Precio Bajo--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Pollo, Precio Bajo, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Pollo, Precio Bajo, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")
              else:
                print("\n Ingrese un numero entre 1 - 3 \n")


          elif op1 == 3:
            print("--Especialidad Hamburguesa--")
            run1 = True
            print("")
            print("¿Qué nivel de precios relativos estaria dispuesto a pagar?")
            print("1. Alto (Q.71+) \n2. Medio (Q.51 - Q.70) \n3. Bajo(Q.1 - Q.50)")

            run2 = False
            while not run2:
              op2 = pedirNumeroEntero()

              if op2 == 1:
                print("--Especialidad Hamburguesa, Precio Alto--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Hamburguesa, Precio Alto, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Hamburguesa, Precio Alto, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")


              elif op2 == 2:
                print("--Especialidad Hamburguesa, Precio Medio--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Hamburguesa, Precio Medio, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Hamburguesa, Precio Medio, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")


              elif op2 == 3:
                print("--Especialidad Hamburguesa, Precio Bajo--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Hamburguesa, Precio Bajo, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Hamburguesa, Precio Bajo, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")


              else:
                print("\n Ingrese un numero entre 1 - 3 \n")

          elif op1 == 4:
            print("--Especialidades Varias--")
            run1 = True
            print("")
            print("¿Qué nivel de precios relativos estaria dispuesto a pagar?")
            print("1. Alto (Q.71+) \n2. Medio (Q.51 - Q.70) \n3. Bajo(Q.1 - Q.50)")

            run2 = False
            while not run2:
              op2 = pedirNumeroEntero()

              if op2 == 1:
                print("--Especialidad Varias, Precio Alto--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Varias, Precio Alto, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Varias, Precio Alto, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")


              elif op2 == 2:
                print("--Especialidad Varias, Precio Medio--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Varias, Precio Medio, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Varias, Precio Medio, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")


              elif op2 == 3:
                print("--Especialidad Varias, Precio Bajo--")
                run2 = True
                print("")
                print("¿En que Ambiente se sentiría mejor degustar de su comida?")
                print("1. Ambiente Serio \n2. Ambiente Comida Rapida")
                run3 = False
                while not run3:
                  op3 = pedirNumeroEntero()

                  if op3 == 1:
                    print("--Especialidad Varias, Precio Bajo, Ambiente Serio--")
                    run3 = True
                    run = True
                  elif op3 == 2:
                    print("--Especialidad Varias, Precio Bajo, Ambiente Comida Rápida--")
                    run3 = True
                    run = True
                  else:
                    print("\n Ingrese un numero entre 1 - 2 \n")


              else:
                print("\n Ingrese un numero entre 1 - 3 \n")

          else:
             print("\n Ingrese un numero entre 1 - 4 \n")
          
          

    elif op == 2:
        print("")
        print("Gracias por utlizar el programa :)\n ")
        run = True
    else:
        print("\n Ingrese un numero entre 1 y 2 \n")
