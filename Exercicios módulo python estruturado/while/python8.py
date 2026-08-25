passW = 40028922

while True:
    senha = int(input("Digite a senha: ")) 
    if senha == passW:
        print("Senha correta! Acesso permitido.")
        break
    else:
        print("Senha incorreta! Tente novamente.")