# 084 - colocar varias nomes nas lista, informar mais pesada e mais leve
# lista = list()
# grupo = list()
# pleve = list()
# ppesada = list()
# while True:
#     lista.append(str(input('Nome: ')))
#     lista.append(int(input('Peso: ')))
#     grupo.append(lista[:])
#     lista.clear()
#     contiuar = str(input('Continuar? [S/N]')).split()[0]
#     if contiuar in 'Nn':
#         break
# for v in grupo:
#     if v[1] >= 100:
#         ppesada.append(v[0])
#     elif v[1] <= 70:
#         pleve.append(v[0])
# print(f'Foram digitados {len(grupo)} valores')
# print(f'As pessoas mais pesadas são {ppesada}')
# print(f'As pessoas mais leves são {pleve}')

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
linha1 = list()
linha2 = list()
linha3 = list()
for c in range(0, 9):
    n = int(input('Digite um valor: '))
print(c)
