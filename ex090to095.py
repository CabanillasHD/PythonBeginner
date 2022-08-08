#090 - Ler nome e media de aluno e situacao 7 ou mais aprovado.
# boletim = dict()
# boletim['Nome'] = str(input('Nome aluno: '))
# boletim['Media'] = float(input(f'Media de {boletim["Nome"]}: '))
# if boletim['Media'] >= 7.0:
#     boletim['Situacao'] = 'Aprovado'
# else:
#     boletim['Situacao'] = 'Reprovado'
# for k, v in boletim.items():
#     print(f'- {k} é igual a {v}')

#091 - 4 jogadores vao jogar um dado, guardar em um dicionario, colocar em ordem
# from operator import itemgetter
# from random import randint
# from time import sleep
# jogadas = dict()
# for c in range(0, 4):
#     jogadas[f'Jogador {c + 1}'] = int(randint(1, 7))
# jogadasord = sorted(jogadas.items(), key=operator.itemgetter(1), reverse=True)
# for k, v in jogadas.items():
#     print(f'O {k} jogou {v}')
#     sleep(1)
# print('=+' * 25)
# print(f'{"Classificação":^50}')
# print('=+' * 25)
# for i, v in enumerate(jogadasord):
#     print(f'{i + 1}° Lugar --> {v[0]} jogou {v[1]}')
#     sleep(1)


#092 - Cadastrar nome, ano de nascimento (idade), carteira de trabalho. Quando aposenta, 35 anos
# from datetime import date
# anoatual = date.today().year
# trabalhador = {}
# nome = str(input('Nome: '))
# ano = int(input('Ano de nascimento: '))
# carteira = int(input('Carteira de trabalho [0 não tem]: '))
# trabalhador['nome'] = nome
# trabalhador['idade'] = anoatual - ano
# trabalhador['carteira'] = carteira
# if carteira > 0:
#     pvaga = int(input('Ano 1° vaga: '))
#     sal = float(input('Salário: '))
#     tempotra = 35 - (anoatual - pvaga)
#     dataap = trabalhador['idade'] + tempotra
#     trabalhador['vaga'] = pvaga
#     trabalhador['salario'] = sal
#     trabalhador['aposentar'] = dataap
# print('=-' * 10)
# for k, v in trabalhador.items():
#     print(f'{k} tem o valor {v}')

#093 - Programa que analisa aproveitamento de um jogador de futebol
# hist = {}
# hist['nome'] = str(input('Nome jogador: '))
# partidas = int(input(f'Quantas partidas {hist["nome"]} jogou? '))
# qtdgols = []
# for p in range(0, partidas):
#     gol = int(input(f'Quantos gols na {p + 1}° partida : '))
#     qtdgols.append(gol)
# hist['gols'] = qtdgols
# hist['total'] = sum(qtdgols)
# print('=-' * 30)
# print(hist)
# print('=-' * 30)
# for k, v in hist.items():
#     print(f'O campo {k} tem o valor {v}')
# print('=-' * 30)
# print(f'O jogador {hist["nome"]} jogou {len(qtdgols)} partidas')
# for j, g in enumerate(hist["gols"]):
#     print(f'=> Na partida {j + 1}, fez {g} gols')
# print(f'Foi um total de {hist["total"]} gols')

#094 - Guardar nome sexo idade em dict e os dicts em uma lista
# grupo = []
# pessoa = {}
# while True:
#     pessoa['nome'] = str(input('Nome: '))
#     pessoa['idade'] = int(input('Idade: '))
#     while True:
#         pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().split()[0]
#         if pessoa['sexo'] in 'FM':
#             break
#         print('ERRO. Digite apenas M ou F')
#     grupo.append(pessoa.copy())
#     pessoa.clear()
#     while True:
#         continuar = str(input('Deseja continuar[S/N]? ')).upper().split()[0]
#         if continuar in 'NS':
#             break
#         print('ERRO. Digite apenas S ou N')
#     if continuar == 'N':
#         break
# print(f'A) Foram cadastradas {len(grupo)} pessoas')
# somaidade = media = 0
#
# for i, p in enumerate(grupo):
#     somaidade += p["idade"]
# media = somaidade / (i+1)
# print(f'B) A media de idade do grupo é de {media:.0f} anos')
# print('C) Mulheres do grupo: ', end='')
# for p in grupo:
#     if p['sexo'] == 'F':
#         print(f'{p["nome"]} ', end='')
# print()
# print('D) Pessoas com idade acima da média: ', end='')
# for p in grupo:
#     if p['idade'] > media:
#         print(f'{p["nome"]} ', end='')

#095 - Aprimorar o 93, para funcionar com vários jogadores
# jogadores = []
# hist = {}
# while True:
#     hist.clear()
#     hist['nome'] = str(input('Nome jogador: '))
#     partidas = int(input(f'Quantas partidas {hist["nome"]} jogou? '))
#     qtdgols = []
#     for p in range(0, partidas):
#         gol = int(input(f'Quantos gols na {p + 1}° partida : '))
#         qtdgols.append(gol)
#     hist['gols'] = qtdgols
#     hist['total'] = sum(qtdgols)
#     jogadores.append(hist.copy())
#     while True:
#         continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
#         if continuar in 'SN':
#             break
#         print('ERRO. Digite S ou N')
#     if continuar == 'N':
#         break
# print('=-' * 30)
# print(jogadores)
# print('=-' * 30)
# print(f'{"cod"} ', end='')
# for k in hist.keys():
#     print(f'{k:<15}', end='')
# print()
# for k, v in enumerate(jogadores):
#     print(f'{k:>3} ', end='')
#     for d in v.values():
#         print(f'{str(d):<15}', end='')
#     print()
# print('=-' * 30)
# while True:
#     opcao = int(input('Qual jogador quer detalhar? [999 para]: '))
#     if opcao == 999:
#         break
#     if opcao >= len(jogadores):
#         print(f'ERRO, não existe jogador de número {opcao}')
#     else:
#         print(f'Levantamento do Jogador {jogadores[opcao]["nome"]}')
#         for i, v in enumerate(jogadores[opcao]["gols"]):
#             print(f'Na partida {i+1} fez {v} gols')
#         print('=-' * 30)
# print('=-' * 30)
# print('=-= Programa Encerrado =-=')
