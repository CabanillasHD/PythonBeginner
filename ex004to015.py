#05Antecessor e Sucessor
#n = int(input('Digite um número: '))
#print(f'O antecessor é {n-1} e o sucessor é {n+1}')

#06Dobro, Triplo e Raiz
#n1 = int(input('Digite um número: '))
#print('O dobro do número é {}, o triplo é {} e raiz quadrada é {:.2f}'.format((n1*2), (n1*3), (n1**(1/2))))

#07Media Nota
#n1 = float(input('Digite sua primeira nota: '))
#n2 = float(input('Digite sua segunda nota: '))
#m = ((n1 + n2) / 2)
#print('A média de sua nota é {:.2f}!'.format(m))

#08ConvertorM/CM/MM
#m = float(input('Digite um valor em metros: '))
#cm = (m * 100)
#mm = (m * 1000)
#print('{} equivale a {}cm e {}mm'.format(m, cm, mm))

#09Tabuada
#n = int(input('Digite um número para saber sua tabuada: '))
#print('-' * 10)
#print('{} x 1 = {}'.format(n, (n*1)))
#print('{} x 2 = {}'.format(n, (n*2)))
#print('{} x 3 = {}'.format(n, (n*3)))
#print('{} x 4 = {}'.format(n, (n*4)))
#print('{} x 5 = {}'.format(n, (n*5)))
#print('{} x 6 = {}'.format(n, (n*6)))
#print('{} x 7 = {}'.format(n, (n*7)))
#print('{} x 8 = {}'.format(n, (n*8)))
#print('{} x 9 = {}'.format(n, (n*9)))
# #print('_' * 10)

#10CambioMoeda
#d = float(input('Digite quanto você tem em Doláres: '))
#print('Você tem {} reais'.format(d*3.27))

#11PintaraCasa
#h = float(input('Qual a altura da parade? '))
#l = float(input('Qual a largura da parade? '))
#a = h * l
#bt = a / 2
#print('A área da parade é de {} m'.format(a))
#print('Você irá utilizar {:.4f} l de tinta'.format(bt))

#12Desconto
#p = float(input('Digite o preço do produto: '))
#d = float(input('Digite o desconto do produto: '))
#pf = p - ((p * d) / 100)
#pf = p * (1-d/100)
#print('O produto sai a R${:.2f} com o desconto de {:.2f}%'.format(pf, d))

#13AumentodeSalário
#s = float(input('Digite o salário: '))
#p = float(input('Qual a porcentagem de aumento? '))
#sn = (s * (1+p/100))
#print('O salário atual é {}'.format(s))
#print('O novo salário será de {:.2f}'.format(sn))

#14ConversãodeTemp
#t = float(input('Digite a temperatura em ºC: '))
#f = (t * 9/5) + 32
#print('A temperatura em Fahrenheit é {}ºF'.format(f))

#15AlugueldeCarro
#km = float(input('Quantos KM foram percorridos? '))
#d = int(input('Por quantos dias ele foi alugado? '))
#p = (60 * d) + (0.15 * km)
#print('O carro custou R${:.2f}'.format(p))