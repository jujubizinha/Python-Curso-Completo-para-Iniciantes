numero = 10
while numero > 0:
    print(numero)
    numero -= 1

numero1 = float(input("digite um numero: "))
contador = 0
while contador <= numero1:
    print(contador)
    contador += 1

numero_inteiro = int(input("digite numeros inteiros: "))
soma = 0
while numero_inteiro != 0:
    soma = soma + numero_inteiro
    numero_inteiro = int(input("digite numeros inteiros: "))
print(soma)

numero_positivo = int(input("digite um numero inteiro positivo: "))
aux = 0
while aux < numero_positivo:
    if  (aux % 5 == 0):
        print(aux)
    aux += 1


