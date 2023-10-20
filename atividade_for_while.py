# Claro, aqui estão 20 exercícios, divididos em 10 de nível fácil,
# 5 de nível médio e 5 de nível difícil, relacionados aos tópicos mencionados:

# Nível Fácil:

# Escreva um programa que use um loop "for" para imprimir os números pares de 1 a 10.
 for numero in range(1, 11):
    print(numero)

# Escreva um programa que use um loop "while" para contar de 1 até 5 e, em seguida, imprimir
 #"Contagem concluída!".
    contador = 1
 while contador <= 5:
     print(contador)
     if contador >= 5:
         print("Contagem concluída!")
     contador += 1

# Crie um programa que use loops aninhados para imprimir uma matriz 2D simples,
# como uma matriz de identidade (uma matriz quadrada com 1s na diagonal principal e 0s em outros lugares).
def criar_matriz_identidade(n):
    matriz = []

    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=" ")
        print("\n")


tamanho_matriz = 8
matriz_identidade = criar_matriz_identidade(tamanho_matriz)

print("Matriz de Identidade {}x{}:".format(tamanho_matriz, tamanho_matriz))
imprimir_matriz(matriz_identidade)


# Escreva um programa que use um loop "for" para imprimir os números ímpares de 1 a 10.
 for numero in range(1,11):
     if numero % 2 == 0:
         pass
     else:
         print(numero)


# Escreva um programa que use um loop "while" para contar de 10 até 1 e, em seguida,
# imprimir "Contagem regressiva concluída!".
 contador2 = 10
 while contador2 >= 1:
 print(contador2)
    contador2 -= 1

# Crie um programa que use um loop "for" para imprimir os primeiros 5
# números da série de Fibonacci.
numero_1 = 0
numero_2 = 1

for numero in range(5):
    if numero <= 1:
        proximo = numero
        print(numero)
    else:
        proximo = numero_1 + numero_2
        numero_1 = numero_2
        numero_2 = proximo
        print(proximo)



# Escreva um programa que use um loop "while" para contar de 1 até 100
# e imprimir apenas os números divisíveis por 7.
contador3 = 1
while contador3 <= 100:
    if contador3 % 7 == 0:
        print(contador3)

    contador3 += 1


# Crie um programa que use um loop "for" para imprimir os números de 1 a 10 em ordem reversa.
for numero10 in range(10, 0, -1):
    print(numero10)


# Escreva um programa que use um loop "while" para pedir ao usuário para adivinhar um número secreto
# (por exemplo, 42) e encerre o loop quando o usuário adivinhar corretamente.
numero_da_sorte = 42
acertou = False

while not acertou:
    palpite = int(input("Digite o número da sorte: "))

    if palpite == numero_da_sorte:
        print(f"Parabéns você acertou, o número é {numero_da_sorte}")
        acertou = True


# Crie um programa que use um loop "for" para imprimir a tabuada de multiplicação de um número inserido
# pelo usuário (por exemplo, a tabuada do 7).
tabuada_usuario = int(input("digite um numero"))
for i in range(11):
    print(i*tabuada_usuario)

# DESAFIO:
# Implemente o jogo "Pedra, Papel e Tesoura" em que o jogador joga contra o computador.
# Use loops e instruções condicionais para determinar o vencedor.

import random


def jogar_pedra_papel_tesoura():
    options = ["Pedra", "Papel", "Tesoura"]

    while True:
        jogador_escolha = input("Escolha entre: Pedra, Papel ou Tesoura!\n")

        if jogador_escolha == "Sair":
            print("Jogo encerrado.")
            break

        if jogador_escolha not in options:
            print("Escolha inválida! Por favor, escolha entre: Pedra, Papel ou Tesoura")
            continue

        computador_escolha = random.choice(options)
        print(f"O computador escolheu: {computador_escolha}")

        if jogador_escolha == computador_escolha:
            print("Empate!")
        elif (
            (jogador_escolha == "Pedra" and computador_escolha == "Tesoura") or
            (jogador_escolha == "Tesoura" and computador_escolha == "Papel") or
                (jogador_escolha == "Papel" and computador_escolha == "Pedra")):
            print("Parabéns, você venceu!")
        else:
            print("O computador venceu!")


jogar_pedra_papel_tesoura()