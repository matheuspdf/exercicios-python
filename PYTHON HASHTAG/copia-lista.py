
# Para copiar os elementos de uma lista, devemos usar:

# lista2 = lista1.copy()
# ou
# lista2 = lista1[:]


lista1 = ['mouse', 'teclado', 'monitor']

lista2 = lista1.copy()
lista2 = lista1[:]
lista1[2] = 'fone'

print(lista1)
print(lista2)
