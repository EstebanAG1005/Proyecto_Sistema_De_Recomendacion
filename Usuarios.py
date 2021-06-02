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
# Clase Usuarios.py
# Clase que será la encargada de registrar e iniciar sesion a los Usuarios
#-------------------------------------------------------------------------

import csv

def datos ():
    print("--------------- Sistema de Recomendacion de Restaurantes ---------------")
    print("\n¿Ya tienes una cuenta?")
    print("1. Iniciar Sesión")
    print("\n¿Eres nuevo aquí?")
    print("2. Registrarse")
    print("\n¿Deseas ingresar en otro momento?")
    print("3. Salir")
    print("")

    global opcion_datos
    a= False
    c = False
    while not a:
       try:
         opcion_datos = input("Ingrese una de las opciones anteriormente mencionadas: ")
         opcion_datos = int(opcion_datos)
         a = True
       except Exception:
         print("\nEl valor ingresado no es un número, por favor, ingrese un número")
     
     #Si el número es menor que 1 o mayor que 3
    while opcion_datos < 1 or opcion_datos > 3:
        #Se imprime un mensaje de error
        print("\nNúmero fuera de rango, por favor ingresar otra vez:")
     #Se crea Defensa del rango
        try:
            #Se pide al usuario que ingrese un número
            opcion_datos = int(input(":"))
            #Si el número es válido, la variable "c", se convierte en TRUE
            c = True
        #Se crea la excepción
        except Exception:
            print()
            
   
            
            
    #Se crea "Loop" de las opciones, mientras lo ingresado no sea 3
    while opcion_datos !=4:   
        if opcion_datos == 1:
            userlista = []

            input_file = csv.DictReader(open("usuarios.csv"))

            for row in input_file:
                userlista.append(row)
                
                    
                
            user1 = {}

            users = user1["usuarios"] = input("Introduzca un nombre de usuario o (M) si desea regresar al menú principal: ")
                        
            if users == "M":
                    print("")
                    datos()
                    
            if users != "M":
                user1["contra"] = input("Introduzca una contraseña: ")
                        
                comprobar = False    
                for userexist in userlista:
                    if userexist ["usuarios"] == user1 ["usuarios"] and userexist ["contra"] == user1 ["contra"]:
                        comprobar = True
                                
                    elif userexist ["usuarios"] != user1 ["usuarios"] and userexist ["contra"] != user1 ["contra"]:
                        comprobar = False
                                
                                
                    
                if comprobar == True:
                    print("")
                    break
                    
                elif comprobar == False:
                    print ("Usuario no  existente, favor ingrese nuevamente")
                    print("")
                    
                            
                
                         
                           



                
        if opcion_datos == 2:
                
            guardado = []

            input_file = csv.DictReader(open("usuarios.csv"))

            for row in input_file:
                guardado.append(row)
                    
                
            
            print("Registros previos: " + str(len(guardado)))

            def crear ():
                a = False
                while not a:
                    user = {}

                    users = user["usuarios"] = input("Introduzca un nombre de usuario o (M) si desea regresar al menú principal: ")
                    
                    if users == "M":
                        print("")
                        datos()
                        
                    if users != "M":
                        user["contra"] = input("Introduzca una contraseña: ")
            
                        comprobar = False    
                        for userOld in guardado:
                            if userOld ["usuarios"] == user ["usuarios"] and userOld ["contra"] == user ["contra"]:
                                comprobar = True
                                print ("Usuario ya existente")
                                print("")
                        
                        
                        
                        
                            elif userOld ["usuarios"] != user ["usuarios"] and userOld ["contra"] != user ["contra"]:
                                comprobar = False
                        
                        
                        
                        if comprobar == False:
                            print ("Usuario agregado correctamente")
                            print("")
                            guardado.append(user)
                            a = True
            crear()
            
            with open ("usuarios.csv" , "w") as f:
                w = csv.DictWriter(f, guardado[0].keys())
                w.writeheader()
                for user in guardado:
                    w.writerow(user)
                    
        if opcion_datos == 3:
            print("\nMuchas Gracias por usar nuestro programa ")
            quit()
            
            
               
              
        datos()








