#Exercício 7
from funcoes import (posicao_valida,preenche_frota,posiciona_frota,faz_jogada,afundados,monta_tabuleiros)
import random

frota = {}

nomes = ['porta-aviões','navio-tanque','contratorpedeiro','submarino']

tamanhos = [4,3,2,1]
quantidades = [1,2,3,4]

for i in range(len(nomes)):
    nome = nomes[i]
    tamanho = tamanhos[i]
    quantidade = quantidades[i]
    posicionados = 0

    while posicionados < quantidade:
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')

        linha = int(input('Linha:'))
        coluna = int(input('Coluna:'))
        if tamanho == 1:
            orientacao = 'vertical'
        else:
            escolha = int(input('[1] Vertical [2] Horizontal >'))

            if escolha == 1:
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'

        if posicao_valida(frota,linha,coluna,orientacao,tamanho):
            frota = preenche_frota(frota,nome,linha,coluna,orientacao,tamanho)
            posicionados += 1
        else:
            print('Esta posição não está válida!')



#Exercicio 8
# Exercício 8
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

total_navios = 0
for nome in frota_oponente:
    total_navios += len(frota_oponente[nome])

jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    jogada_valida = False

    while not jogada_valida:
        linha = int(input('Jogador, qual linha deseja atacar? '))

        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))

        coluna = int(input('Jogador, qual coluna deseja atacar? '))

        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))

        if (tabuleiro_oponente[linha][coluna] == 'X'
                or tabuleiro_oponente[linha][coluna] == '-'):
            print(
                f'A posição linha {linha} e coluna {coluna} '
                'já foi informada anteriormente!'
            )
        else:
            jogada_valida = True

    tabuleiro_oponente = faz_jogada(
        tabuleiro_oponente, linha, coluna
    )

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False



#Exercicio 9
if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

else:
    linha_oponente = random.randint(0, 9)
    coluna_oponente = random.randint(0, 9)

    while (tabuleiro_jogador[linha_oponente][coluna_oponente] == 'X'
            or tabuleiro_jogador[linha_oponente][coluna_oponente] == '-'):
        linha_oponente = random.randint(0, 9)
        coluna_oponente = random.randint(0, 9)

    print(
        f'Seu oponente está atacando na linha {linha_oponente} '
        f'e coluna {coluna_oponente}'
        )

    tabuleiro_jogador = faz_jogada(
        tabuleiro_jogador, linha_oponente, coluna_oponente
        )

    if afundados(frota, tabuleiro_jogador) == total_navios:
        print('Xi! O oponente derrubou toda a sua frota =(')
        jogando = False