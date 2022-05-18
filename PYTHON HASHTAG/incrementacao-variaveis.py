# Estrutura:

# variavel = variavel + outroValor

# ou

# variavel += outro valor


lista = ['celular', 'tablet']
vendas = [100, 200]
lista += ['mouse']
print(lista)


somaVendas = 300
somaVendas += 500
print(somaVendas)

email = f'Esse mês vendemos um total de {somaVendas}, sendo:\n{vendas[0]} unidades de {lista[0]} \n{vendas[1]} unidades de {lista[1]}'

email += f'\n {500} unidades de mouse'
print(email)
