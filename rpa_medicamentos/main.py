from scraping.buscar_precos import buscar_precos
from db.mongo_connect import salvar_medicamento

# Este script é responsável por buscar os preços de medicamentos e salvar as informações no banco de dados MongoDB.
# Ele utiliza a função buscar_precos do módulo scraping.buscar_precos para realizar a busca e a função salvar_medicamento do módulo db.mongo_connect para salvar os dados.
# O nome do medicamento a ser buscado é definido na variável 'nome'.
# Após a busca, os resultados são iterados e cada resultado é salvo no banco de dados com a função salvar_medicamento.
# O script imprime uma mensagem de sucesso após salvar todos os preços.

# Este é um exemplo de como você pode usar o módulo de scraping para buscar preços de medicamentos e salvá-los em um banco de dados MongoDB.

if __name__ == "__main__":
    nome = "dipirona 500mg"
    resultados = buscar_precos(nome)
    for r in resultados:
        salvar_medicamento({"medicamento": nome, **r})
    print("Preços salvos com sucesso!")
