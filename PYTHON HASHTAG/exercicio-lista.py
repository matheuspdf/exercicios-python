# faturamento do melhor e do pior mês do ano
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
         'jul', 'ago', 'set', 'out', 'nov', 'dez']

vendas1sem = [25000, 29000, 22200, 17750, 15870, 19000]
vendas2sem = [19850, 20120, 17989, 15555, 99999, 100]


# juntando as duas listas de vendas com o método extend
vendas1sem.extend(vendas2sem)

maiorValor = max(vendas1sem)
menorValor = min(vendas1sem)
print(maiorValor)
print(menorValor)


# pegando a posição do maior e menor valor dentro da lista
iMaiorValor = vendas1sem.index(maiorValor)
iMenorValor = vendas1sem.index(menorValor)

print(f'O melhor mês do ano foi {meses[iMaiorValor]} com {maiorValor} vendas')
print(f'O pior mês do ano foi {meses[iMenorValor]} com {menorValor} vendas')

faturamentoTotal = sum(vendas1sem)
print('Faturamento total: R${:,}'.format(faturamentoTotal))

percentual = maiorValor / faturamentoTotal
print(
    'O melhor mês representou {:.1%} das vendas do ano todo'.format(percentual))


# Pegar os três maiores valores da lista
top3 = []

maiorValor = max(vendas1sem)
top3.append(maiorValor)

vendas1sem.remove(maiorValor)
maiorValor = max(vendas1sem)
top3.append(maiorValor)

vendas1sem.remove(maiorValor)
maiorValor = max(vendas1sem)
top3.append(maiorValor)

print(top3)
