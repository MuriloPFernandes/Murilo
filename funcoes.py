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


#Exercício 4
def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for nome in frota:
        for navio in frota[nome]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro



#Exercício 5
def afundados(frota,tabuleiro):
    quantidade = 0
    for nome in frota:
        for navio in frota[nome]:
            acertos = 0
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] == 'X':
                    acertos += 1

            if acertos ==len(navio):
                quantidade += 1

    return quantidade



#Exercício 6 
def posicao_valida(frota,linha,coluna,orientacao,tamanho):
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    for posicao in posicoes:
        lin = posicao[0]
        col = posicao[1]
        if lin < 0 or lin >= 10 or col < 0 or col >= 10:
            return False

        for nome in frota:
            for navio in frota[nome]:
                if posicao in navio:
                    return False

    return True








def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join(
            [str(item) for item in tabuleiro_jogador[linha]]
        )
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0'
             for info in tabuleiro_oponente[linha]]
        )
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'

    return texto


