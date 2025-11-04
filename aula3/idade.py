idade = int(input('Digite a idade?'))
if idade > 18:
    print('Usuário possui idade minima para dirigir')
elif idade >16 and idade <19:
    print("Indivíduo tem entre 17 e 18 anos e ainda NÃO está apto para dirigir")
else :
    print("Indivíduo NÃO está apto para dirigir")
