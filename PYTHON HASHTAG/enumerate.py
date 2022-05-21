# Enumerate permite que você percorra uma lista e ao mesmo tempo tenha em uma variável o índice daquele item.


estoque = [100, 20, 30, 23, 65, 12, 29, 34, 33, 55]
produtos = ['dolly', 'cerveja', 'pepsi', 'coca', 'agua',
            'vinho', 'del valle', 'guarana', 'sprite', 'fanta']

nivel_minimo = 30

for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print('{} está abaixo do nível mínimo. Temos apenas {} unidades'.format(
            produtos[i], qtde))
