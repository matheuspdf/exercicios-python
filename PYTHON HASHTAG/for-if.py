vendas = [100, 200, 300, 400, 500, 1000, 1200,
          50, 450, 2000, 900, 650, 830, 320, 210, 750, ]
meta = 750

qtde_bateu_meta = 0

for venda in vendas:
    if venda >= meta:
        qtde_bateu_meta += 1

qtde_funcionarios = len(vendas)

print('O percentual de pessoas que bateram a meta foi de {:.0%}'.format(
    qtde_bateu_meta / qtde_funcionarios))
print(qtde_bateu_meta)
