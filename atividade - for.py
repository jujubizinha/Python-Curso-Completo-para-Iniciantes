#Contagem crescente: Escreva um programa que use um loop for para contar de 1 a 10 e exibir cada número.
for i in range (1,11):
    print(i)

#Contagem regressiva: Crie um programa que use um loop for para contar de 10 até 1 e exibir cada número.
for j in range (10,0,-1):
    print(j)

#Tabuada de multiplicação: Solicite ao usuário um número inteiro e use um loop for para exibir a tabuada de multiplicação
# desse número de 1 a 10.
numero = int(input("digite um numero inteiro: "))
for x in range(1,11):
    print(numero * x)

#Soma de números pares: Calcule a soma de todos os números pares de 2 a 20 usando um loop for.
soma = 0
for pares in range(2,21):
    if pares % 2 == 0:
        soma += pares


print(soma)

#Soma de números ímpares: Calcule a soma de todos os números ímpares de 1 a 19 usando um loop for.
soma_impar = 0
for impares in range(1,20):
    if not (impares % 2 == 0):
        soma_impar += impares

print(soma_impar)


#Múltiplos de 3: Use um loop for para exibir todos os múltiplos de 3 de 3 a 30.
for multiplo in range (3,31):
    if multiplo % 3 == 0:
        print(multiplo)

#Fatorial: Solicite ao usuário um número inteiro e use um loop for para calcular o fatorial desse número.
fatorial = 1
numero_int = int(input("digite um numero inteiro: "))
for p in range(1,numero_int):
    fatorial *= p

print(fatorial)

#Verificação de número primo: Peça ao usuário para inserir um número e use um loop for para determinar
# se ele é um número primo.
possivel_primo = int(input("digite um numero inteiro: "))
if possivel_primo < 2:
    print(possivel_primo,"não é um numero primo")
else:
    e_primo = True
    for primo in range(2,(possivel_primo -1)):
        if possivel_primo % primo == 0:
           e_primo = False
           break
    if e_primo:
      print(possivel_primo,"é um numero primo")
    else:
      print(possivel_primo, "não é um numero primo")


#Lista de compras: Crie uma lista de compras e use um loop for para exibir cada item da lista.

#Soma de números positivos: Peça ao usuário para inserir números inteiros positivos e use um loop for para calcular a soma desses números até que o usuário insira zero.

#Esses exercícios são muito simples e ajudarão você a se familiarizar com o uso do loop for em Python. Eles são ótimos para iniciantes.