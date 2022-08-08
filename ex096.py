#096 - Criar função para calcular área
# def area(l, c):
#     a = c * l
#     print(f'O terreno de {l} de largura e {c} de comprimento, tem uma área de {a}m²')
#
#
# print('Controle de Terrenos')
# print('-=' * 15)
# area(float(input('Largura [m]:')), float(input('Comprimento [m]:')))


#097 - Função para adpatar texto as linhas
# def escreva(frase):
#     tam = len(frase) + 4
#     print('-' * tam)
#     print(f'  {frase}')
#     print('-' * tam)
#
#
# escreva(str(input('Frase: ')))

#098 - Função contador(), receba 3 parâmetros
# from time import sleep
#
#
# def contador(i, f, p):
#     print('-=' * 15)
#     print(f'Contagem de {i} até {f} de {p} em {p}: ')
#     sleep(1)
#     if p == 0:
#         p = 1
#     if i < f:p
#         while i <= f:
#             if p < 0:
#                 p *= -1
#             print(f'{i} ', end='')
#             i += p
#             sleep(0.5)
#         print()
#     else:
#         while i >= f:
#             if p < 0:
#                 p *= -1
#             print(f'{i} ', end='')
#             i -= p
#             sleep(0.5)
#         print()
#
#
# contador(1, 10, 1)
# contador(10, 0, 2)
# i = int(input('Inicio: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
# contador(i, f, p)

#099 - Fazer uma função que recebe vários valores e diga o qual o maior
# def maior(*num):
#     mnum = 0
#     cont = 0
#     for i, c in enumerate(num):
#         if i == 0:
#             mnum = c
#         elif c > mnum:
#             mnum = c
#         cont += 1
#     print(f'O maior número foi o {mnum}')
#     print(f'Foram digitados {cont} números')
#     print('-=' * 15)
#
#
# maior(1, 15, 6, 8, 9, 34)
# maior(1, 2)
# maior(6)
# maior()

#100 - Fazer uma formula para sortear 5 num e jogar em uma lista e criar uma função para somar os pares da lista
# from random import randint
#
#
# def sortear(lista):
#     for c in range(0, 5):
#         lista.append(randint(1, 10))
#     print(lista)
#
#
# def somapar(lista):
#     somapares = 0
#     for c in lista:
#         if c % 2 == 0:
#             somapares += c
#     print(f'A soma dos pares é {somapares}')
#
#
# num = []
# sortear(num)
# somapar(num)
