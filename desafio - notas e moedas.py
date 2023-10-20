# Leia um valor de ponto flutuante com duas casas decimais.
# Este valor representa um valor monetário. A seguir,
# calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
# As notas consideradas são de 100, 50, 20, 10, 5, 2.
# As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
# seguir mostre a relação de notas necessárias.
from decimal import Decimal

valor = Decimal(input("Digite um valor: "))
nota_100 = nota_50 = nota_20 = nota_10 = nota_5 = nota_2 = 0
moeda_1 = moeda_50 = moeda_25 = moeda_10 = moeda_5 = moeda_01 = 0

while valor > 0:
    if valor >= Decimal('100'):
        valor -= Decimal('100')
        nota_100 += 1
    elif valor >= Decimal('50'):
        valor -= Decimal('50')
        nota_50 += 1
    elif valor >= Decimal('20'):
        valor -= Decimal('20')
        nota_20 += 1
    elif valor >= Decimal('10'):
        valor -= Decimal('10')
        nota_10 += 1
    elif valor >= Decimal('5'):
        valor -= Decimal('5')
        nota_5 += 1
    elif valor >= Decimal('2'):
        valor -= Decimal('2')
        nota_2 += 1
    elif valor >= Decimal('1'):
        valor -= Decimal('1')
        moeda_1 += 1
    elif valor >= Decimal('0.50'):
        valor -= Decimal('0.50')
        moeda_50 += 1
    elif valor >= Decimal('0.25'):
        valor -= Decimal('0.25')
        moeda_25 += 1
    elif valor >= Decimal('0.10'):
        valor -= Decimal('0.10')
        moeda_10 += 1
    elif valor >= Decimal('0.05'):
        valor -= Decimal('0.05')
        moeda_5 += 1
    elif valor >= Decimal('0.01'):
        valor -= Decimal('0.01')
        moeda_01 += 1

print(f"{nota_100} nota(s) de R$ 100,00")
print(f"{nota_50} nota(s) de R$ 50,00")
print(f"{nota_20} nota(s) de R$ 20,00")
print(f"{nota_10} nota(s) de R$ 10,00")
print(f"{nota_5} nota(s) de R$ 5,00")
print(f"{nota_2} nota(s) de R$ 2,00")
print(f"{moeda_1} moeda(s) de R$ 1,00")
print(f"{moeda_50} moeda(s) de R$ 0,50")
print(f"{moeda_25} moeda(s) de R$ 0,25")
print(f"{moeda_10} moeda(s) de R$ 0,10")
print(f"{moeda_5} moeda(s) de R$ 0,05")
print(f"{moeda_01} moeda(s) de R$ 0,01")