#Imprima os números de 1 a 10 usando um loop while.
numero = 1
while numero <= 10:
    print(numero)
    numero += 1
#Solicite ao usuário um número e imprima a tabuada desse número até 10.
numero = int(input("digite um numero: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(resultado)
    contador += 1

#Peça ao usuário para adivinhar um número entre 1 e 10 e dê dicas até que ele acerte.


#Calcule e imprima a soma dos números de 1 a 100 usando um loop while.
#soma = 0
#numero = 1
#while numero <= 100:
    #soma += numero
  # numero += 1
   #print(soma)

#Conte quantos números pares existem de 1 a 50 usando um loop while.
contador = 1
pares = 0
while contador <= 50:
    if contador % 2 == 0:
        pares += 1
    contador += 1
    print("os numeros pares de 1 a 50 sao: ", pares)


#Peça números ao usuário até que ele digite um número negativo e, em seguida,
# imprima a soma dos números digitados.
soma = 0
numero = int(input("digite um numero e para sair do loop digite um numero negativo: "))
while numero < 0:
    soma += numero
    print(soma)
#Peça ao usuário para inserir um número e calcule seu fatorial usando um loop while.
contador = 1
numero = int(input("digite um numero: "))
while contador <= 10:
    resultado = contador * numero
    print(resultado)
    contador += 1


#Peça ao usuário para inserir um número e determine se é primo usando um loop while.
#numero = int(input("digite um numero: "))
#while numero % 1 == 0:
    #print("o numero é primo")

#Solicite ao usuário que insira uma palavra e verifique se é um palíndromo
# (lê-se igual de trás para frente) usando um loop while.

#Calcule e imprima a média de 5 notas digitadas pelo usuário usando um loop while.
contador = 0
#soma = 0
#while contador < 5:
#nota = float(input("digite as notas: "))
#contador += 1

 #media = soma/5
 #print("a media é ", media)

#Peça ao usuário para inserir números até que a soma dos números digitados seja maior que 100 usando
# um loop while.
soma = 0
while soma <= 100:
    numero =float (input("digite um numero: "))
    soma += numero
    print(soma)

#Implemente um jogo de adivinhação onde o usuário tenta adivinhar um número secreto entre 1 e 100
# usando um loop while.

#Peça ao usuário que insira números até que ele digite dois números consecutivos iguais usando
# um loop while.


#Implemente um conversor de número decimal para binário usando um loop while.


#Peça ao usuário para inserir uma sequência de números separados por vírgulas e calcule a
# média usando um loop while.

#Solicite ao usuário que insira um número e encontre todos os divisores desse número usando um loop while.
divisor = 1
numero = int(input("digite um numero inteiro positivo "))
while divisor <= numero == 0:
    if numero % divisor == 0:
        print(divisor)
        divisor += 1


#Peça ao usuário para inserir um número e imprima a sequência de Fibonacci até esse número usando um
# loop while.

#Peça ao usuário que insira números até que ele digite um número negativo e, em seguida,
#imprima o maior número digitado usando um loop while.
numero = 0
while numero >= 0:
    numero = int(input("digite um numero e um numero negativo para encerrar: "))



#Crie um programa que simule um caixa eletrônico, onde o usuário pode sacar dinheiro até que não
# haja mais saldo disponível usando um loop while.

#Solicite ao usuário que insira uma sequência de números e determine quantos deles são pares
# e quantos são ímpares usando um loop while.
pares = 0
impares = 0
numero = int(input("digite um numero: "))
while numero != 0:
    if numero % 2 == 0:
        pares += 1
    else:
        imapres += 1