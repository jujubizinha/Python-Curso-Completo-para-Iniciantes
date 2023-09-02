"""
Em programação, type casting é a operação de converter o tipo de uma variável de um tipo para outro.
Isso é feito para garantir que a variável seja do tipo correto para a operação que está sendo realizada.
"""
inteiro = 1
real = 2.0
palavra = "5"
print(type(real))
print(type(palavra))
real = int(real)
palavra = int(palavra)
print(type(real))
print(type(palavra))

print(inteiro + palavra)