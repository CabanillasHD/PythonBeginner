# 057 - Perguntar o sexo e só aceitar F ou M
# s = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
# while s not in 'FM':
#     s = str(input('Dados inválidos. Digite apenas M ou F ').upper().strip()[0])
# if s == 'F':
#     print('Dados recebido com sucesso. Sexo F inserido no banco')
# elif s == 'M':
#     print('Dados recebido com sucesso. Sexo M inserido no banco')

#058 - Jogo de adivinha
# import random
# n = int(input('Adivinhe o número que pensei de 0 a 10: '))
# r = random.randint(0, 10)
# c = 1
# while r != n:
#     c += 1
#     if n < r:
#         n = int(input('Maior, tente novamente: '))
#     else:
#         n = int(input('Menos, tente novamente: '))
# print('Parabéns ! Você acertou em {} tentativas'.format(c))

# 059 - Menu Básico
# from time import sleep
# n1 = int(input('Primeiro número: '))
# n2 = int(input('Segundo número: '))
# opcao = 0
# while opcao != 5:
#     print('=*=' * 5)
#     print('Menu de opções')
#     print('=*=' * 5)
#     print('''1 - somar\n2 - multiplicar\n3 - maior\n4 - trocar números\n5 - sair do programa''')
#     opcao = int(input('Escolha uma das opções acima: '))
#     if opcao == 1:
#         soma = n1 + n2
#         print('A soma é {}'.format(soma))
#     elif opcao == 2:
#         mult = n1 * n2
#         print('A multplicação é igual a {}'.format(mult))
#     elif opcao == 3:
#         if n1 > n2:
#             print('0 maior é {}'.format(n1))
#         else:
#             print('O maior é {}'.format(n2))
#     elif opcao == 4:
#         print('Escolhas os novos números')
#         n1 = int(input('Primeiro número: '))
#         n2 = int(input('Segundo número: '))
#     else:
#         print('Opção incorreta, tente novamente')
# print('Fechando o programa....')
# sleep(2)
# print('------' * 5)
# print('Programa fechado com sucesso')
# print('------' * 5)

# 060 - Fatorial
# n = int(input('Digite um número para saber o fatorial: '))
# c = n
# fat = 1
# while c > 0:
#     print('{} '.format(c), end='')
#     print('x ' if c > 1 else '= ', end='')
#     fat = fat * c
#     c = c - 1
# print('{}'.format(fat))

# 060 usando o FOR
# n = int(input('Informe o número: '))
# n1 = 1
# for f in range(n, 0, -1):
#     fat = n1 * f
#     n1 = fat
#     #print(f)
# print(fat)

# 061 - Refazer o 51 com while
# p = int(input('Digite o primeiro termo: '))
# r = int(input('Digite a razão: '))
# n = 0
# while n < 10:
#     print(p)
#     p = p + r
#     n += 1

#062 - Melhorando o 61
# p = int(input('Digite o primeiro termo: '))
# r = int(input('Digite a razão: '))
# t = p
# cont = 1
# total = 0
# mais = 10
# while mais != 0:
#     total = total + mais
#     while cont <= total:
#         print('{} -> '.format(t), end='')
#         t += r
#         cont += 1
#     print('Pausa')
#     mais = int(input('Quantos termos você quer mostrar a mais? '))
# print('FIM')
# print('Foram mostrados {} termos'.format(total))

#063 - Fibonacci - número seguinte é a soma dos dois anteriores
# n = int(input('Digite quantos termos: '))
# t1 = 0
# t2 = 1
# print('{} -> {}'.format(t1, t2), end='')
# cont = 3
# while cont <= n:
#     t3 = t1 + t2
#     t1 = t2
#     t2 = t3
#     cont = cont + 1
#     print(' -> {}'.format(t3), end='')


#064 - Ler vários números somar e parar quando for 999
# n = int(input('Digite um valor: '))
# s = 0
# c = 0
# while n != 999:
#     s += n
#     c += 1
#     n = int(input('Digite um valor: '))
# print('Acabou e foram {} números e a soma é {}'.format(c, s))

#065 - Ler varios números e dar a media maior e menor
# p = int(input('Digite um valor: '))
# continuar = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
# cont = 1
# menor = maior = total = p
# while continuar in 'S':
#     p = int(input('Digite um valor: '))
#     if menor > p:
#         menor = p
#     elif maior < p:
#         maior = p
#     cont += 1
#     total += p
#     continuar = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
# print('A média dos números é {}'.format(total/cont))
# print('A soma total foi de {}'.format(total))
# print('Foram digitados {} números'.format(cont))
# print('O menor valor foi {}'.format(menor))
# print('O maior valor foi {}'.format(maior))
