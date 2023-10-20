# Criação de Lista: Crie uma lista contendo os nomes de três cores de sua escolha.
# Em seguida, imprima a lista.
cores = ["amarelo", "azul", "vermelho"]
print(cores)
# Acesso a Elementos: A partir da lista criada na questão anterior, imprima o segundo elemento da lista.
print(cores[1])

# Modificação de Elementos: Modifique o primeiro elemento da lista
# para outra cor de sua escolha e, em seguida, imprima a lista atualizada.
cores[0] = "verde"
print(cores)
# Adição de Elementos: Adicione uma cor à lista de cores e imprima a lista resultante.
cores.append("roxo")
print(cores)
# Remoção de Elementos: Remova a última cor da lista e imprima a lista atualizada.
cores.remove("roxo")
print(cores)

# Comprimento da Lista: Determine o número de elementos na lista de cores e imprima esse valor.
print(len(cores))

# Verificação de Elemento: Verifique se uma cor específica (por exemplo, "vermelho")
# está presente na lista e imprima uma mensagem informando se está ou não.
# for cor in cores:
#      if cor == "azul":
#         print("a cor esta na lista")
if "azul" in cores:
    print("a cor esta na lista")

# Fatiamento de Lista: A partir da lista de cores, crie uma nova lista contendo apenas
# as duas primeiras cores e imprima-a.
nova_lista = cores[1:3]
print(nova_lista)
# Inversão de Lista: Inverta a ordem dos elementos na lista de cores e imprima a lista invertida.
# cores_invertidas = cores[::-1]
# print(cores_invertidas)
cores.reverse()
print(cores)
# Ordenação de Lista: Crie uma lista de números desordenados e, em seguida,
# ordene-os em ordem crescente e imprima a lista ordenada.
numeros = [6, 5, 3, 8, 0, 6, 4, 1, 9]
numeros.sort()
print(numeros)

#Desafio!
# Escreva um programa em Python que encontre o menor número em uma lista de números.
# numeros_aleatorios = [100, 29292, 2312 , 321312, 0, 1423, 324]
# menor_numero = min(numeros_aleatorios)
# print(menor_numero)

numeros_aleatorios = [100, 29292, 2312 , 321312, 0, 1423, 324]
menor_numero = numeros_aleatorios[len(numeros_aleatorios) -1]
for i in numeros_aleatorios:
    if i <= menor_numero:
       menor_numero = i

print(menor_numero)





