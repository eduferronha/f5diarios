from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://admin1:auOf5q4TUtdKkJSx@myatlasclusteredu.bqfwm7l.mongodb.net/?appName=myAtlasClusterEDU"
DB_NAME="F5tci"

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]
activities_collection = db["activities"]

atividades = [
    ("Administrativa/Administrative", 100),
    ("Análise/Analysis", 100),
    ("Comercial/Commercial", 100),
    ("Consultoria/Consulting", 100),
    ("Doença/Disease", 100),
    ("Elaboração Documentação/Documentation", 100),
    ("Férias/Vacations", 100),
    ("Formação/Training", 100),
    ("Gestão de Parceiros/Partners management", 100),
    ("Gestão de projeto/Project manager", 100),
    ("Instalação-Configuração-Parametrização/Install-Config-Parametrizations", 100),
    ("Marketing", 100),
    ("Organização de eventos/Event organization", 100),
    ("Organização Interna/Internal Organization", 100),
    ("Outra/Other", 100),
    ("Preparação de demo/Demo preparation", 100),
    ("Preparação Projeto/Project planning", 100),
    ("Programação/Programming", 100),
    ("Reunião interna/Internal meeting", 100),
    ("Reunião/Meeting", 100),
    ("SEM ACTIVIDADE DEFINIDA/NO ACTIVITY DEFINNED", 100),
    ("Serviço StyleShoots/StyleShoots Services", 100),
    ("SIB", 0),
    ("Suporte a cliente/Client support", 100),
    ("Telefonemas/Phone calls", 100),
    ("Viagem/Travel", 100),
]

activities_collection.delete_many({})

docs = [{"atividade": nome, "custo_hora": custo} for nome, custo in atividades]
activities_collection.insert_many(docs)

print(f"{len(docs)} atividades inseridas com sucesso na coleção 'activities' 🚀")
