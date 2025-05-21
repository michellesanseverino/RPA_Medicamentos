from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["controle_medicamentos"]
colecao = db["medicamentos"]

def salvar_medicamento(dados):
    colecao.insert_one(dados)