from neo4j import GraphDatabase

db = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "1234"))
session=db.session()

def get_person():
    query="MATCH (n:Person) RETURN n LIMIT 25"
    nodes = session.run(query)
    nodes = list(nodes)
    print(nodes)

get_person()