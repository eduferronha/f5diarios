from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://aabcde:abcde@myatlasclusteredu.bqfwm7l.mongodb.net/?retryWrites=true&w=majority"
DB_NAME = "F5tci"

try:
    client = MongoClient(MONGODB_URL, serverSelectionTimeoutMS=)
    client.server_info()  # força ligação imediata
    print("✅ Conexão ao MongoDB Atlas bem-sucedida!")
except Exception as e:
    print("❌ Erro ao conectar:", e)