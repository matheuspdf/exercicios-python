meta = 10000
vendas = [
    ['Margarida', 12000],
    ['João', 9000],
    ['Sebastião', 11000],
    ['Afonso', 8500],
    ['Maria', 15000],
    ['José', 9400],
    ['Miguel', 6700]
]
# Criando lista auxiliar
acima_meta = []

for venda in vendas:
    if venda[1] >= meta:
        acima_meta.append(venda)

print(acima_meta)
print('{:.3%} dos vendedores bateram a meta'.format(
    len(acima_meta) / len(vendas)))


# Calculo diretamente na lista
qtde_vendedores_acima = 0

for venda in vendas:
    if venda[1] >= meta:
        qtde_vendedores_acima += 1

print('{:.3%} dos vendedores bateram a meta'.format(
    qtde_vendedores_acima / len(vendas)))

# Achando o melhor vendedor


melhor_vendedor = ''
maior_venda = 0


for venda in vendas:
    if venda[1] > maior_venda:
        maior_venda = venda[1]
        melhor_vendedor = venda[0]

print('O melhor vendedor foi {} com {} vendas.'.format(
    melhor_vendedor, maior_venda))
