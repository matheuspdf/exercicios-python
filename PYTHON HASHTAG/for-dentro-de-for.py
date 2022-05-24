estoque = [
    [102, 89, 47, 425, 206],
    [112, 89, 47, 225, 29],
    [12, 89, 47, 25, 26],
    [192, 89, 47, 255, 256]
]
fabricas = ['FabricaA', 'FabricaB', 'FabricaC', 'FabricaD']
nivel_minimo = 30
fabricas_abaixo_do_nivel = []


for i, lista in enumerate(estoque):
    for qtde in lista:
        if qtde < nivel_minimo:
            if fabricas[i] in fabricas_abaixo_do_nivel:
                pass
            else:
                fabricas_abaixo_do_nivel.append(fabricas[i])

print(fabricas_abaixo_do_nivel)
