#Em Python, os métodos de string são funções que podem ser usadas para manipular strings.
#Existem muitos métodos de string disponíveis, e cada um deles tem uma função diferente.
nome = "sophia"
#quantidade de caracteres
print(len(nome))

#verifica em qual posição tem a letra, se não tiver retorna -1
print(nome.find("S"))

#Transformar a primeira letra em Maiuscula
print(nome.capitalize())

#juntando 2 funções
print(nome.capitalize().find('S'))

#armazenando na memória após utilizar o capitalize
nome = nome.capitalize()
print(nome)
print(nome.find("S"))

#transformar todos os caracteres em maiusculo
print(nome.upper())

#transformar todos os caracteres em minusculo
print(nome.lower())

#verifica se a variavel é um digito
print(nome.isdigit())

#verifica se a variavel é um alpha(alfabeto)
print(nome.isalpha())

#quantidade de um caractere especifico
print(nome.count("S"))

#troca determinado caractere por outro
print(nome.replace("o","i"))

print(nome*3)