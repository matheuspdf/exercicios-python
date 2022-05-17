produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado']
estoque = [100, 150, 200, 250, 120]

i = produtos.index('mouse')
qtdeEstoque = estoque[i]

print(f'Quantidade em estoque de mouse é de: {qtdeEstoque}')


produto = input('Insira o nome do produto em letra minúscula: ')
if produto in produtos:
    i = produtos.index(produto)
    qtdeEstoque = estoque[i]
    print(f'Temos {qtdeEstoque} unidades de {produto} no estoque')
else:
    print(f'{produto}  não existe no estoque')
