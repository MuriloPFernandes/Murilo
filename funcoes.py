# Exercício 1
def define_posicoes(linha,coluna,orientacao,tamanho):
    lista1 = []
    i = 0
    while i < tamanho:
        if orientacao == 'vertical':
            linhas = linha + i
            colunas = coluna
        if orientacao == 'horizontal':
            linhas = linha
            colunas = coluna + i
        lista1.append([linhas,colunas])
        
        i += 1
    return lista1


# Exercício 2
def preenche_frota(frota,nome,linha,coluna,orientacao,tamanho):
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)

    if nome not in frota:
        frota[nome] = []

    frota[nome].append(posicoes)
    return frota


# Exercício 3
def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro