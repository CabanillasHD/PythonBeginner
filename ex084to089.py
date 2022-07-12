# 084 - Colocar varias nomes nas lista, informar mais pesada e mais leve
# lista = list()
# grupo = list()
# pleve = list()
# ppesada = list()
# pesado = leve = 0
# while True:
#     lista.append(str(input('Nome: ')))
#     lista.append(float(input('Peso: ')))
#     grupo.append(lista[:])
#     lista.clear()
#     contiuar = str(input('Continuar? [S/N]')).split()[0]
#     if contiuar in 'Nn':
#         break
# for i, v in enumerate(grupo):
#     if i == 0:
#         leve = pesado = v[1]
#     elif v[1] < leve:
#         leve = v[1]
#     elif v[1] > pesado:
#         pesado = v[1]
#     if v[1] >= 70.0:
#         ppesada.append(v[0])
#     elif v[1] <= 70:
#         pleve.append(v[0])
# print(f'Foram digitados {len(grupo)} valores')
# print(f'O maior peso foi {pesado} e as pessoas mais pesadas são {ppesada}')
# print(f'O menor peso foi {leve} e as pessoas mais leves são {pleve}')

# 085 - Receber 7 números e e separar pares e ímparas na mesma lista
# num = list()
# par = list()
# impar = list()
# for c in range(0, 7):
#     num.append(int(input('Digite um valor: ')))
# for v in num:
#     if v % 2 == 0:
#         par.append(v)
#     else:
#         impar.append(v)
# num.clear()
# par.sort()
# impar.sort()
# num.append(par[:])
# num.append(impar[:])
# #print(num)
# print(f'O valores pares são {num[0]}, e os ímpares são {num[1]}')

# 086 - Criar uma matriz 3x3
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         n = int(input(f'Digite um valor [{l},{c}] : '))
#         matriz[l][c] = n
# print(f'=*=' * 10)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()
# print(f'=*=' * 10)

#087 - Trabalhar o sobre matriz
#
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# somapar = somater = maiorseg = 0
# for l in range(0, 3):
#     for c in range(0, 3):
#         n = int(input(f'Digite um valor [{l},{c}] : '))
#         matriz[l][c] = n
#         if matriz[l][c] % 2 == 0:
#             somapar += matriz[l][c]
#         if c == 2:
#             somater += matriz[l][c]
#         if l == 1:
#             if c == 0:
#                 maiorseg = matriz[l][c]
#             else:
#                 if maiorseg < matriz[l][c]:
#                     maiorseg = matriz[l][c]
# print(f'=*=' * 10)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()
# print(f'=*=' * 10)
# print(f'A soma de números pares é {somapar}')
# print(f'A soma da terceira coluna é igual a {somater}')
# print(f'O maior da segunda linha é {maiorseg}')

#088 - MEGA SENA
# from random import randint
# from time import sleep
# jogo = []
# jogos = []
# tot = 1
# print('{:*^30}'.format(' MEGA SENA '))
# qtd = int(input('Quantos jogos você quer ? '))
# while tot <= qtd:
#     cont = 0
#     while True:
#         n = randint(1, 60)
#         if n not in jogo:
#             jogo.append(n)
#             cont += 1
#         if cont >= 6:
#             break
#     jogo.sort()
#     jogos.append(jogo[:])
#     jogo.clear()
#     tot += 1
# for i, j in enumerate(jogos):
#     print(f'Jogo {i+1}: {j}')
#     sleep(1.1)

#089 - Criar boletim de alunos, com nome, 2 notas e média.
# from time import sleep
# boletim = []
# alunos = []
# notas = []
# asnotas = []
# medias = []
# media = 0
# while True:
#     nome = str(input('Nome: '))
#     alunos.append(nome)
#     for n in range(0, 2):
#         nota = float(input(f'Nota {n + 1}: '))
#         notas.append(nota)
#     media = (notas[0] + notas[1]) / 2
#     medias.append(media)
#     asnotas.append(notas[:])
#     notas.clear()
#     continuar = str(input('Continuar [S/N]')).upper().split()[0]
#     if continuar in 'N':
#         break
# boletim.append(alunos)
# boletim.append(asnotas)
# boletim.append(medias)
# print('_' * 20)
# for n in range(len(boletim[0])):
#     print(f'{n:<5}{boletim[0][n]:<10}{boletim[2][n]:^5.1f}')
# print('_' * 20)
#
# print('=*' * 30)
# while True:
#     sel = int(input('Ver a nota de qual aluno: [999 para parar]: '))
#     if sel != 999:
#         print(f'As notas do(a) {boletim[0][sel]} foram {boletim[1][sel]}')
#     print('=*' * 30)
# print('Fechando o programa....')
# sleep(1.5)
# print('Volte sempre e bons estudos!!')


# def print_alpha_nums(abc_list, num_list):
#     for char in abc_list:
#         for num in num_list:
#             print(char, num)
#     return
#
#
# print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])

