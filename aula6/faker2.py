from faker import Faker
import random
import csv

fake = Faker("pt_BR")

def criar_persona():
    return {
        "nome": fake.name(),
        "cidade": fake.city(),
        "idade": random.randint(18, 80)
    }

personas = [criar_persona() for _ in range(5)]

with open("personas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=["nome", "cidade", "idade"])
    escritor.writeheader()
    escritor.writerows(personas)

print("CSV criado com sucesso.")
