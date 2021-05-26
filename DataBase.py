# Generar los Restaurante
import numpy as np
import random
import pandas as pd
from neo4j import GraphDatabase

df = pd.read_csv("export.csv")

transaction_list = df.values.tolist()

transaction_execution_commands = []

for i in transaction_list:
    neo4j_create_statemenet = "create (n:Restaurante {Nombre: '" + str(i[0]) + "', Especialidad: '" + str(i[1]) + "'})"
    transaction_execution_commands.append(neo4j_create_statemenet)


def execute_transactions(transaction_execution_commands):
    data_base_connection = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "12345"))
    session = data_base_connection.session()
    for i in transaction_execution_commands:
        session.run(i)


execute_transactions(transaction_execution_commands)

execute_transactions(transaction_execution_commands)
