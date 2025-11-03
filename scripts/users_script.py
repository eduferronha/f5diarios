from pymongo import MongoClient

# --- Configuração DB ---
MONGODB_URL = "mongodb+srv://admin1:auOf5q4TUtdKkJSx@myatlasclusteredu.bqfwm7l.mongodb.net/?appName=myAtlasClusterEDU"
DB_NAME = "F5tci"

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]
users_collection = db["users"]

# --- Dados fornecidos (passwords substituídas por "test") ---
users = [
    {
        "nome": "Eduardo Ferronha",
        "username": "eferronha",
        "password": "test",
        "email": "eduardo.ferronha@f5tci.com",
        "empresa_base": "F5TCI",
        "chave": "fCZLekkSZfpVQC2FhrHZUw=="
    },
    {
        "nome": "Fernando Pereira",
        "username": "fpereira",
        "password": "test",
        "email": "fernando.pereira@f5tci.com",
        "empresa_base": "F5TCI",
        "chave": "ku0cT3dSOymUbPwmA9WL6w"
    },
    {
        "nome": "Hugo Correia",
        "username": "hcorreia",
        "password": "test",
        "email": "hugo.correia@f5tci.com",
        "empresa_base": "F5TCI",
        "chave": "fCZLekkSZfpVQC2FhrHZUw=="
    },
    {
        "nome": "Inês Pinho",
        "username": "ipinho",
        "password": "test",
        "email": "ines.pinho@f5tci.com",
        "empresa_base": "F5TCI",
        "chave": "fCZLekkSZfpVQC2FhrHZUw=="
    },
    {
        "nome": "João Vieira",
        "username": "jvieira",
        "password": "test",
        "email": "joao.vieira@f5tci.com",
        "empresa_base": "F5TCI",
        "chave": "GXZ7DU+fk1WqPO4coU4oSA=="
    },
    {
        "nome": "Jorge Costa",
        "username": "jcosta",
        "password": "test",
        "email": "jorge.costa@f5tci.com",
        "empresa_base": "F5TCI",
        "chave": "fCZLekkSZfpVQC2FhrHZUw=="
    },
    {
        "nome": "Rafael Simões",
        "username": "rsimoes",
        "password": "test",
        "email": "rafael.simoes@f5tci.com",
        "empresa_base": "F5TCI",
        "chave": "fCZLekkSZfpVQC2FhrHZUw=="
    },
    {
        "nome": "Ricardo Magalhães",
        "username": "rmagalhaes",
        "password": "test",
        "email": "ricardo.magalhaes@f5tci.com",
        "empresa_base": "F5TCI",
        "chave": "fCZLekkSZfpVQC2FhrHZUw=="
    },
    {
        "nome": "Tiago Brandão",
        "username": "tbrandao",
        "password": "test",
        "email": "tiago.brandao@f5tci.com",
        "empresa_base": "F5TCI",
        "chave": "fCZLekkSZfpVQC2FhrHZUw=="
    },
    {
        "nome": "Tomás Martins",
        "username": "tmartins",
        "password": "test",
        "email": "tomas.martins@f5tci.com",
        "empresa_base": "F5TCI",
        "chave": "fCZLekkSZfpVQC2FhrHZUw=="
    },
]

# --- Limpa coleção e insere ---
users_collection.delete_many({})
result = users_collection.insert_many(users)

print(f"{len(result.inserted_ids)} utilizadores inseridos com sucesso na coleção 'users' ✅")
