# # help(input)
# #
# # print(input.__doc__)
#
#
# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela
#     :param i: Início da contagem
#     :param f: Fim da contagem
#     :param p: Passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM')
#
#
# contador(2, 10, 2)
#
# help(contador)

# def somar(a, b, c=0):
#     """
#     Somar 3 valores
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
#
# somar(3, 2)

# Escopo de variáveis
# def teste():
#     x = 8
#     print(f'Na função n vale {n}')
#     print(f'Na função x vale {x}')
#
#
# n = 2
# print(f'No programa principal n vale {n}')
# teste()
# #print(f'No program principal x vale {x} ') #variável local não pode usada fora da função

# def teste(b):
#     global a
#     a = 8
#     b += 4
#     c = 2
#     print(a)
#     print(b)
#     print(c)
#
#
# a = 5
# teste(a)
# print(a)

# def soma(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
#
# r1 = soma(3, 2, 5)
# r2 = soma(2, 2)
# r3 = soma(5)
# print(f'As contas deram {r1}, {r2}, {r3}')

#Pratica
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
#
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é {fatorial(n)}')

def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um valor: '))
if par(n):
    print('É par')
else:
    print('Não é par')

