#lista = é usado para armazenar múltiplos itens em uma única variavél
foods = ["kkkk", "pizza", "morango", "frango frito", "comida japonesa"]
print(foods[0])
foods[0] = "hamburguer"


for i in foods:
    print(i)

animals = ["cachorro", "gato", "girafa", "gafanhoto", "urso"]
print(animals)
animals.remove("cachorro")
print(animals)
print(animals.pop(0))
print(animals)
animals.append("oi")
print(animals)
animals.sort()
print(animals)
animals.insert(1, "elefante")
print(animals)
animals.clear()
print(animals)

# Escreva um programa em Python que encontre o maior número em uma lista de números.
# Você pode criar a lista manualmente ou gerá-la aleatoriamente.
# Em seguida, seu programa deve imprimir o maior número encontrado na lista.

import random

lista_de_numeros = [
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
    random.randint(1, 80000),
]
print(lista_de_numeros)
maior_numero = lista_de_numeros[len(lista_de_numeros) - 1]

for i in range(len(lista_de_numeros)):
    if (lista_de_numeros[i] >= maior_numero):
        maior_numero = lista_de_numeros[i]

print(maior_numero)
