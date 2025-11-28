import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carla", "Diego", "Eva", "Felipe", "Gustavo"],
    "Idade": [25, 30, 22, 28, 35, 27, 31],
    "Cidade": ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus"]
}

df = pd.DataFrame(dados)

df_recife = df[df["Cidade"] == "Recife"]

print(df_recife)
