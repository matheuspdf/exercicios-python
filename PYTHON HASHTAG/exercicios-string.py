# ----------------Exercícios----------

# CADASTRO DE CPF
cpf = input('insira seu CPF (apenas números)')

# tirar espaços no início e no final
cpf = cpf.strip()
# tirar os pontos
cpf = cpf.replace('.', '')
# tirar os traços
cpf = cpf.replace('-', '')
if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('digite seu CPF corretamente e digite apenas números')
# ----------------------------------------------------------------------------------------------------------
# Cadastro de e-mails
nome = input('Digite seu nome')
email = input('digite seu e-mail')

if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro concluído')
    else:
        print('Email inválido')
else:
    print('Digite seu nome e e-mail corretamente')
