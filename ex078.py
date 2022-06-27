#078 - Criar lista e mostrar maior e menor
lista = list()
menor = maior = posma = posme = 0
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = lista[c]
    elif lista[c] < menor:
        menor = lista[c]
        posme = c
    elif lista[c] > maior:
        maior = lista[c]
        posma = c
print(f'Olha que dmais essa é a sua lista {lista}')
print(f'O maior da lista é {maior} e está na posição {posma + 1}')
print(f'O menor da lista é {menor} e está na posição {posme + 1}')

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
# for v in range(0, 2):
#     if v == 0:
#         lista.append(int(input('Digite um valor:')))
#     if v == 1:
#         if v[1] > v[0]:
#             lista.append(int(input('Digite um valor:')))
#         else:
#             lista.insert(int(input('Digite um valor:'), 0))
#     print(v[0])
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
#     if n % 2 == 0:
#         listapar.append(n)
#     else:
#         listaimpar.append(n)
# print(f'Essa é a lista de números pares {listapar}')
# print(f'Essa é a lista de números ímpares {listaimpar}')

#083 - Analise de expressao com parenteses
# frase = []
# frase.extend(str(input('Digite a expressão: ')))
# if (frase.count('(')) == (frase.count(')')):
#     print('expressão correta')
# else:
#     print('expressão errada')
