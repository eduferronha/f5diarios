from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://admin1:auOf5q4TUtdKkJSx@myatlasclusteredu.bqfwm7l.mongodb.net/?appName=myAtlasClusterEDU"
DB_NAME="F5tci"
client = MongoClient(MONGODB_URL)
db = client[DB_NAME]
clients_collection = db["clients"]

clientes = [
    ("ADIRA", "F5TCI", "Portugal", 0, "00:00", "", "", "Vila Nova de Gaia"),
    ("Arsopi", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("ATOBE", "F5TCI", "Portugal", 0, "00:00", "", "", "Lisboa"),
    ("Brisa - Auto-estradas de Portugal S. A.", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("Cinca - Companhia Industrial Cerâmica, S.A", "F5TCI", "Portugal", 32, "00:30", "", "", "Lourosa"),
    ("Cliente_Teste", "F5TCI", "Portugal", 12, "00:15", "", "", "Porto"),
    ("COFCO", "F5TCI", "Portugal", 10, "00:15", "", "", "Leça do Balio"),
    ("Coindu", "F5TCI", "Portugal", 45, "00:00", "", "", "Vila Nova de Famalicão"),
    ("Compta", "F5TCI", "Portugal", 15, "00:15", "", "", "Maia"),
    ("Desfruta, Comércio de Frutas, S.A.", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("Estado Líquido S.A.", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("F. Ramada Serviços de Gestão , Lda", "F5TCI", "Portugal", 60, "01:00", "", "", "Aveiro"),
    ("F5 Tecnologias de Comunicação Informação Lda", "F5TCI", "Portugal", 0, "00:00", "", "", "Matosinhos"),
    ("Facime II, SA", "F5TCI", "Portugal", 74, "00:00", "", "", "Viana do Castelo"),
    ("Franquiger SA", "F5TCI", "Portugal", 0, "00:00", "", "", "Sintra"),
    ("Frulact", "F5TCI", "Portugal", 15, "00:15", "", "", "Maia"),
    ("Fundo de Apoio Municipal", "F5TCI", "Portugal", 0, "00:00", "", "", "Lisboa"),
    ("Grupo Ferpinta", "F5TCI", "Portugal", 42, "00:45", "", "", "Ovar"),
    ("Grupo Martins", "F5TCI", "Portugal", 36, "00:30", "", "", "Meixomil"),
    ("GrupoatWork", "F5TCI", "Portugal", 2, "00:00", "", "", "Matosinhos"),
    ("Heliroma", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("Hotel Vouga", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("IKEA Industry", "F5TCI", "Portugal", 75, "00:30", "", "", "Paço de Ferreira"),
    ("IKEA Industry AB", "F5TCI", "Suécia", 0, "00:00", "", "", ""),
    ("INAPA", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("Inovapotek", "F5TCI", "Portugal", 10, "00:30", "", "", ""),
    ("Intraplás", "F5TCI", "Portugal", 40, "00:45", "", "", "Aves, Santo Tirso"),
    ("Kathrein Automotive Gmbh", "F5TCI", "Alemanha", 0, "00:00", "", "", ""),
    ("Marques Soares", "F5TCI", "Portugal", 0, "00:00", "", "", "Porto"),
    ("Mecwide", "F5TCI", "Portugal", 46, "00:00", "", "", "Barcelos"),
    ("Metro do Porto, S.A", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("Mitsubishi Fuso Truck Europe", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("Montepio Crédito - Instituição financeira de crédito , S.A", "F5TCI", "Portugal", 7, "00:00", "", "", "Porto"),
    ("N4IT", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("Orbitur", "F5TCI", "Portugal", 6, "00:00", "", "", "Porto"),
    ("PisanaAreia", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("Porini International, Lda", "F5TCI", "Portugal", 0, "00:00", "", "", "Matosinhos"),
    ("QlikTech Iberica, S.L", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("RCC", "F5TCI", "Portugal", 10, "00:00", "", "", "V N Gaia"),
    ("Recauchutagem Nortenha S.A.", "F5TCI", "Portugal", 90, "01:15", "", "", ""),
    ("Sakthi Portugal", "F5TCI", "Portugal", 0, "00:00", "", "", "Maia"),
    ("SAPWISE", "F5TCI", "Portugal", 9, "00:15", "", "", "Leça do Balio"),
    ("Serlima", "F5TCI", "Portugal", 20, "00:00", "", "", "Valongo"),
    ("Shamir", "F5TCI", "Portugal", 20, "00:30", "", "", "Vilar"),
    ("Sodril", "F5TCI", "Portugal", 0, "00:00", "", "", "Açores"),
    ("Solidal", "F5TCI", "Portugal", 48, "00:30", "", "", "Gandra"),
    ("Storax", "F5TCI", "Portugal", 47, "00:45", "", "", "Ovar"),
    ("STS Gestão", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("Teixeira Duarte", "F5TCI", "Portugal", 350, "03:30", "", "", "Oeiras"),
    ("Tensai Indústria", "F5TCI", "Alemanha", 0, "00:00", "", "", ""),
    ("Toyota Financial Services", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
    ("Universidade Católica Porto", "F5TCI", "Portugal", 5, "00:15", "", "", "Porto"),
    ("Universidade Portucalense", "F5TCI", "Portugal", 14, "00:30", "", "", "Porto"),
    ("WatchPlanet", "F5TCI", "Portugal", 0, "00:00", "", "", ""),
]

clients_collection.delete_many({})

docs = [
    {
        "nome": nome,
        "parceiro": parceiro,
        "pais": pais,
        "distancia_km": distancia,
        "tempo_viagem": tempo,
        "campo_extra1": extra1,
        "campo_extra2": extra2,
        "local": local,
    }
    for nome, parceiro, pais, distancia, tempo, extra1, extra2, local in clientes
]

clients_collection.insert_many(docs)

print(f"{len(docs)} clientes inseridos com sucesso na coleção 'clients' 🚀")
