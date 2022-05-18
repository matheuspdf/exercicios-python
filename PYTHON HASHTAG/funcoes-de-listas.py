# Tamanho da lista
#tamanho = len(lista)

from wsgiref.validate import validator


produtos = ['celular', 'tablet', 'relógio', 'mouse', 'teclado', 'monitor']

tamanho = len(produtos)
print(f'Temos {tamanho} produtos')

# Maior e Menor valor
# maior = max(lista)
# menor = min(lista)

vendas = [130, 120, 150, 200, 450, 220]

# qual é o item mais vendido?
# qual é o item menos vendido?

maisVendido = max(vendas)
menosVendido = min(vendas)
print(
    f'O produto mais vendido teve {maisVendido} unidades vendidas e o menos vendido teve {menosVendido} unidades vendidas')

i = vendas.index(maisVendido)
produtoMaisVendido = produtos[i]
print(f'{produtoMaisVendido} foi o produto mais vendido')

i = vendas.index(menosVendido)
produtoMenosVendido = produtos[i]
print(f'{produtoMenosVendido} foi o produto menos vendido')
