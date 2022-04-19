n1 = int((input('Digite o primeiro número: ')))
n2 = int((input('Digite o segundo número: ')))
s = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
pot = n1 ** n2
di = n1 // n2
res = n1 % n2
print('A soma dos números {} e {} é igual a \n {}'.format(n1, n2, s), end='¨¨¨¨¨¨¨')
print('A subtração dos números {} e {} é igual a {}'.format(n1, n2, sub))
print('A multiplicação dos números {} e {} é igual a {}'.format(n1, n2, mul))
print('A divisão dos números {} e {} é igual a {:.3f}'.format(n1, n2, div))
print('A potência dos números {} e {} é igual a {}'.format(n1, n2, pot))
print('A divisao inteira dos números {} e {} é igual a {}'.format(n1, n2, di))
print('O resto da divisão dos números {} e {} é igual a {}'.format(n1, n2, res))

