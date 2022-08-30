#101 - Criar uma função voto, recebe ano de nascimento e retorna NEGADO, OPICIONAL, OBRIGATORIO
# def voto(ano):
#     from datetime import date
#     anoatual = date.today().year
#     idade = (anoatual - ano)
#     print(f'Com {idade} anos, o voto é ', end='')
#     if idade < 16:
#         print('NEGADO')#Pode usar o RETURN no lugar do PRINT
#     elif 16 <= idade < 18 or idade > 65:
#         print('OPICIONAL')
#     elif idade >= 18:
#         print('OBRIGATÓRIO')
#
#
# n = int(input('Digite o ano de nascimento: '))
# voto(n)

#102 - Função fatorial e uma função para mostrar ou não o processo.
# def fatorial(num, show=False):
#     f = 1
#     while num > 0:
#         if show:
#             if num == 1:
#                 print(f'{num} = ', end='')
#             else:
#                 print(f'{num} x ', end='')
#         f *= num
#         num -= 1
#     return f
#
#
# #Programa principal
# print(fatorial(9, True))

#103 -
A = int(input())
B = int(input())
SOMA = A + B

print("SOMA = {}".format(SOMA))