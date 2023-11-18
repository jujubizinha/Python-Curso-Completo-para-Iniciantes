from pilha import Pilha
pilha_exemplo = Pilha()
print(pilha_exemplo.tamanho_pilha())
pilha_exemplo.empilhar(3)
pilha_exemplo.empilhar(8)
print(pilha_exemplo.topo())
print(pilha_exemplo.esta_vazia())
pilha_exemplo.desempilhar()
print(pilha_exemplo.topo())
print(pilha_exemplo.esta_vazia())

