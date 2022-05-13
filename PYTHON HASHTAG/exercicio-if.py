produto = input('qual é o produto?')
categoria = input('qual é a categoria?')
qtde = input('digite a quantidade atual do produto: ')


if produto and categoria and qtde:
    qtde = int(qtde)
    if categoria == 'bebidas':
        if qtde < 75:
            print(
                f'solicitar {produto} à equipe de compras, temos apenas {qtde} unidades em estoque')
        elif categoria == 'limpeza':
            if qtde < 30:
                print(
                    f'Solicitar  {produto} à equipe de compras, temos apenas {qtde} unidades em estoque')
        else:
            if qtde < 50:
                print(
                    f'solicitar {produto} à equipe de compras, temos apenas {qtde} em estoque')
else:
    print('preencha todas as informações')
