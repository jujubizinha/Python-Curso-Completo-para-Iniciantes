
senha_certa = 2002
acertou = False

while not acertou:
    senha = int(input("Digite o número a senha: "))

    if senha == senha_certa:
        print("Acesso Permitido")
        acertou = True
    else:
        print("Senha Invalida")

