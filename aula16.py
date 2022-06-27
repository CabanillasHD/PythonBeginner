num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(5, 2)
num.remove(2)
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')

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
