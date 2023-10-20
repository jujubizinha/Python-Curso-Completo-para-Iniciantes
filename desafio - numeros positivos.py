valor_1 = float(input("digite um valor: "))
valor_2 = float(input("digite um valor: "))
valor_3 = float(input("digite um valor: "))
valor_4 = float(input("digite um valor: "))
valor_5 = float(input("digite um valor: "))
valor_6 = float(input("digite um valor: "))
contador = 0
soma = 0
if valor_1 >= 0:
    soma += valor_1
    contador += 1

if valor_2 >= 0:
    soma += valor_2
    contador += 1

if valor_3 >= 0:
    soma += valor_3
    contador += 1

if valor_4 >= 0:
    soma += valor_4
    contador += 1

if valor_5 >= 0:
    soma += valor_5
    contador += 1

if valor_6 >= 0:
    soma += valor_6
    contador += 1

print(contador,"valores positivos")
print(soma/contador)


