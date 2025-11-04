valorCompra = float(input("Digite o valor da compra: "))

if valorCompra < 250:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")
elif valorCompra >= 250 and valorCompra < 500:
    print("PARABÉNS! VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00.")
else:
    print("PARABÉNS! VOCÊ GANHOU UM SUPER DESCONTO DE 30%.")
