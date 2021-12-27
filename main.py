import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk 
import urllib3
from io import BytesIO

## ======== Fuunction ========##

def loadPokemon():
    pokemon = pypokedex.get(name=inputNameId.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    resp = http.request("GET", pokemon.sprites.front.get("default"))
    image = PIL.Image.open(BytesIO(resp.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemonImage.config(image=img)
    pokemonImage.image = img

    pokemonInfo.config(text=f"{pokemon.dex} - {pokemon.name}".title())
    pokemonTypes.config(text=" - ".join([t for t in pokemon.types]).title())

## ======== Screen Definitions ========##

screen = tk.Tk()
screen.geometry("600x500")
screen.title("Pokedex")
screen.config(padx=10,pady=10)

titleLabel = tk.Label(screen, text="Pokedex")
titleLabel.config(font=("Arial", 40))
titleLabel.pack(padx=10, pady=10)

pokemonImage= tk.Label(screen)
pokemonImage.pack(padx=10, pady=10)

pokemonInfo = tk.Label(screen)
pokemonInfo.config(font=("Arial", 30))
pokemonInfo.pack(padx=10, pady=10)

pokemonTypes = tk.Label(screen)
pokemonTypes.config(font=("Arial", 30))
pokemonTypes.pack(padx=10, pady=10)

labelNameId = tk.Label(screen, text="Nome ou Id:")
labelNameId.config(font=("Arial", 20))
labelNameId.pack(padx=10, pady=10)

inputNameId = tk.Text(screen, height=1)
inputNameId.config(font=("Arial", 20))
inputNameId.pack(padx=10, pady=10)

btnLoad = tk.Button(screen, text="Buscar Pokemon", command=loadPokemon)
btnLoad.config(font=("Arial", 20))
btnLoad.pack(padx=10, pady=10)

## ======== Init ========##

screen.mainloop()