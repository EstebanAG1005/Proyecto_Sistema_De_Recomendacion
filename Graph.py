from neo4j import GraphDatabase
import re
import random

db = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "12345"))

session = db.session()


def Agregar(Nombre, Especialidad, Precio, Ambiente):
    transaction_execution_commands = []
    # Se crean el nodo de Restaurante y se le agrean las propiedades
    neo4j_create_statemenet = "create (n:Restaurante {Nombre: '" + Nombre + "', Especialidad: '" + Especialidad + "', Precio: '" + Precio + "', Ambiente: '" + Ambiente + "'}) "
    transaction_execution_commands.append(neo4j_create_statemenet)

    session.run(neo4j_create_statemenet)


def Borrar(Nombre):
    q = """MATCH (n {nombre:'%s'}) DETACH DELETE n
    
    
    """ % (Nombre)
    session.run(q)
