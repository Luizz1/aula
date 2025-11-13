import requests

integrantes = { 
    "Luiz": {"cep": 11634044},
    "Uarley": {"cep": 11630970},
    "Pacheco": {"cep": 11630971}
}   

for nome, dados in integrantes.items():
    cep = dados["cep"]
    request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    cidade = request.json()["localidade"]
    print(f"{nome} -> {cidade}")