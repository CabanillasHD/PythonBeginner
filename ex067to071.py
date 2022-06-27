#066 - Ler vários números parar quando 999, quantos digitados e somas deles
# s = c = 0
# while True:
#     n = int(input('Digite um valor: '))
#     if n == 999:
#         break
#     s += n
#     c += 1
# print(f'Foram digitados {c} e a soma deles é {s}')

#067 - Tabuada dos números solicitados
# import time
# n = int(input('Digite o valor para ver sua tabuada: '))
# t = 0
# while True:
#     if n <= 0 or n > 9:
#         break
#     else:
#         for c in range(1, 11):
#             t = n * c
#             time.sleep(0.5)
#             print(f'{c} x {n} = {t}')
#     n = int(input('Quer ver outra tabuada? Digite outro número: '))
# print('Fim da Tabuada')


#068 - Par ou Impar
# import random
# print(10 * '=+')
# print('Jogo de Par ou Ímpar')
# print(10 * '=+')
# np = int(input('Digite um número: '))
# ep = str(input('Par ou Ímpar? ')).upper().strip()[0]
# cont = 0
# while True:
#     nm = random.randint(0, 10)
#     res = np + nm
#     print(f'Você jogou {np} o computador jogou {nm}. O total deu {res}! ')
#     if res % 2 == 0:
#         print('Deu par')
#         if ep in 'pP':
#             print('Você venceu!')
#             cont = cont + 1
#         else:
#             print('Você perdeu!')
#             break
#     else:
#         print('Deu ímpar')
#         if ep in 'iI':
#             print('Você venceu!')
#             cont = cont + 1
#         else:
#             print('Você perdeu!')
#             break
#     np = int(input('Vamos jogar novamente! Escolha outro número: '))
#     ep = str(input('Par ou Ímpar? ')).upper().strip()[0]
# print(f'Você ganhou {cont} rodadas consecutivas')
# #

#069 - Ler idade e sexo
# conthomem = 0
# contmaior = 0
# contmulher20 = 0
# while True:
#     idade = int(input('Digite a idade: '))
#     sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
#     while sexo not in 'FM':
#         sexo = str(input('Sexo incorreto, favor digite F ou M: ')).upper().strip()[0]
#     if idade > 18:
#         contmaior += 1
#     if sexo in 'M':
#         conthomem += 1
#     if sexo in 'F':
#         if idade < 20:
#             contmulher20 += 1
#     continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
#     while continuar not in 'SN':
#         continuar = str(input('Opção inválida, digite S ou N: ')).upper().strip()[0]
#     if continuar not in 'S':
#         break
# print(f'Foram cadastrados {contmaior} pessoas com mais de 18 anos')
# print(f'No total foram cadastrados {conthomem} homens')
# print(f'Foram cadastrados {contmulher20} mulheres com menos de 20 anos')

#070 - ler nome e preço de produtos
# menor = 0
# cont = 0
# barato = ''
# totalcompras = 0
# mais100 = 0
# while True:
#     prod = str(input('Digite o nome do produto: ')).upper()
#     preco = float(input('Digite o valor do produto R$ '))
#     cont += 1
#     totalcompras += preco
#     if cont == 1 or preco < menor:
#         menor = preco
#         barato = prod
#     if preco > 1000:
#         mais100 += 1
#     continuar = str(input('Deseja continuar [S/N]: ')).upper().split()[0]
#     while continuar not in 'SN':
#         continuar = str(input('Opção inválida, digite S ou N: ')).upper().split()[0]
#     if continuar not in 'S':
#         break
# print(f'O valor total das compras foi de R${totalcompras:.2f}')
# print(f'{mais100} produtos valem mais de R$1000,00')
# print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

#071 - Simulador de caixa eletronico
# print('*' * 30)
# print('{:^30}'.format('Banco do Caba'))
# print('*' * 30)
# saque = int(input('Qual valor deseja sacar? R$ '))
# total = saque
# ced = 50
# totalced = 0
# while True:
#     if total >= ced:
#         total -= ced
#         totalced += 1
#     else:
#         if totalced > 0:
#             print(f'Total de {totalced} cédulas de R${ced}')
#         if ced == 50:
#             ced = 20
#             totalced = 0
#         elif ced == 20:
#             ced = 10
#             totalced = 0
#         elif ced == 10:
#             ced = 1
#             totalced = 0
#         if total == 0:
#             break
#
