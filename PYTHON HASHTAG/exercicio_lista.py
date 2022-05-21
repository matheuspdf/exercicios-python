produtos = ['computador', 'mouse', 'livro', 'tv']

produtos_ecommerce = [[10000, 2500], [50000, 40], [7000, 1200], [20000, 150]]

qtde = 50000
preco = 40
total = qtde * preco
print('{:,}'.format(total))


if 'livro' in produtos:
    i_livro = produtos.index('livro')
    print(i_livro)
    total_antigo = produtos_ecommerce[i_livro][0] * \
        produtos_ecommerce[i_livro][1]
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * 1.1
    novo_total = produtos_ecommerce[i_livro][0] * \
        produtos_ecommerce[i_livro][1]
    print('Vamos pagar de imposto a mais: R${:,}'.format(
        novo_total - total_antigo))
