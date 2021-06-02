import csv

from neo4j import GraphDatabase
import re
import random
from csv import writer

db = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345"))

session = db.session()


def Agregar(Nombre, Especialidad, Precio, Ambiente):
    transaction_execution_commands = []
    # Se crean el nodo de Restaurante y se le agrean las propiedades
    neo4j_create_statemenet = "create (n:Restaurante {Nombre: '" + Nombre + "', Especialidad: '" + Especialidad + "', Precio: '" + Precio + "', Ambiente: '" + Ambiente + "'}) "
    transaction_execution_commands.append(neo4j_create_statemenet)

    session.run(neo4j_create_statemenet)


def Borrar(Nombre):
    q = """MATCH (n:Restaurante {Nombre:"%s"}) DELETE n
    
    """ % Nombre
    session.run(q)


def Buscar(Especialidad, Precio, Ambiente):
    transaction_execution_commands = []
    # Se crean el nodo de Restaurante y se le agrean las propiedades
    neo4j_create_statemenet = "MATCH (n:Restaurante {Especialidad: '" + Especialidad + "', Precio: '" + Precio + "', Ambiente: '" + Ambiente + "'}) RETURN n.Nombre "
    transaction_execution_commands.append(neo4j_create_statemenet)

    mas = session.run(neo4j_create_statemenet)

    Recomendacion = list(mas)
    print("\nPor tus respuestas dadas a nuestro sistema, te recomendamos consumir en")
    print(Recomendacion)

    result = re.split("[']", str(Recomendacion))  # Se separa por apostrofe
    print(result[1])


def Add(Nombre, Especialidad, Precio, Ambiente):
    List = [Nombre, Especialidad, Precio, Ambiente]

    with open('export.csv', 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)

        # Close the file object
        f_object.close()


def delete(Restaurante):
    with open("export.csv", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if Restaurante not in line:
                f.write(line)
        f.truncate()
