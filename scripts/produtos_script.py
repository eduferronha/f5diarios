from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://admin1:auOf5q4TUtdKkJSx@myatlasclusteredu.bqfwm7l.mongodb.net/?appName=myAtlasClusterEDU"
DB_NAME="F5tci"

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]
products_collection = db["products"]

produtos = [
    "Consultoria",
    "Fabric",
    "NPrinting",
    "Power BI",
    "QlikSense",
    "Qlikview"
]

products_collection.delete_many({})

docs = [{"produto": nome, "empresa": "F5TCI"} for nome in produtos]
products_collection.insert_many(docs)

print(f"{len(docs)} produtos inseridos com sucesso na coleção 'products' 🚀")
