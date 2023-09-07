"""
Funções matemáticas são funções que realizam operações matemáticas.
Em Python, as funções matemáticas são definidas no módulo math
"""
import math
pi = 3.14
#arredonda para um numero especifico de digitos
print(round(pi,4))

#ceil retorna o menor inteiro maior ou igual ao numero
print(math.ceil(pi))

#floor retorna o maior inteiro menor ou igual ao numero
print(math.floor(pi))

#retorna o valor absoluto
print(abs(pi))

#pow é potenciação
print(pow(pi,5))

#retorna raiz quadrada de um numero
print(math.sqrt(36))

x = int(input("digite o valor de x"))
y = int(input("digite o valor de y"))
z = int(input("digite o valor de z"))

def maior_numero (numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        print(numero1)
    elif numero2 > numero1 and numero2 > numero3:
        print(numero2)
    else:
        print(numero3)


maior_numero(x, y, z)

#retorna o maior valor de conjunto de valores
print(max(x,y,z))

#retorna o menor valor de conjunto de valores
print(min(x,y,z))