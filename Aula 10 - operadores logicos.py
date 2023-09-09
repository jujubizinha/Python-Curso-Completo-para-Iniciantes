#os operadores lógicos são usados para combinar duas ou mais expressões booleanas
# e produzir uma expressão booleana como resultado.
temperatura = float(input("digite uma temperatura: "))
if temperatura >= 0 and temperatura <= 30:
    print("o dia esta agradavel")
elif temperatura < 0 or temperatura > 30:
    print("o dia esta ruim")


if not (temperatura >= 0 and temperatura <= 30):
    print("o dia esta ruim")
elif not (temperatura < 0 or temperatura > 30):
    print("o dia esta agradavel")

#Exercício - Classificação do Tráfego:

#Crie um programa que determine a classificação do tráfego com base em várias condições:

#Se o número de carros for igual ou inferior a 10 e não houver acidentes reportados, classifique o tráfego como "Leve".
#Se o número de carros for superior a 10 e inferior a 30 e não houver acidentes reportados, classifique o tráfego como "Moderado".
#Se houver um acidente reportado, independentemente do número de carros, classifique o tráfego como "Trânsito Pesado".
#Se o número de carros for igual ou superior a 30 e não houver acidentes reportados, classifique o tráfego como "Congestionado".

carros = float(input("digite o numero de carros: "))
acidentes = float(input("reporte os acidentes: "))
if carros <= 10 and acidentes == 0:
    print("leve")
elif carros > 10 and carros < 30 and acidentes == 0:
    print("moderado")
elif acidentes == 1:
    print("transito pesado")
elif carros >= 30 and acidentes == 0:
    print("congestionado")
