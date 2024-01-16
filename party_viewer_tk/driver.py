from tkinter import ttk

def main():
    image = ttk.PhotoImage(file=render_pokemon(mon))

if __name__ == '__main__':
    main()


import requests
from PIL import Image
from io import BytesIO

def render_pokemon(mon_name):
    url = format(f'https://img.pokemondb.net/sprites/silver/normal/{mon_name.lower()}.png')
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert('RGB')

    return img

