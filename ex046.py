# 046 - Contagem regressiva
#from time import sleep
#print('=*' * 10)
#print('Contagem Regressiva')
#print('=*' * 10)
#for c in range(10, 0, -1):
#    print(c)
#    sleep(1)
#print('=*' * 10)
#print('{:^20}'.format('\33[35;3mFeliz Ano Novo\33[m'))
#print('=*' * 10)


# 047 - Números pares de 1 a 50
#n = int(input('Digite um número e descubra os pares entre 0 e o número:'))
#for c in range(2, n+1, 2):
#    print(c, end=' ')

# 048 -Somar números impar e multiplos de 3 entre 1 e 500
#s = 0
#for c in range(1, 501, 2):
#    if c % 3 == 0:
#        s += c
#print('A soma dos números entre 1 e 500, ímpares e múltiplos de 3 é {}'.format(s))

# 049 - Fazer a tabuada usando o laço for
#t = 0
#n = int(input('Digite o número:'))
#for c in range(1, 10):
#    t = n * c
#    print('{} * {} = {}'.format(n, c, t))

# 050 - Digitar 6 número e somar os pares
#s = 0
#for c in range(0, 6):
#    n = int(input('Digite um número: '))
#   if n % 2 == 0:
#        s += n
#print(s)

# 051 - PA mostrar os 10 primeiros
#p = int(input('Digite o primeiro termo: '))
#r = int(input('Digite a razão: '))
#for c in range(p, 10 * r + p, r):
#    print(c)

# 052 - Ler um número e saber se é primo
#count = 0
#n = int(input('Digite um número: '))
#for c in range(1, n+1):
#    if n % c == 0:
#        count = count + 1
#if count == 2:
#    print('O número é PRIMO')
#else:
#    print('O número NÃO é primo')

# 053 - Ler uma frase e dizer se é palindromo
#frase = str(input('Digite uma frase: ').strip().upper())
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#inverso = junto[::-1] # outra forma de pegar a frase ao contrário
#for letra in range(len(junto)-1, -1, -1):
#    inverso = inverso + junto[letra]
#if inverso == junto:
#    print('A frase {} é um palíndromo, pois seu inverso é {} é o mesmo que {}'. format(frase, inverso, junto))
#else:
#    print('Não é um palíndromo')


# 054 - Ler data de nascimento e falar se é de maior
#from datetime import date
#data_atual = date.today().year
#cme = 0
#cma = 0
#for c in range(1, 8):
#    idade = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(c)))
#    if data_atual - idade < 21:
#        cme += 1
#    else:
#        cma += 1
#print('Nesta lista temos {} menor de idade e {} maiores de idade'.format(cme, cma))


# 055 - Ler pesos qual o maior e o menor
#p = 0
#pm = 0
##pm = 100000000000000
#for c in range(1, 6):
#    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
#    if c == 1:
#        p = peso
#        pm = peso
#    else:
#        if peso > p:
#            p = peso
#        elif peso < pm:
#            pm = peso
#print('O maior peso é {:.2f}Kg e o menor é {:.2f}Kg'.format(p, pm))

# 056 - Programa que leia informações de 4 pessoas e retorna algumas informações
#i = 0
#idadeinicial = 0
#countmul = 0
#for c in range(1, 5):
#    nome = str(input('Digite seu nome: '))
#    idade = int(input('Digite sua idade: '))
#    sexo = str(input('Qual o seu sexo (M ou F): ').upper())
#    i += idade
#    if idade > idadeinicial and sexo == 'M':
#        idadeinicial = idade
#        nomevelho = nome
#    elif sexo == 'F':
#        if idade < 20:
#            countmul = countmul + 1
#print('A média da idade deste grupo é de {} anos'.format(i/4))
#print('O nome do homem mais velho é {} e ele tem {} anos'.format(nomevelho, idadeinicial))
#print('O número de mulheres com menos de 20 anos é {}'.format(countmul))
