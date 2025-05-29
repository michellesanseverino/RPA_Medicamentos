import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

def conectar_mongo():
    """
    Conecta ao banco MongoDB Atlas usando URI armazenada no .env
    Retorna a coleção 'medicamentos' do banco 'controle_medicamentos'
    """
    mongo_uri = os.getenv("MONGO_URI")
    
    if not mongo_uri:
        raise ValueError("URI do MongoDB não encontrada no .env")

    # Criação do cliente e conexão com banco/coleção
    client = MongoClient(mongo_uri)
    db = client["controle_medicamentos"]
    colecao = db["medicamentos"]

    return colecao
