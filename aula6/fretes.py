import requests

cep = input("Digite o CEP (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url).json()

estado = resposta["uf"]

regioes_frete_gratis = [
    "AM","RR","AP","PA","TO","RO","AC",  
    "MA","PI","CE","RN","PB","PE","AL","SE","BA" 
]

if estado in regioes_frete_gratis:
    print("Frete GRÁTIS disponível!")
else:
    print("Frete grátis NÃO disponível.")
