"""
uma variável é um espaço na memória do computador reservado para armazenar um valor.
As variáveis são usadas para armazenar dados que podem ser alterados durante a execução do programa.

As variáveis são definidas usando o operador igual (=). O lado esquerdo do operador de atribuição é
o nome da variável, e o lado direito é o valor que será armazenado na variável.
"""
#TIPO STRING
#String: Representa uma sequência de caracteres.
nome = "julia"
print("ola " + nome)

print(type(nome))
first_name = "julia"
last_name = "ribeiro"
full_name = first_name + " " + last_name
print(full_name)

#TIPO INTEIRO
#Integer: Representa um número inteiro.
idade = 19
print(idade)
idade += 1
print(idade)
print(type(idade))
print("sua idade é:",idade)

#TIPO FLOAT
#Float: Representa um número de ponto flutuante.
peso = 1.7
print(peso)
print(type(peso))

#TIPO BOOLEANDO
#Boolean: Representa um valor booleano (verdadeiro ou falso).
animal = False
print("Você é um humano?",animal)
print(type(animal))




