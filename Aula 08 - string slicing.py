nome = "Julia Silvestre"
primeiro_nome = nome[:5]
ultimo_nome = nome[6:len(nome)]
nickname = nome[:len(nome):5]
nome_reverso = nome[::-1]
site = "http://google.com"
slice = slice(7, 13)
print(site[-1])
print(site[slice])
print(nome_reverso)
print(nome[6])
print(nickname)
print(len(nome))
print(primeiro_nome)
print(ultimo_nome)

