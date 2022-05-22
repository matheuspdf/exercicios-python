# # 1.Criando um registro de hóspedes
# qtde_pessoas = int(input('Quantas pessoas terão no quarto?'))
# quarto = []

# for i in range(qtde_pessoas):
#     nome = input('Qual o nome?')
#     cpf = input('Qual o cpf?')
#     hospede = [nome, 'cpf:{}'.format(cpf)]
#     quarto.append(hospede)

# print(quarto)


# # 2. Análise de vendas
# meta = [10000]
# vendas = [['joão', 15000], ['matheus', 20000], [
#     'maria', 9900], ['josé', 5900], ['francisco', 13000]]

# for item in vendas:
#     if item[1] >= meta:
#         print('Vendedor {} bateu a meta. Fez {} vendas'.format(
#             item[0], item[1]))


# 3. Comparação com o ano anterior
produtos = ['iphone', 'galaxy', 'ipad', 'tv',
            'máquina de café', 'geladeira', 'notebook', 'monitor']
vendas2019 = [57896, 35687, 56874, 12548, 25698, 24567, 26412, 75864]
vendas2020 = [45791, 63549, 24689, 15497, 46721, 65329, 19813, 79246]

for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        crescimento = vendas2020[i] / vendas2019[i] - 1
        print('{} vendeu R$ {:,} em 2019, R$ {:,} em 2020 e teve {:.1%} de crescimento'.format(
            produto, vendas2019[i], vendas2020[i], crescimento))
