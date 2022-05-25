venda = input(
    'Insira um produto. Para cancelar, aperte ENTER com a caixa vazia')
vendas = []

while venda != '':
    vendas.append(venda)
    venda = input(
        'Insira um produto. Para cancelar, aperte ENTER com a caixa vazia')

print('Registro Finalizado. Os produtos cadastrados foram: {}'.format(vendas))
