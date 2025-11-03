from pymongo import MongoClient

# === CONFIGURAÇÃO DA BASE DE DADOS ===
MONGODB_URL = "mongodb+srv://admin1:auOf5q4TUtdKkJSx@myatlasclusteredu.bqfwm7l.mongodb.net/?appName=myAtlasClusterEDU"
DB_NAME = "F5tci"

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]
contracts_collection = db["contracts"]

# === LISTA DE CONTRATOS ===
contratos = [
    ("A@W240101", "Ativo", "F5TCI", "GrupoatWork", "João Vieira", "Inês Pinho", "01/01/2024", "31/12/2024", 0, 340.00),
    ("ADI220629", "Ativo", "F5TCI", "ADIRA", "João Vieira", "Claúdia Santos", "01/08/2022", "01/08/2023", 15, 375.00),
    ("ARS220324", "Ativo", "F5TCI", "Arsopi", "João Vieira", "Inês Pinho", "24/03/2022", "31/12/2022", 10, 395.00),
    ("ATB231201", "Ativo", "F5TCI", "ATOBE", "João Vieira", "Inês Pinho", "19/12/2023", "31/05/2024", 0, 395.00),
    ("ATB240401_SKYWAY", "Ativo", "F5TCI", "ATOBE", "João Vieira", "Inês Pinho", "08/04/2024", "31/10/2024", 18, 395.00),
    ("ATB2410_RDW", "Ativo", "F5TCI", "ATOBE", "João Vieira", "Fernando Pereira", "01/10/2024", "30/09/2024", 30, 11250.00),
    ("ATB250101_SDG", "Ativo", "F5TCI", "ATOBE", "João Vieira", "Inês Pinho", "27/01/2025", "31/03/2025", 50, 395.00),
    ("CON230117", "Ativo", "F5TCI", "Kathrein Automotive Gmbh", "João Vieira", "Inês Pinho", "17/01/2023", "31/05/2023", 5, 500.00),
    ("Dev Int", "Ativo", "F5TCI", "F5 Tecnologias de Comunicação Informação Lda", "Inês Pinho", "Inês Pinho", "01/01/2022", "31/12/2022", 0, 0.00),
    ("ETL250717", "Ativo", "F5TCI", "Estado Líquido S.A.", "Tomás Martins", "Inês Pinho", "21/07/2025", "31/07/2025", 8, 445.00),
    ("F52025 S/ALOC", "Ativo", "F5TCI", "F5 Tecnologias de Comunicação Informação Lda", "Inês Pinho", "Inês Pinho", "01/01/2025", "31/12/2025", 0, 0.00),
    ("FER250903", "Ativo", "F5TCI", "Grupo Ferpinta", "João Vieira", "Inês Pinho", "11/09/2025", "10/10/2025", 11, 395.00),
    ("HEL211104", "Ativo", "F5TCI", "Heliroma", "Nuno Sousa", "Inês Pinho", "04/11/2021", "31/12/2021", 28, 356.00),
    ("IKE210101", "Ativo", "F5TCI", "IKEA Industry AB", "Rafael Simões", "Fernando Pereira", "06/10/2020", "31/12/2024", 0, 365.00),
    ("IKE220101", "Ativo", "F5TCI", "IKEA Industry AB", "Rafael Simões", "Inês Pinho", "01/07/2018", "31/12/2024", 0, 365.00),
    ("IKE250129", "Ativo", "F5TCI", "IKEA Industry AB", "Rafael Simões", "Inês Pinho", "05/02/2025", "29/01/2025", 240, 550.00),
    ("IKE250710", "Ativo", "F5TCI", "IKEA Industry", "Rafael Simões", "Inês Pinho", "17/07/2025", "31/08/2025", 200, 432.00),
    ("IKE250902", "Ativo", "F5TCI", "IKEA Industry AB", "Eduardo Ferronha", "Inês Pinho", "15/09/2025", "24/10/2025", 28, 55.00),
    ("LDC250115", "Ativo", "F5TCI", "Franquiger SA", "João Vieira", "Inês Pinho", "15/01/2025", "17/01/2025", 0, 415.00),
    ("Marketing", "Ativo", "F5TCI", "F5 Tecnologias de Comunicação Informação Lda", "Catarina Neves", "Inês Pinho", "01/01/2022", "31/12/2022", 0, 0.00),
    ("MEC150424", "Ativo", "F5TCI", "Mecwide", "Rafael Simões", "Inês Pinho", "15/04/2024", "30/04/2024", 0, 356.00),
    ("N4I210617", "Ativo", "F5TCI", "N4IT", "João Vieira", "Inês Pinho", "17/06/2021", "31/12/2022", 0, 328.00),
    ("POC230101", "Ativo", "F5TCI", "Cliente_Teste", "João Vieira", "Inês Pinho", "01/03/2023", "31/12/2023", 0, 0.00),
    ("POR240224", "Ativo", "F5TCI", "Porini International, Lda", "João Vieira", "Inês Pinho", "05/02/2024", "05/08/2024", 0, 0.00),
    ("SOL250508", "Ativo", "F5TCI", "Solidal", "Gonçalo Ruão", "Inês Pinho", "08/05/2025", "31/08/2025", 60, 455.00),
    ("STS21012025", "Ativo", "F5TCI", "STS Gestão", "João Vieira", "Inês Pinho", "10/02/2025", "30/06/2025", 10, 400.00),
    ("STS230327", "Ativo", "F5TCI", "STS Gestão", "João Vieira", "Inês Pinho", "29/03/2023", "31/12/2023", 50, 400.00),
    ("TESTE123", "Ativo", "F5TCI", "F5 Tecnologias de Comunicação Informação Lda", "Afonso Vieite", "Afonso Vieite", "30/09/2023", "01/10/2023", 100, 123.00),
    ("WTP2411320", "Ativo", "F5TCI", "WatchPlanet", "João Vieira", "Inês Pinho", "18/11/2024", "15/05/2025", 25, 370.00),
    ("WTP250120", "Ativo", "F5TCI", "WatchPlanet", "João Vieira", "Inês Pinho", "21/01/2025", "30/04/2025", 60, 395.00),
]

# === LIMPAR E INSERIR NOVOS CONTRATOS ===
contracts_collection.delete_many({})

docs = [
    {
        "contrato": contrato,
        "estado": estado,
        "empresa": empresa,
        "cliente": cliente,
        "p_manager": p_manager,
        "comercial": comercial,
        "data_inicio": data_ini,
        "data_fim": data_fim,
        "valor_dias": valor_d,
        "valor_euro": valor_euro,
    }
    for contrato, estado, empresa, cliente, p_manager, comercial, data_ini, data_fim, valor_d, valor_euro in contratos
]

contracts_collection.insert_many(docs)

print(f"{len(docs)} contratos inseridos com sucesso na coleção 'contracts' 🚀")
