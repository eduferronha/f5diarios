from pymongo import MongoClient

# --- Configuração da base de dados ---
MONGODB_URL = "mongodb+srv://admin1:auOf5q4TUtdKkJSx@myatlasclusteredu.bqfwm7l.mongodb.net/?appName=myAtlasClusterEDU"
DB_NAME = "F5tci"

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]
partners_collection = db["partners"]

# --- Dados dos parceiros (com base na imagem) ---
parceiros = [
    ("All@Work", "F5TCI", "Portugal", "Matosinhos", "", ""),
    ("PedroTenreiro", "F5TCI", "Portugal", "Matosinhos", "", ""),
    ("Sem Parceiro", "F5TCI", "Portugal", "", "", ""),
]

# --- Limpa e reinsere os dados ---
partners_collection.delete_many({})

docs = [
    {
        "parceiro": parceiro,
        "empresa": empresa,
        "pais": pais,
        "localidade": localidade,
        "latitude": latitude,
        "longitude": longitude,
    }
    for parceiro, empresa, pais, localidade, latitude, longitude in parceiros
]

partners_collection.insert_many(docs)

print(f"{len(docs)} parceiros inseridos com sucesso na coleção 'partners' 🚀")
