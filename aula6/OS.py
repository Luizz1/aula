import os

dados = ["Ana", "Bruno", "Carla", "Diego"]

os.makedirs("minha_pasta", exist_ok=True)

with open("minha_pasta/dados.txt", "w") as arquivo:
    for item in dados:
        arquivo.write(item + "\n")
