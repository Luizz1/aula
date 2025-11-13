email = input("Digite o email a ser checado: ").lower()
check = email.split("@")
if check[1] == "jogajuntoinstituto.org":
    print("Email verificado")
else: 
    print("O email precisa conter @jogajuntoinstituto.org")