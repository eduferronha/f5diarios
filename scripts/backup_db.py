import os
import json
import zipfile
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("DB_NAME")

if not MONGODB_URL:
    raise ValueError("❌ MONGODB_URL não foi definida.")
if not DB_NAME:
    raise ValueError("❌ DB_NAME não foi definida.")

# Conecta ao Mongo
client = MongoClient(MONGODB_URL)
db = client[DB_NAME]

# Nome do ficheiro final
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
zip_filename = f"backup_{DB_NAME}_{timestamp}.zip"

# Cria o ZIP
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    collections = db.list_collection_names()

    for col_name in collections:
        col = db[col_name]

        # Obter todos os documentos
        data = list(col.find({}))

        # Serializar ObjectId para string
        for doc in data:
            doc["_id"] = str(doc["_id"])

        # Guardar como JSON temporário
        json_filename = f"{col_name}.json"
        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        # Adicionar ao ZIP
        zipf.write(json_filename)

        # Remover ficheiro temporário
        os.remove(json_filename)

print(f"✔ Backup completo criado: {zip_filename}")
