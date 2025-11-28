def verificar_grupo():
    numero = int(input("Digite o número da matrícula: "))

    if numero % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")

verificar_grupo()
