# Documentação SQ
Este repositório contém um conjunto de ferramentas que podem ser úteis para programadores que trabalham em projetos relacionados a webscraping.


## sq_extract_images.py
Este código em Python tem como objetivo extrair imagens de anúncios em um conjunto de URLs fornecidas em uma lista. As imagens são baixadas e salvas em pastas correspondentes ao ID de cada anúncio em um diretório base definido pelo usuário.

### Utilização
Antes de utilizar o código, é necessário definir a lista de URLs dos anúncios que se deseja extrair as imagens, bem como o diretório base onde as imagens serão salvas.

O código itera sobre as URLs de anúncios e para cada uma delas faz uma requisição HTTP para obter o conteúdo da página. Em seguida, o código utiliza a biblioteca BeautifulSoup para encontrar todas as tags de imagem na página e extrai as URLs das imagens que contém a ID do anúncio na URL.

Por fim, o código faz o download das imagens e salva em disco em pastas correspondentes ao ID de cada anúncio no diretório base definido pelo usuário.

#### Dependências
O código utiliza as seguintes bibliotecas do Python:
- os: biblioteca padrão do Python para manipulação de arquivos e diretórios.
- requests: biblioteca para fazer requisições HTTP em Python.
- beautifulsoup4: biblioteca para extrair dados HTML e XML em Python.
- urllib: biblioteca para fazer o download de arquivos em Python.

Certifique-se de ter todas essas bibliotecas instaladas antes de executar o código acima. Para instalar as bibliotecas selenium e webdriver, você pode utilizar o gerenciador de pacotes pip:
```py
pip install requests beautifulsoup4 os urllib
```

#### Limitações
É importante ressaltar que o código pode falhar em alguns casos, por exemplo, se as imagens não estiverem disponíveis na URL fornecida ou se a conexão com a internet estiver instável. Nesses casos, o código simplesmente ignora o erro e continua o processo de extração de imagens para as demais URLs fornecidas.
