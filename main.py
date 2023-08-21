#pip install beautifulsoup4
#pip install requests

import requests
from bs4 import BeautifulSoup

# URL de la página web
url = "https://www.losandes.com.pe/seccion/zona/puno/"

# Realizar una solicitud HTTP a la página web
response = requests.get(url)

# Comprobar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Crear un objeto BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Encontrar todos los elementos div con la clase "jeg_postblock_content"
    post_blocks = soup.find_all("div", class_="jeg_posts jeg_load_more_flag")
    
    # Iterar a través de los bloques de contenido
    for post_block in post_blocks:
        
        articles = post_block.find_all("article", class_="jeg_post jeg_pl_lg_2 format-standard")

        # Iterar a través de los elementos <article>
        for article in articles:
            # Extraer el contenido que deseas de cada artículo, por ejemplo:
            # URL
            article_url = article.find("a")["href"]

            # Título
            article_title = article.find("h3", class_="jeg_post_title").text.strip()

            # Fecha
            article_date = article.find("div", class_="jeg_meta_date").text.strip()

            # Número de Vistas
            article_views = article.find("div", class_="jeg_meta_views").text.strip()

            # Imprimir la información extraída
            print("URL:", article_url)
            print("Título:", article_title)
            print("Fecha:", article_date)
            print("Número de Vistas:", article_views)
            print("-" * 50)  # Separador entre artículos
else:
    print("Error al obtener la página:", response.status_code)