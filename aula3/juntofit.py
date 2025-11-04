dias = 0

while dias < 21:
    catraca = input("Passar a catraca? [S/N]: ").lower()
    if catraca == "s":
        dias += 1
        print(f"Dia {dias}/21 - Continue firme na PROMO TREINA JUNTO!")
    elif catraca == "n":
        print("Ok! Voltaremos a contar quando você passar a catraca novamente.")
    else:
        print("Opção inválida. Digite apenas S ou N.")

if dias == 21:
    print("UHUU! AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ!")
