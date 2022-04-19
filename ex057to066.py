# 057 - Perguntar o sexo e só aceitar F ou M
s = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while s not in 'FM':
    s = str(input('Dados inválidos. Digite apenas M ou F ').upper())
if s == 'F':
    print('Dados recebido com sucesso. Sexo F inserido no banco')
elif s == 'M':
    print('Dados recebido com sucesso. Sexo M inserido no banco')
