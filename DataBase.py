from neo4j import GraphDatabase

# Coneccion al servidor de Neo4j
db = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "1234"), encrypted=False)

session = db.session()
