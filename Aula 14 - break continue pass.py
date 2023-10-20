import random

def jogar_pedra_papel_tesoura():
    # Lista de opções para o jogo
    opcoes = ["Pedra", "Papel", "Tesoura"]

    while True:
        # O jogador faz sua escolha
        jogador_escolha = input("Escolha Pedra, Papel ou Tesoura (ou 'Sair' para encerrar): ").capitalize()

        if jogador_escolha == "Sair":
            print("Jogo encerrado.")
            break

        if jogador_escolha not in opcoes:
            print("Escolha inválida. Por favor, escolha entre Pedra, Papel ou Tesoura.")
            continue

        # O computador faz sua escolha aleatoriamente
        computador_escolha = random.choice(opcoes)
        print(f"O computador escolheu: {computador_escolha}")

        # Determinar o vencedor
        if jogador_escolha == computador_escolha:
            print("Empate!")
        elif (
            (jogador_escolha == "Pedra" and computador_escolha == "Tesoura") or
            (jogador_escolha == "Papel" and computador_escolha == "Pedra") or
            (jogador_escolha == "Tesoura" and computador_escolha == "Papel")
        ):
            print("Você venceu!")
        else:
            print("O computador venceu!")

# Chama a função para iniciar o jogo
jogar_pedra_papel_tesoura()