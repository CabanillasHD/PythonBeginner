# 028 - Jogo de adivinha
#from random import randint
#from time import sleep
#np = int(input('Pensei em número entre 0 e 5, dúvido você acertar... fala um número ai: '))
#nm = randint(0, 5)
#print('Processando...')
#sleep(2)
#if np == nm:
#    print('O número que eu pensei foi {}. Parabéns você acertou !'.format(nm))
#else:
#    print('O número que eu pensei foi {} e não {}. Você erroooou !!'.format(nm, np))

# 029 - Radar de velocidade
#v = int(input('Digite a velocidade do carro: '))
#e = v - 80
#if v > 80:
#    print('Você ultrapassou a velocidade permitida, MULTADO !')
#    print('Você terá que pagar R${:.2f} de multa'.format(e * 7.00))
#print('Tenha um bom dia !')

# 030 - Ler número e falar se é par o ímpar
#n = float(input('Digite um número, para sabermos se é \033[36mPAR\033[m ou \033[31mÍMPAR\033[m: '))
#if n % 2 == 0:
#    print('O número é \033[36mpar\033[m')
#else:
#    print('O número é \033[31mímpar\033[m')

# 031 - Preço da passagem
#km = int(input('Digite a km: '))
#if km <= 200:
#    print('Você percorreu {}km. A sua passagem será de R${:.2f}'.format(km, (km * 0.50)))
#else:
#    print("Você percorreu {}km. A sua passagem será de R${:.2f}".format(km, (km * 0.45)))

# 032 - Ler ano bissexto
#from datetime import date
#a = int(input('Digite um ano para saber se ele é bissexto: '))
#if a == 0:
#    a = date.today().year
#if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
#   print('O ano {} é bissexto !'.format(a))
#else:
#    print('O ano {} não é bissexto !'.format(a))

# Ler 3 números falar o maior e o menor
#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite um valor: '))
#n3 = int(input('Digite um valor: '))
#if n1 > n2 and n1 > n3:
#    print('O maior número é o {}'.format(n1))
#else:
#    if n2 > n1 and n2 > n3:
#        print('O maior valor é {}'.format(n2))
#    else:
#       print('O maior valor é {}'.format(n3))
#if n1 < n2 and n1 < n3:
#    print('O menor número é o {}'.format(n1))
#else:
#    if n2 < n1 and n2 < n3:
#       print('O menor valor é {}'.format(n2))
#    else:
#        print('O menor valor é {}'.format(n3))

# 034 - Aumento no salário
#s = float(input('Digite seu salário:'))
#if s > 1250:
#    print('Seu aumento será de 10% e seu salário será de {:.2f}'.format(s*1.1))
#else:
#    print('Seu aumento será de 15% e seu salário será de {:.2f}'.format(s*1.15))

# 035 - Retas formam triângulo
#print('-=-' * 10)
#print('Analisador de Triângulo')
#print('-=-' * 10)
#l1 = float(input('Digite um valor para o lado do triângulo:'))
#l2 = float(input('Digite um valor para o lado do triângulo:'))
#l3 = float(input('Digite um valor para o lado do triângulo:'))
#c1 = (l2 - l3) < l1 < (l2 + l3)
#c2 = (l1 - l3) < l2 < (l1 + l3)
#c3 = (l2 - l1) < l3 < (l2 + l1)
#if c1 and c2 and c3:
#   print('Os lados FORMAM um triângulo')
#else:
 #   print('Os lados NÃO formam um triângulo')



