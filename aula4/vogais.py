vogais = ("aeiou")
palavra = input("Digite a palavra: ")
letras = list(palavra)
contador = 0

for i in letras:
    if i in vogais:
        contador += 1

print(f"A frase contém {contador} vogais")
