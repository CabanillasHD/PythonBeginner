#078 - Criar lista e mostrar maior e menor
# lista = list()
# menor = maior = posma = posme = 0
# for c in range(0, 5):
#     lista.append(int(input('Digite um valor: ')))
#     if c == 0:
#         maior = menor = lista[c]
#     elif lista[c] < menor:
#         menor = lista[c]
#         posme = c
#     elif lista[c] > maior:
#         maior = lista[c]
#         posma = c
# print(f'Olha que dmais essa é a sua lista {lista}')
# print(f'O maior da lista é {maior} e está na posição {posma + 1}')
# for i, v in enumerate(lista):
#     if v == maior:
#         print(f'O valor maior apareceu nas posições {i + 1}')
# print(f'O menor da lista é {menor} e está na posição {posme + 1}')
# for i, v in enumerate(lista):
#     if v == menor:
#         print(f'O valor menor apareceu nas posições {i + 1}')

#079 - Digitar vários números - só aceitar números novos e mostrar em ordem crescente
# lista = list()
# while True:
#     n = int(input('Digite um valor: '))
#     if n not in lista:
#         lista.append(n)
#     else:
#         print('Valor duplicado')
#     continuar = str(input('Quer continuar? [S/N]')).upper().split()[0]
#     if continuar in 'nN':
#         break
# lista.sort()
# print(lista)

#080 - Digitar 5 valores e ordenar sem usar o sort()
# lista = []
# for c in range(0, 5):
#     n = int(input('Digite um valor: '))
#     if c == 0 or n > lista[-1]:
#         lista.append(n)
#         print('Valor inserido no final da lista')
#     else:
#         pos = 0
#         while pos < len(lista):
#             if n <= lista[pos]:
#                 lista.insert(pos, n)
#                 print(f'Valor inserido na posição {pos} da lista')
#                 break
#             pos += 1
# print(lista)


#081 - Receber varios valores em uma lista e falar qnt digitados, ordenar desc e mostra se tem 5
# lista = list()
# cont = 0
# while True:
#     lista.append(int(input('Digite uma valor: ')))
#     cont += 1
#     continuar = str(input('Quer continuar [S/N] ')).split()[0]
#     if continuar in 'Nn':
#         break
# lista.sort(reverse=True)
# print(f'Foram digitados {cont} números')
# print(lista)
# if lista.count(5) > 0:
#     print(f'O valor 5 foi digitado e está na posição {lista.index(5) + 1}')
# else:
#     print('O valor 5 não foi digitado')

#082 - Criar uma lista e depois separar em uma lista par e outra ímpar
# lista = list()
# listapar = list()
# listaimpar = list()
# while True:
#     lista.append(int(input('Digite uma valor: ')))
#     continuar = str(input('Quer continuar [S/N] ')).split()[0]
#     if continuar in 'Nn':
#         break
# print(f'Sua lista completa é {lista}')
# for n in lista:
#     print(n)
#     if n % 2 == 0:
#         listapar.append(n)
#     else:
#         listaimpar.append(n)
# print(f'Essa é a lista de números pares {listapar}')
# print(f'Essa é a lista de números ímpares {listaimpar}')

#083 - Analise de expressao com parenteses - VERIFICAR
# frase = (str(input('Digite a expressão: ')))
# parabre = []
# for v in frase:
#     if v == '(':
#         parabre.append('(')
#     if v == ')':
#         if len(parabre) > 0:
#             parabre.pop()
#         else:
#             parabre.append(')')
#             break
# if len(parabre) == 0:
#     print('Expressão correta')
# else:
#     print('Expressão incorreta')
