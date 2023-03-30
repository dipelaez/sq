import os
import requests
from bs4 import BeautifulSoup
import urllib.request

# Define a lista de URLs de anúncios que queremos extrair as imagens
urls = lista

# Define o diretório base onde as imagens serão salvas
base_dir = 'imagens'

# Cria o diretório base se ele ainda não existir
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

# Itera sobre as URLs de anúncios
for url in urls:
    # Obtém o ID do anúncio a partir da URL
    id_anuncio = url.split('/')[-1]

    # Define o diretório para salvar as imagens do anúncio
    dir_anuncio = os.path.join(base_dir, id_anuncio)

    # Cria o diretório para salvar as imagens do anúncio, se ele ainda não existir
    if not os.path.exists(dir_anuncio):
        os.makedirs(dir_anuncio)

    # Faz a requisição HTTP para obter o conteúdo da página
    response = requests.get(url)

    # Cria o objeto BeautifulSoup para analisar o conteúdo da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontra todas as tags de imagem na página
    img_tags = soup.find_all('img')

    # Itera sobre as tags de imagem e extrai as URLs das imagens que contém a id_anuncio na URL
    urls = []
    for img in img_tags:
        if id_anuncio in str(img['src']):
            urls.append(img['src'])

    # Cria um loop para baixar as imagens e salvá-las na pasta do anúncio correspondente
    for url in urls:
        try:
            # Obtém o nome de arquivo da imagem a partir da URL
            filename = url.split("/")[-1]

            # Define o caminho completo para o arquivo de imagem
            filepath = os.path.join(dir_anuncio, filename)

            # Faz o download da imagem e salva em disco
            urllib.request.urlretrieve(url, filename=filepath)
        except:
            pass
        