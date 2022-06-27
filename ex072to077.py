#072 - Escrever número por extenso
# extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
#            'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezesete', 'dezeoito', 'dezenove', 'vinte')
# continuar = 'S'
# while continuar in 'Ss':
#     while True:
#         n = int(input('Digite um número de 0 a 20: '))
#         if 0 <= n <= 20:
#             break
#         print('Tente novamente. ', end='')
#     print(f'O seu extenso é {extenso[n]}')
#     continuar = str(input('Deseja continuar [S/N]')).upper().strip()[0]
# print('Programa encerrado')


#073 - Tabela do brasileirão
# tabela = ('Cruzeiro',	'Bahia',	'Vasco',	'Sport',	'Grêmio',	'Criciúma',	'Tombense',	'Operário-PR',
#           'Sampaio Corrêa',	'Londrina',	'CRB',	'Novorizontino',	'Brusque',	'Ituano',	'CSA',	'Ponte Preta',
#           'Náutico',	'Chapecoense',	'Guarani',	'Vila Nova')
#
# print(tabela[0:5])
# print(tabela[-4:])
# print(sorted(tabela))
# print(tabela.index('Chapecoense')+1)

#074 - Colocar números aleatórios em uma tupla, mostrar o maior e menor
# from random import randint
# n = ((randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)))
# print(n)
# maior = 0
# menor = 0
# for c in range(0, len(n)):
#     if c == 0:
#         menor = n[c]
#         maior = n[c]
#     elif menor > n[c]:
#         menor = n[c]
#     elif n[c] > maior:
#         maior = n[c]
# print(f'O menor número é o {menor}')
# print(f'O maior número é o {maior}')
# #Em tupla, podemos usar o metedo MAX e MIN
# print(f'O maior valor sorteado foi {max(n)}')
# print(f'O maior valor sorteado foi {min(n)}')

#075 - Ler 4 valores e colocar na tupla
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite um número: '))
# n3 = int(input('Digite um número: '))
# n4 = int(input('Digite um número: '))
# c = 0
# t = (n1, n2, n3, n4)
# cont = t.count(9)
# print(f'Você digitou {t}')
# print(f'O número 9 aparece {cont} vezes')
# if t.count(3) > 0:
#     print(f'O número 3 está na {t.index(3) + 1}° posição')
# else:
#     print(f'O valor 3 não foi digitado')
# print(f'Os valores pares são ', end='')
# if n1 % 2 == 0:
#     print(f'{n1} ', end='')
# if n2 % 2 == 0:
#     print(f'{n2} ', end='')
# if n3 % 2 == 0:
#     print(f'{n3} ', end='')
# if n4 % 2 == 0:
#     print(f'{n4} ', end='')

#076 - Criar tupla com nomes de produtos e preços
# lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
#          'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
# print('=*' * 20)
# print(f'{"Lista de Produtos":^40}')
# print('=*' * 20)

# print(f'{lista[0] :.<30}R${lista[1]:>7.2f}')
# print(f'{lista[2] :.<30}R${lista[3]:>7.2f}')
# print(f'{lista[4] :.<30}R${lista[5]:>7.2f}')
# print(f'{lista[6] :.<30}R${lista[7]:>7.2f}')
# print(f'{lista[8] :.<30}R${lista[9]:>7.2f}')
# print(f'{lista[10] :.<30}R${lista[11]:>7.2f}')
# print(f'{lista[12] :.<30}R${lista[13]:>7.2f}')
# print(f'{lista[14] :.<30}R${lista[15]:>7.2f}')
# print(f'{lista[16] :.<30}R${lista[17]:>7.2f}')

#Outra forma, mais simples
# for pos in range(0, len(lista)):
#     if pos % 2 == 0:
#         print(f'{lista[pos]:.<30}', end='')
#     else:
#         print(f'R${lista[pos]:>7.2f}')

#077 - fazer tupla com varias palavras e mostrar as vogais
# palavras = ('palavra', 'programador', 'desenvolvimento', 'dinheiro', 'vida', 'estudar', 'dedicacao', 'computador',
#             'casa', 'prazer', 'amor')
# for p in palavras:
#     print(f'\nA palavra {p.upper()}, possui as seguinte vogais: ', end='')
#     for i in range(0, len(p)):
#         if p[i] in 'AEIOUaeiou':
#             print(f'{p[i]}', end='')
