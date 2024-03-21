import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse
import os

def get_html_and_domain(url):
    
    # Realiza una solicitud HTTP GET a la URL especificada y devuelve el contenido HTML y el dominio.
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return response.text, domain

def download_image(image_url, domain):
    
    # Descarga la imagen especificada por su URL.
    # Si la URL es relativa, la convierte en absoluta usando el dominio proporcionado.
    
    directory = "data"
    if image_url[:4] != 'http':
        image_url = f'https://{domain}{image_url}'
    filename = os.path.join(directory, image_url.split("/")[-1])
    urllib.request.urlretrieve(image_url, filename)
    return filename

def process_images_from_url(url):
    
    # Extrae todas las imágenes de la URL dada y las descarga.
    
    html_data, domain = get_html_and_domain(url)
    soup = BeautifulSoup(html_data, 'html.parser')
    images_downloaded = 0

    for item in soup.find_all('img'):
        if len(item['src']) > 4:
            print("maiu")
            download_image(item['src'], domain)
            images_downloaded += 1
        else:
            print('Imagen no válida o URL demasiado corta.')
    return images_downloaded
