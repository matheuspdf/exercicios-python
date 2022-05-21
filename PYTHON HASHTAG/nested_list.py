# Listas de listas

# Quando temos umas lista dentro de outras lista, temos uma nested list

vendedor = ['joao', 'jose', 'mauricio', 'maria']
produtos = ['mouse', 'teclado']
vendas = [[100, 200],
          [200, 90],
          [10, 400],
          [500, 20]
          ]
# Quanto Joao vendeu de mouse?
vendasJoaoMouse = vendas[0][0]
print(f'Joao vendeu {vendasJoaoMouse} mouses')

# Quanto maria vendeu de teclado?
vendasMariaTeclado = vendas[3][1]
print(f'Maria vendeu {vendasMariaTeclado} teclados')

# Qual é o total de vendas de mouse?
vendasMouse = vendas[0][0] + vendas[1][0] + vendas[2][0] + vendas[3][0]
print(f'O número total de vendas de mouse é de: {vendasMouse}')


# E se mauricio vendeu apenas 5 teclados?
vendas[2][1] = 5
print(vendas)

# E para adicionar um novo produto a primeira lista?
vendasMonitor = [3, 9, 2, 7]
vendas[0].append(vendasMonitor[0])
vendas[1].append(vendasMonitor[1])
vendas[2].append(vendasMonitor[2])
vendas[3].append(vendasMonitor[3])
print(vendas)
