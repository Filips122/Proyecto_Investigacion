from src.scrapping import *


url = 'https://fundacioncnse-dilse.org/?buscar='

images_downloaded = process_images_from_url(url)
print(f'Total de imágenes descargadas: {images_downloaded}')
