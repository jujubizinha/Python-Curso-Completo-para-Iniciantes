# A entrada do usuário é uma forma de coletar dados do usuário de um programa.
nome =  input("qual o seu nome?: ")
idade = int(input("qual sua idade?: "))
altura = float(input("qual sua altura?: "))
print(type(idade))
print("oioi " + nome)
print(idade)
print(altura)

print("oi ", nome, "voce tem ", idade, "anos, e sua altura é", altura )

print("Olá," + nome +"!" " Você tem " + str(idade) + " anos" + " e uma altura de: " + str(altura))

print("Olá,{}! Você tem {} anos e mede {} metros.".format(nome, idade, altura))

print(f"Olá,{nome}! Você tem {idade} anos e mede {altura} metros.")

print("Olá", nome +"!", "Você tem ", idade, "anos, e sua altura é", altura )

