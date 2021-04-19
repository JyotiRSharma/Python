import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    final_name = str(name) + '.jpg'

    urllib.request.urlretrieve(url, final_name)

download_web_image("https://drive.google.com/file/d/0BwG-9IEc88tdVUt1X1NmaC13SVU/view?usp=sharing")

