def verificar_grupo(numero):
    if numero % 2 == 0:
        print(f"{numero} → VOCÊ ESTÁ NO TIME AZUL")
    else:
        print(f"{numero} → VOCÊ ESTÁ NO TIME AMARELO")

matriculas = []

print("Digite até 5 números de matrícula:")

while len(matriculas) < 5:
    entrada = input("Número da matrícula: ")
    if entrada.isdigit():
        matriculas.append(int(entrada))
    else:
        print("Valor inválido! Digite apenas números.")

print("\nRESULTADOS:")
for numero in matriculas:
    verificar_grupo(numero)
