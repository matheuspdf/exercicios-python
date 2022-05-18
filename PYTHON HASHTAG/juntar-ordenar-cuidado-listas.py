# lista1.extend(lista2)
#listaNova = lista1 + lista2

from operator import truediv


produtos = ['celular', 'tablet', 'mouse']
novosProdutos = ['teclado', 'monitor', 'fone']

todosProdutos = produtos + novosProdutos

print(todosProdutos)


# Cuidado:
# [1] + [2] não é a mesma coisa que 1+2.

vendas = [100, 300, 250, 400, 180, 500]
vendasCelular = [100]
vendasTablet = [300]

totalPortatil = vendas[0] + vendas[1]
totalPortatilListas = vendasCelular[0] + vendasTablet[0]

print(totalPortatil)
print(totalPortatilListas)


# Ordenar
# lista.sort() /// (reverse=True -> ordena ao contrário)

novaLista = ['matheus', 'joao', 'jose', 'maria']
novaLista.sort(reverse=True)
print(novaLista)
