from typing import TextIO


texto = ''' matheus
Lopes '''

# capitalize() -> Coloca a 1ª letra Maiúscula
print(texto.capitalize())

# casefold() -> Transforma todas as letras em minúsculas
print(texto.casefold())

# count() -> Mostra quantas vezes um valor aparece na string
print(texto.count('s'))

# endswith() -> Verifica se o texto termina com um valor específico e retorna True ou False
print(texto.endswith('Lopes'))

# find() -> Procura um texto dentro de outro texto e retorna a posição do texto encontrado
print(texto.find('m'))

# format() -> Formata uma string de acordo com os valores passados
print(f'Meu nome é {texto}')

# isalnum -> Verifica se o texto é composto unicamente por letras e números
print(texto.isalnum())

# isalpha() -> Verifica se o texto é composto apenas por letras
print(texto.isalpha())

# isnumeric() -> Verifica se o texto é composto apenas por números
print(texto.isnumeric())

# replace() -> Substitui um texto por outro em uma string
print(texto.replace('m', 'M'))

# split() -> Separa uma string de acordo com um delimitador em vários textos diferentes
print(texto.split('L'))

# splitlines() -> separa um texto em vários textos de acordo com os 'enters'
print(texto.splitlines())

# startswith() -> Verifica se a string começa com determinado texto
print(texto.startswith('ma'))

# strip() -> retira caracteres indesejados dos textos. Por padrão, retira espaços "extras" no início e no final
print(texto.strip())

# title() -> Coloca a 1ª letra de cada palavra em maiúscula
print(texto.title())

# upper -> Coloca o texto todo em letra maiúscula
print(texto.upper())


