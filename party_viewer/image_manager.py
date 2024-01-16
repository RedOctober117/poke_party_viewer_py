import climage
import requests
from PIL import Image
from io import BytesIO
import numpy as np

def render_pokemon(mon_name):
    url = format(f'https://img.pokemondb.net/sprites/silver/normal/{mon_name.lower()}.png')
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert('RGB').resize((20, 20))
    arr = np.array(img)
    converted = climage.convert_array(arr, is_unicode=True)
    return converted
