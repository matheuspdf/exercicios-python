metaFuncionario = 10000
metaLoja = 250000
vendasFuncionario = 15000
vendasLoja = 250000

notaFuncionario = 5
metaNota = 9


if notaFuncionario >= metaNota or (vendasFuncionario >= metaFuncionario and vendasLoja >= metaLoja):
    bonus = 0.03 * vendasFuncionario
    print(f'Bônus do funcionário foi de {bonus}')
else:
    print(f'Funcionário não ganhou bônus')
