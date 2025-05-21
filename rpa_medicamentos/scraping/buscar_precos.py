# Esse script faz scraping no site da Ultrafarma para buscar preços de medicamentos.
# Ele utiliza a biblioteca requests para fazer requisições HTTP e BeautifulSoup para fazer o parsing do HTML.
# O script busca os preços de medicamentos no site da Ultrafarma e salva as informações no banco de dados MongoDB.  

import requests
from bs4 import BeautifulSoup

def buscar_precos(nome_medicamento):
    url = f"https://www.ultrafarma.com.br/busca?termo={nome_medicamento.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resposta = requests.get(url, headers=headers)
    sopa = BeautifulSoup(resposta.text, 'html.parser')

    resultados = []
    produtos = sopa.find_all('div', class_='product-box')
    for p in produtos[:5]:
        nome = p.find('h3').get_text(strip=True)
        preco = p.find('span', class_='price-val').get_text(strip=True)
        resultados.append({"nome": nome, "preco": preco})
    return resultados 