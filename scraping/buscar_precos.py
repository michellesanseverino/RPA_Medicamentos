import requests
from bs4 import BeautifulSoup

def buscar_precos(nome_medicamento):
    """
    Faz scraping simples em uma farmácia fictícia.
    Retorna uma lista de dicionários com nome, preço e link.
    """

    # URL de busca (substitua com uma real)
    url = f"https://www.farmaciaexemplo.com/busca?q={nome_medicamento}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erro ao acessar {url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    resultados = []

    # Exemplo de extração de dados
    produtos = soup.select(".produto")

    for item in produtos:
        nome = item.select_one(".nome").text.strip()
        preco = item.select_one(".preco").text.strip()
        link = item.select_one("a")["href"]

        resultados.append({
            "nome": nome,
            "preco": preco,
            "link": f"https://www.farmaciaexemplo.com{link}"
        })

    return resultados
