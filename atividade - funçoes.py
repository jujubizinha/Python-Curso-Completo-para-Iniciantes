# Escreva uma função para calcular a média de uma lista de números.
# Crie uma função para verificar se um número é primo.
# Implemente uma função que converta uma temperatura de Celsius para Fahrenheit.
# Escreva uma função para verificar se uma string é um palíndromo.
# Crie uma função que calcule o fatorial de um número inteiro não negativo.

def calcular_media_de_uma_lista_de_numeros(lista):
   media =  sum(lista)/len(lista)
   return media

def verificar_se_um_numero_e_primo(numero):
    if numero > 1 and numero % numero == 0 and numero % 1 == 0:
     return True
    else:
     return False

def converter_uma_temperatura_de_Celsius_para_Fahrenheit(graus_celsius):
  graus_Fahrenheit = (graus_celsius * 1.8 + 32)
  return graus_Fahrenheit

def verificar_se_uma_string_e_um_palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        return True
    else:
        return False


def calcular_o_fatorial_de_um_numero_inteiro_nao_negativo(numero):
    if numero < 0:
        return "O numero é negativo"
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1,numero+1):
            resultado*= i
        return resultado

numero = [22, 40, 32, 3493, 3123, 545]
print(calcular_media_de_uma_lista_de_numeros(numero))
print(verificar_se_um_numero_e_primo(23))
print(converter_uma_temperatura_de_Celsius_para_Fahrenheit(0))
print(verificar_se_uma_string_e_um_palindromo("bolo"))
print(calcular_o_fatorial_de_um_numero_inteiro_nao_negativo(5))