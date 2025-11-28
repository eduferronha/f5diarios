from pymongo import MongoClient
import pandas as pd

# 🔹 Configurações de conexão
MONGODB_URL = "mongodb+srv://admin1:auOf5q4TUtdKkJSx@myatlasclusteredu.bqfwm7l.mongodb.net/?appName=myAtlasClusterEDU"
DB_NAME = "F5tci"
COLLECTION_NAME = "tasks"

# 🔹 Conectar ao MongoDB
client = MongoClient(MONGODB_URL)
db = client[DB_NAME]
tasks_collection = db[COLLECTION_NAME]

# 🔹 Caminho do ficheiro Excel (ajusta o nome conforme necessário)
EXCEL_PATH = "F5TCI_out_set.xlsx"

# 🔹 Ler o Excel
df = pd.read_excel(EXCEL_PATH)

# 🔹 Remover linhas completamente vazias
df = df.dropna(how="all")

# 🔹 Filtrar apenas linhas com datas válidas na coluna "Data"
def is_valid_date(value):
    try:
        pd.to_datetime(value, dayfirst=True, errors="raise")
        return True
    except Exception:
        return False

df = df[df["Data"].apply(is_valid_date)]

print(f"📊 {len(df)} linhas válidas carregadas do Excel.")


# 🔹 Converter campos para o formato esperado
def safe_str(value):
    return "" if pd.isna(value) else str(value).strip()

def to_hhmm(value):
    """Converte horas em formato timedelta, número ou string para HH:MM"""
    if pd.isna(value):
        return "00:00"

    # Se for timedelta (ex: 0 days 06:00:00)
    if isinstance(value, pd.Timedelta):
        total_seconds = int(value.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        return f"{hours:02d}:{minutes:02d}"

    # Se for número (ex: 6, 8.5, etc.)
    if isinstance(value, (int, float)):
        hours = int(value)
        minutes = int((value - hours) * 60)
        return f"{hours:02d}:{minutes:02d}"

    # Se for string (ex: "06:00:00", "8", "8.5", etc.)
    s = str(value).strip()
    if "days" in s and ":" in s:
        s = s.split("days")[-1].strip()
    if ":" in s:
        parts = s.split(":")
        return f"{int(parts[0]):02d}:{int(parts[1]):02d}"
    try:
        h = int(float(s))
        return f"{h:02d}:00"
    except:
        return "00:00"


# 🔹 Criar lista de documentos a inserir
docs = []
for _, row in df.iterrows():
    doc = {
        "descricao": safe_str(row.get("Descritivo")),
        "cliente": safe_str(row.get("Descritivo_Cliente")),
        "parceiro": None,
        "produto": "",
        "contrato": "",
        "atividade": safe_str(row.get("Descritivo_TipoActividade")),
        "data": str(pd.to_datetime(row.get("Data")).date()) if not pd.isna(row.get("Data")) else "",
        "distancia_viagem": int(row.get("Distancia_Viagem")) if not pd.isna(row.get("Distancia_Viagem")) else 0,
        "tempo_viagem": to_hhmm(row.get("Horas_Viagem")),
        "tempo_atividade": to_hhmm(row.get("Horas_Durcacao")),
        "tempo_faturado": to_hhmm(row.get("Horas_Faturar")),
        "faturavel": "Yes" if str(row.get("Factura_Actividade")).strip().lower() in ["sim", "yes"] else "No",
        "viagem_faturavel": "Yes" if str(row.get("Factura_Viagem")).strip().lower() in ["sim", "yes"] else "No",
        "local": safe_str(row.get("Descritivo_Local")),
        "valor_euro": 0,
        "username": safe_str(row.get("Nome")),
    }
    docs.append(doc)

# 🔹 Limpar coleção antes de inserir (opcional)
tasks_collection.delete_many({})

# 🔹 Inserir na base de dados
if docs:
    tasks_collection.insert_many(docs)
    print(f"✅ {len(docs)} tarefas inseridas com sucesso na coleção '{COLLECTION_NAME}' 🚀")
else:
    print("⚠️ Nenhum registo encontrado no Excel.")
