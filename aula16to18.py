# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort()
# num.sort(reverse=True)
# num.insert(5, 2)
# num.remove(2)
# #num.pop(2)
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# valores = list()
#
# # valores.append(5)
# # valores.append(9)
# # valores.append(4)
# for cont in range(0, 4):
#     valores.append(int(input('Digite um valor: ')))
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}')
# print('FIM')

#
# lista = [2, 5, 9, 4]
# for i, v in enumerate(lista):
#     print(i, v)

##Lista dentro de listas
# dados = list()
# pessoas = list()
# dados.append('pedro')
# dados.append(25)
# print(dados[0:2])
# pessoas.append(dados[:])
# print(pessoas)

# teste = list()
# teste.append('Henrique')
# teste.append(27)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Marcos'
# teste[1] = 21
# galera.append(teste[:])
# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquin', 13], ['Maria', 45]]
# # print(galera[3][0])
# for p in galera:
#     print(p[0])

#
# galera = list()
# dados = list()
# totmai = totme = 0
# for c in range(0, 3):
#     dados.append(str(input('Nome: ')))
#     dados.append(int(input('Idade: ')))
#     galera.append(dados[:])
#     dados.clear()
# for p in galera:
#     if p[1] >= 18:
#         print(f'O {p[0]} é maior')
#         totmai += 1
#     else:
#         print(f'O {p[0]} é menor')
#         totme += 1
# print(f'Temos {totmai} maiores e {totme} menores de idade')
# print(galera)


