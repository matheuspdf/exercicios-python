vendas = [100, 150, 1500, 2000, 120]

meta = 110

for venda in vendas:
    if venda < meta:
        print('A loja não ganha bônus')
        break
    print(venda)


vendedores = ['João', 'Maria', 'José', 'Ana', 'Julia']
meta = 130

for venda in vendas:
    if venda < meta:
        continue
    print(venda)
