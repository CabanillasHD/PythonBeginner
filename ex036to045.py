# 036 - Calcula a prestação e se ela é 30% do salário
# vlcasa = float(input('Digite o valor da casa R$: '))
# vlsal = float(input('Digite o valor do salário R$: '))
# pres = int(input('Quantos anos de prestação: '))
# vlpres = (vlcasa / pres) / 12
# salideal = (vlpres * 100) / 30
# print("O valor das prestações será de R${:.2f}".format(vlpres))
# if vlpres <= (vlsal * 30)/100:
#     print('Parabéns, empréstimo APROVADO !')
# else:
#     print('Empréstimo NEGADO !\nSeu salário precisaria ser de no mínimo {:.2f} para comprar esta casa'.format(salideal))



# 037 - Transformar número em bases númericas
# n = int(input('Digite um número inteiro: '))
# base = int(input('Qual base? \n1 - binário \n2 - octal \n3 - hexadecimal \n='))
# if base == 1:
#   print('{} em binario é {}'.format(n, bin(n)[2:]))
# elif base == 2:
#    print('{} na base octal é {}'.format(n, oct(n)[2:]))
# elif base == 3:
#    print('{} na base hexadecimal é {}'.format(n, hex(n)[2:]))
# else:
#    print('Escolha uma das opções acima')

# 038 - Comparar valores
# v1 = int(input('Digite o primeiro valor: '))
# v2 = int(input('Digite o segundo valor: '))
# if v1 > v2:
#    print('O PRIMEIRO valor é o MAIOR')
# elif v1 == v2:
#   print('Os valores são IGUAIS')
# else:
#    print('O SEGUNDO valor é o MAIOR')

# 039 - Hora de se alistar
# from datetime import date
# sexo = str(input('Qual o seu sexo? F ou M ? '))
# if sexo == 'f':
#    print('Você não precisa se alistar')
# elif sexo == 'm':
#    nasc = int(input('Digite o ano do nascimento: '))
#    ano_atual = date.today().year
#    alis = ano_atual - nasc
#    if alis == 18:
#        print('Você deve se alistar!')
#    elif alis > 18:
#        print('Você NÃO precisa mais se alistar, já se passaram {} anos do seu período!'.format(alis - 18))
#    else:
#        print('Ainda não é tempo para você se alistar. Você deverá se apresentar daqui {} anos'.format(18 - alis))


# 040 - Ler notas aluno
# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# media = (n1 + n2) / 2
# print('{:.1f}'.format(media))
# if media < 5.0:
#    print('REPROVADO')
# elif 5.0 <= media <= 6.9:
#    print('RECUPERAÇÃO')
# else:
#    print('APROVADO')


# 041 - Categoria
# from datetime import date
# idade = int(input('Qual o ano do seu nascimento? '))
# ano_atual = date.today().year
# cat = ano_atual - idade
# if cat <= 9:
#    print('MIRIM')
# elif cat > 9 and cat <= 14:
#    print('INFANTIL')
# elif cat > 14 and cat <= 19:
#    print('JUNIOR')
# elif cat > 19 and cat <= 20:
#   print('SÊNIOR')
# else:
#    print('MASTER')

# 042 - Tipos de triângulo
# print('-=-' * 10)
# print('Analisador de Triângulo')
# print('-=-' * 10)
# l1 = float(input('Digite um valor para o lado do triângulo:'))
# l2 = float(input('Digite um valor para o lado do triângulo:'))
# l3 = float(input('Digite um valor para o lado do triângulo:'))
# c1 = (l2 - l3) < l1 < (l2 + l3)
# c2 = (l1 - l3) < l2 < (l1 + l3)
# c3 = (l2 - l1) < l3 < (l2 + l1)
# if c1 and c2 and c3:
#    print('Os lados FORMAM um triângulo ', end='')
#    if (l1 == l2 and l1 != l3) or (l2 == l3 and l2 != l1) or (l3 == l1 and l3 != l2):
#        print('ISÓSCELES')
#    elif (l2 == l1) and (l1 == l3):  # r1 == r2 == r3
#        print('EQUILÁTERO')
#    elif (l1 != l2) and (l1 != l3) and (l2 != l3):
#        print('ESCALENO')
# else:
#    print('Os lados NÃO formam um triângulo')

# 043 - IMC
# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))
# imc = peso / (altura ** 2)
# print('Seu IMC é {:.2f} e você está no status '.format(imc), end='')
# if imc < 18.5:
#    print('Abaixo do Peso')
# elif 18.5 <= imc < 25:
#    print('Peso Ideal')
# elif 25 <= imc < 30:
#    print('Sobrepeso')
# elif 30 <= imc < 40:
#    print('Obesidade')
# else:
#    print('Obesidade Morbida')

# 044 - Gerenciador de Pagamentos
#prodval = float(input('Qual o valor do produto? R$ '))
#print('1 - à vista dinheiro/cheque'  '\n2 - à vista no cartão' '\n3 - Em até 2X no cartão' '\n4 - 3X ou mais no cartão')
#cond_pag = int(input('Escolha uma das formas de pagamento acima: '))
#if cond_pag == 1:
#    valorf = prodval - ((prodval * 10) / 100)
#    print('A forma de pagamento selecionada foi \033[1;34mà vista dinheiro/cheque\033[m e o valor final será de '
#          'R${:.2f}'.format(valorf))
#elif cond_pag == 2:
#    valorf = prodval - ((prodval * 5) / 100)
#    print('A forma de pagamento selecionada foi \033[1;34mà vista no cartão\033[m e o valor final será de '
#          'R${:.2f}'.format(valorf))
#elif cond_pag == 3:
#    print('A forma de pagamento selecionada foi \033[1;34mem até 2X no cartão\033[m e o valor final será de '
#          'R${:.2f}'.format(prodval))
#elif cond_pag == 4:
#    valorf = prodval + ((prodval * 20) / 100)
#   print('A forma de pagamento selecionada foi \033[1;34m3X ou mais no cartão\033[m e o valor final será de '
#         'R${:.2f}'.format(valorf))
#else:
#    print('Escolha uma das \033[1;32;44mopções\033[m acima')

# 045 - Jokenpô
#from random import randint
#import time
#itens = ('Pedra', 'Papel', 'Tesoura')
#escolha = int(input('''[0] - Pedra
#[1] - Papel
#[2] - Tesoura
#Escolha:'''))
#maqescolha = randint(0, 2)
#print('Voce escolheu {} e máquina {}'.format(itens[escolha], itens[maqescolha]))
#print('então...')
#time.sleep(3)
#if escolha == maqescolha:
#    print('Iiih Deu Empate')
#elif escolha == 0 and maqescolha == 1:
#    print('A máquina venceu')
#elif escolha == 0 and maqescolha == 2:
#    print('Você venceu')
#elif escolha == 1 and maqescolha == 0:
#    print('Você venceu')
#elif escolha == 1 and maqescolha == 2:
#    print('A máquina venceu')
#elif escolha == 2 and maqescolha == 1:
#    print('Você venceu')
#elif escolha == 2 and maqescolha == 0:
#    print('A máquina venceu')
