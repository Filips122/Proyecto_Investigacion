+----------------------------+
|  Proyecto Lenguaje Signos  |
+----------------------------+

Basic:
 - README, secret, gitignore...

Carpeta code_for_img:
 - SegmentacionSigno.ipynb: dividimos la imagen con todas las letras en varias imagenes separadas.

Carpeta Backend:
 - Data: donde encontramos las imagenes que descargamos a partir del webscraping. En nuestro caso elegimos la img que tengan todas lasl etras y las dividimos con segmentación de img.
    - Roboflow: dataset exportado de roboflow
    - Modelos: segmentacion de imagenes para hugging face / cnn (no terminada).
 - Models: 
    - HuggingFace, a partir de modelos ya entrenados, vemos resultados.
    - RoboFlow, entrenar modelo con software.
    - CNN
 - Src: codigo webscraping.
 - main.py: iniciar el webscraping.

Carpeta Frontend:
 - Se encuentra vacia, pero para alguna interfaz bonita para el proyecto deberia ir en dicha carpeta.