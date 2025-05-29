
import json
from scraping.buscar_precos import buscar_precos
from db.mongo_connect import conectar_mongo
from db.s3_utils import upload_para_s3

def carregar_medicamentos():
    """
    Carrega os medicamentos do arquivo JSON.
    """
    with open("data/medicamentos.json", "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_mongo(dados, colecao):
    """
    Insere os dados na coleção MongoDB.
    """
    if dados:
        colecao.insert_many(dados)
        print("✅ Dados salvos no MongoDB")

def salvar_localmente(dados, caminho):
    """
    Salva os dados em um arquivo JSON local.
    """
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def executar():
    medicamentos = carregar_medicamentos()
    colecao = conectar_mongo()
    todos_precos = []

    for item in medicamentos:
        nome = item["nome"]
        print(f"🔍 Buscando: {nome}")
        precos = buscar_precos(nome)

        for preco in precos:
            preco["medicamento"] = nome
        
        todos_precos.extend(precos)

    salvar_mongo(todos_precos, colecao)
    salvar_localmente(todos_precos, "data/precos_medicamentos.json")
    upload_para_s3("data/precos_medicamentos.json", "seu-bucket", "precos_medicamentos.json")

if __name__ == "__main__":
    executar()
