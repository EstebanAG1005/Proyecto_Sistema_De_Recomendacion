from neo4jrestclient.client import GraphDatabase

db = GraphDatabase("https://localhost:7687", username="neo4j", password="sistema")


# ---------------Categorias--------------------
Comida = db.labels.create("Comida")
Presupuesto = db.labels.create("Presupuesto")
Restaurantes = db.labels.create("Restaurantes")
TipoRestaurante = db.labels.create("TipoRestaurante")


# --------------------Comidas---------------------
Pizza=db.nodes.create(name="Pizza")
Pollo =db.nodes.create(name="Pollo")
Hamburguesas =db.nodes.create(name="Hamburguesas")
Tacos=db.nodes.create(name="Tacos")
Pasta=db.nodes.create(name="Pasta")
Carne_Asada=db.nodes.create(name="CarneAsada")
Suchi=db.nodes.create(name="Suchi")
Comida_China=db.nodes.create(name="ComidaChina")
Sandwich=db.nodes.create(name="Sandwich")
Crepes=db.nodes.create(name="Crepes")
Caldos=db.nodes.create(name="Caldos")
Mariscos=db.nodes.create(name="Mariscos")

Comida.add(Pizza,Pollo,Hamburguesas,Tacos,Pasta,Carne_Asada,Suchi,Comida_China,Sandwich,Crepes,Caldos,Mariscos)

# ----------------------Presupuestos----------------------
Alto=db.nodes.create(name="Alto")
Medio=db.nodes.create(name="Medio")
Bajo=db.nodes.create(name="Bajo")

Presupuesto.add(Alto,Medio,Bajo)

# -------------------Restaurantes-------------------------
BurgerKing=db.nodes.create(name="BurgerKing")
Trefratelli=db.nodes.create(name="Trefratelli")
El_Pinche=db.nodes.create(name="El Pinche")
Mcdonalds=db.nodes.create(name="Mcdonalds")
Subway=db.nodes.create(name="Subway")
Saul=db.nodes.create(name="Saul")
TacoBell=db.nodes.create(name="Taco Bell")
Panda_Expresss=db.nodes.create(name="Panda Express")
Dominos=db.nodes.create(name="Dominos")
KFC=db.nodes.create(name="KFC")
Wendys=db.nodes.create(name="Wendys")
Little_Ceasers=db.nodes.create(name="Little Ceasers")
Pollo_Campero=db.node.create(name="Pollo Campero")
Siete_Caldos=db.nodes.create(name="7 Caldos")
Frisco_Grill=db.nodes.create(nmae="Frisco Grill")
Puerto_Barrios=db.nodes.create(name="Puerto Barrios")
El_Puente=db.nodes.create(name="El Puente")

Restaurantes.add(BurgerKing,Trefratelli,El_Pinche,Mcdonalds,Subway,Saul,TacoBell,Panda_Expresss,Dominos,KFC,Wendys,Little_Ceasers,Pollo_Campero,Siete_Caldos,Frisco_Grill,Puerto_Barrios,El_Puente)

