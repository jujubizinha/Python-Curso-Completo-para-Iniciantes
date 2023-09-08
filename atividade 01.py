#Declare três variáveis a, b e c e atribua valores a elas.
# Em seguida, imprima o resultado da soma dessas variáveis.
#Atribuição Múltipla:
a, b, c = 10, 20, 30
print(a + b + c)


#Atribua os valores 10, 20 e 30 a três variáveis em uma única linha.
#Em seguida, imprima esses valores.
#Métodos de String:
a, b, c= 10, 20 , 30
print(a)
print(b)
print(c)

#Declare uma variável frase com uma frase de sua escolha.
# Use o método .upper() para imprimir a mesma frase em letras maiúsculas.
#Conversão de Tipo:
fala = "oi! tudo bem?"
print(fala.upper())

#Peça ao usuário para digitar um número como uma string e,
# em seguida, converta-o para um número inteiro e imprima-o.
#Entrada do Usuário:
numero = int(input("digite um numero: "))
print(numero)

#Peça ao usuário para inserir seu nome e, em seguida, imprima uma mensagem
# de boas-vindas usando o nome fornecido.
#Funções Matemáticas:
nome = input("digite seu nome: ")
print("Boas-vindas!", nome,".")


#Peça ao usuário para inserir um número decimal.
# Use a função round() para arredondar o número para duas casas decimais e imprima o resultado.
#Fatiamento de String:
decimal = float(input("digite um numero decimal: "))
print(round(decimal))

#Declare uma variável fruta com o valor "banana".
# Use o fatiamento de string para imprimir apenas os três primeiros caracteres da palavra.
fruta = "banana"
print(fruta[0:3])

#Peça ao usuário para inserir um número.
# Se o número for maior que 10, imprima "O número é maior que 10". Caso contrário, imprima "O número
# não é maior que 10".
#Condições Múltiplas (if-elif):
numero = float(input("digite um numero: "))
if numero > 10:
    print("O número é maior que 10.")
else:
    print("O número não é maior que 10.")

#Peça ao usuário para inserir um número.
# Em seguida, verifique se o número é positivo, negativo ou zero e imprima uma mensagem apropriada.
numero = float(input("digite um numero: "))
if numero > 0:
    print("O número é positivo.")
elif numero == 0:
    print("O número é igual a 0")
else:
    print("O número é negativo")