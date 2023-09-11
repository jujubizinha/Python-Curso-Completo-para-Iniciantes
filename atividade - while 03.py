#Contagem de números pares: Escreva um programa que conte e exiba
# todos os números pares de 2 a 20 usando um loop while.
pares = 2
while pares <= 20:
        print(pares)
        pares += 2


#Contagem regressiva até zero: Crie um programa que conte de um número fornecido pelo usuário até zero e
# exiba cada número no processo.
numero = int(input("digite um numero inteiro: "))
while numero >= 0:
    print(numero)
    numero -= 1

#Soma de números positivos: Solicite ao usuário que insira números inteiros positivos e calcule a soma
# desses números até que o usuário insira zero.
numero_positivo = int(input("digite um numero inteiro positivo(coloque 0 para encerrar: "))
soma = 0
while numero_positivo != 0:
     soma += numero_positivo
     numero_positivo = int(input("digite um numero inteiro positivo(coloque 0 para encerrar: "))

print(soma)

#Média de números positivos: Peça ao usuário para inserir números inteiros positivos e calcule a média
# desses números até que o usuário insira zero.
media = 0
soma_numero = 0
quantidade_numero = 0
numeros = int(input("digite um numero inteiro positivo(digite -1 para parar): "))
while numeros >= 0:
    quantidade_numero += 1
    soma_numero += numeros
    numeros = int(input("digite um numero inteiro positivo(digite -1 para parar): "))

media = soma_numero / quantidade_numero
print(media)


#Adivinhe o número com dicas: Faça um jogo em que o programa escolhe um número aleatório entre 1 e 100,
# e o usuário tenta adivinhar o número. O programa fornece dicas indicando se o número é maior ou menor.
#int(input("escolha um numero entre 1 a 100: ")

#Tabuada de multiplicação: Solicite ao usuário um número inteiro e exiba a tabuada de multiplicação desse
# número de 1 a 10.
numero_int = int(input("digite um numero inteiro: "))
contador = 1
multiplicação = 0
while contador <= 10:
    multiplicação = contador * numero_int
    print(multiplicação)
    contador += 1



#Verificação de número primo: Peça ao usuário para inserir um número e determine se ele é um número primo
# ou não usando um loop while.
numero_primo = int(input("digite um numero: "))
divisor = 2
primo = 1
while divisor < numero_primo:
    if numero_primo < 2:
       print("não é primo")
       break
    if numero_primo % divisor == 0:
        primo = 0
        divisor += 1
    if primo == 1 and numero_primo > 1:
     print("é um numero primo")
     break
    else:
     print("nao é primo")

#Conversão de unidades: Crie um programa que converta a temperatura de graus Celsius para Fahrenheit
# ou vice-versa, dependendo da escolha do usuário.
opcao = ""

while opcao != "3":
    print("Escolha uma opção:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(fahrenheit)
    elif opcao == '2':
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(celsius)
    else:
        break


#Soma dos múltiplos de 3 e 5: Calcule a soma de todos os múltiplos de 3 e 5 menores que 100.
numero = 1
soma = 0
while numero < 100:
    if numero % 3 == 0 and numero % 5 == 0:
        soma += numero
    numero += 1
    print(soma)

#Calculadora simples: Implemente uma calculadora que solicite ao usuário que insira dois números
# e uma operação (adição, subtração, multiplicação ou divisão) e depois realize o cálculo.
numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input("digite o segundo numero: "))
operaçao = input("escolha a operaçao: adição, subtração, multiplicação ou divisão ")

while numero1 and numero2 >= 0:
    if operaçao == '+':
        resultado = numero1 + numero2
    elif operaçao == '-':
        resultado = numero1 - numero2
    elif operaçao == '*':
        resultado = numero1 * numero2
    elif operaçao == '/':
        resultado = numero1 / numero2
        print(resultado)