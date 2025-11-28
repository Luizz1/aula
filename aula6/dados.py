import pandas as pd

caminho_csv = r"C:\Users\Luiz\Downloads\dados_ficticios.csv"

df = pd.read_csv(caminho_csv)

idade_maior_40 = df[df["idade"] > 40]
renda_maior_5k = df[df["renda"] > 5000]
renda_maior_15k = df[df["renda"] > 15000]

print("Idade > 40:\n", idade_maior_40, "\n")
print("Renda > 5000:\n", renda_maior_5k, "\n")
print("Renda > 15000:\n", renda_maior_15k)
