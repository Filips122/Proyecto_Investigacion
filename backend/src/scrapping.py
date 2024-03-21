import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

def get_html_and_domain(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return response.text, domain

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_image(image_url, domain):
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    if image_url[:4] != 'http':
        # Asegúrate de que la URL se construye correctamente
        image_url = f'https://{domain}/{image_url.lstrip("/")}'
    filename = os.path.join(directory, image_url.split("/")[-1])
    
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
        else:
            print(f'Error al descargar {image_url}: Estado {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error al descargar {image_url}: {e}')
    
    return filename


def process_images_from_url(url):
    html_data, domain = get_html_and_domain(url)
    soup = BeautifulSoup(html_data, 'html.parser')
    images_downloaded = 0

    for item in soup.find_all('img'):
        if len(item['src']) > 4:
            print("Confirmed")
            download_image(item['src'], domain)
            images_downloaded += 1
        else:
            print('Imagen no válida o URL demasiado corta.')
    return images_downloaded
