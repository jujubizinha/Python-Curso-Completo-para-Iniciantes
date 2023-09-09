idade = int(input("qual sua idade?"))
if idade >= 18 and idade != 100:
    print(" voce é maior de idade")
elif idade < 0:
    print("voce nem nasceu ainda")
elif idade == 100:
    print("voce tem 100 anos")
else:
    print("voce é menor de idade")