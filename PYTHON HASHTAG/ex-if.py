# A meta é 1000 vendas.
# Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.
# Caso contrário o valor de bônus é 0.
# Print o bônus dos 3 funcionários.
funcionario1 = 1000
funcionario2 = 770
funcionario3 = 2700

if funcionario1 >= 1000:
    print(f'O funcionário 1 ganhou {funcionario1 * 0.1} de bônus')

if funcionario2 >= 1000:
    bonus = funcionario2 * 0.1
else:
    bonus = 0
print(f'O funcionário 2 ganho {bonus}')


if funcionario3 >= 1000:
    bonus = funcionario3 * 0.1
else:
    bonus = 0
print(f'O funcionário 3 ganhou {bonus}')





