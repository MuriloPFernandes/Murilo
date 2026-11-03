#Exercício 7
from funcoes import posicao_valida,preenche_frota

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
        print(f'Insira as informações referentes ao navio {nome}'f'que possui tamanho {tamanho}')

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

print(frota)