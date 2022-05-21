# Estrutura de Repetição: for

# for i in range(n)
#   repetir código n vezes

produtos = ['mouse', 'teclado', 'monitor', 'fone', 'gabinete']
producao = [100, 150, 200, 250, 320]

tamanho = len(produtos)
for i in range(tamanho):
    print(f'{producao[i]} unidades produzidas de {produtos[i]}')
