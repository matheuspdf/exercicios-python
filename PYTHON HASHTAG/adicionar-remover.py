# ADICIONAR E REMOVER ITENS DE UMA LISTA

# ADICIONAR:
# lista.append(item)

# REMOVER:
# item removido = lista.pop(indice)
# lista.remove(item)

from math import prod


produtos = ['celular', 'tablet', 'relógio', 'fogão', 'geladeira']
print(produtos)
# adicionar
produtos.append('microondas')
print(produtos)

# remover
itemRemovido = produtos.pop(3)
print(produtos)
print(f'o item {itemRemovido} foi removido da lista')


# 2 formas de tratar erro

# Criar um if para evitar que ele aconteça
# Esperar que ele possa acontecer e tratar caso o erro aconteça

# try:
#   tentar fazer
# except:
#   Caso dê errado
try:
    produtos.remove('tablt')
    print(produtos)
except:
    print('não existe isso na lista')
