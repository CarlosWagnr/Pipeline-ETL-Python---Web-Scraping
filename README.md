# Pipeline ETL Python - Web Scraping
Solução Pipeline ETL (Extract Transform Load) para monitorar preço de notebooks no Mercado Livre

* Usar Python
* Scrapy para extrair os dados
* Pandas para transformar e fazer o load
* Streamlit para o frontend(dashboards)
* SQL para armazenar os dados

## Objetivo do projeto
- Análise de concorrência de notebooks no mercado livre.
- Coleta de dados estruturados (nome, marca, preço, avaliações, vendedor, etc)
- Necessário desenvolver o Web Scraping
- Necessário salvar os dados em um banco de dados
- Necessário desenvolver um dashboard interativo

Link: HTTPS://LISTA.MERCADOLIVRE.COM.BR/NOTEBOOK#D[A:NOTEBOOK]

## Etapadas do Projeto - Passo a Passo
- Criar o ambiente virtual do projeto no VSCode - ```python -m venv .venv```
- Ativar o ambiente virtual - ```.venv\Scripts\activate```
- Montar a estrutura de pastas do projeto
    * data/
    * source/extraction
    * source/transform_load
    * source/dashboard

- Instalar a biblioteca Scrapy - ```pip install scrapy```
- Na pasta extraction inicializar o projeto de extração com o Scrapy  - ```scrapy startproject coleta```

    * Ao executar o comando acima o scrapy irá criar a estrutura do projeto para ser utilizado, não utilizaremos os arquivos pipeline e middware.

        * settings.py - onde faremos as configurações para acessar o site.

    * Na pasta extraction/coleta criamos um notebook que será utilizado para fazermos a extração dos dados utilizando o seguinte comando - ```scrapy genspider notebook HTTPS://LISTA.MERCADOLIVRE.COM.BR/NOTEBOOK#D[A:NOTEBOOK]```, ao executar este comando ele irá criar o notebook fazendo a importação da biblioteca Scrapy e uma classe que será utilizada para fazer a extração dos dados.

    * Antes de fazer a conexão com o site devemos usar o User Agente pesquisando no google por *my user agent*, copie o resultado e no componente de configuração para não ser bloqueado ao fazer a requisição no site.

    * Após configurado o *User Agente* na pasta coleta, digitamos no terminal o comando ```scrapy shell``` para interagir com o scrpay via terminal, logo após digite ```fetch('https://lista.mercadolivre.com.br/notebook?sb-rb#D[:nontebook]')``` para testar a conexão com o site e verificar o código de retorno da requisição.

    * Retornando o código da requisição 200, podemos seguir com a etapa de seleção dos dados para extração. Dentro do site podemos inspencioná-lo e verificar em qual estrutura está os dados que desejamos e fazemos o teste no scrpay shell. Exemplo: ```response.css('span.poly-component__brand::text').get()```. Agora podemos fazer o mesmo para todos os dados relevante para o nosso projeto.

    * Terminando de estruturar o arquivo notebook com os dados que queremos extrair, estando na pasta 'source\extraction\coleta' podemos executar o notebook para salvarmos os dados: ```scrapy crawl notebook -o C:\Python\Pipeline-ETL-Python---Web-Scraping\data\data.json```. Neste caso estamos salvando os dados no formato json, mas podemos salvar em outros formatos.


response.css('span.poly-component__brand::text').get()


scrapy crawl notebook -o C:\Python\Pipeline-ETL-Python---Web-Scraping\data\data.json


C:\Python\Pipeline-ETL-Python---Web-Scraping\data


#root-app > div > div.ui-search-main.ui-search-main--only-products.ui-search-main--with-topkeywords > section > div:nth-child(6) > nav > ul > li.andes-pagination__button.andes-pagination__button--next