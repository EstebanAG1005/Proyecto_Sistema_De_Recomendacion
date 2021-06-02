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
# Clase DataBase.py
# Clase encargada de realizar el primer commit de la Base de Datos en Neo4J
#-------------------------------------------------------------------------
# Referencia: https://www.youtube.com/watch?v=yluHRteVBNI&t=400s
#-------------------------------------------------------------------------

# Generar los Restaurante

import pandas as pd
from neo4j import GraphDatabase

df = pd.read_csv("export.csv")

transaction_list = df.values.tolist()

transaction_execution_commands = []

for i in transaction_list:
    neo4j_create_statemenet = "create (n:Restaurante {Nombre: '" + str(i[0]) + "', Especialidad: '" + str(i[1]) + "', Precio: '" + str(i[2]) + "', Ambiente: '" + str(i[3]) + "'}) "
    transaction_execution_commands.append(neo4j_create_statemenet)


def execute_transactions(transaction_execution_commands):
    data_base_connection = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "12345"))
    session = data_base_connection.session()
    for i in transaction_execution_commands:
        session.run(i)


execute_transactions(transaction_execution_commands)




