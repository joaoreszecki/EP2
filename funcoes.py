# Questão 1:
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao = []
    for i in range(tamanho):
        if orientacao == "vertical":
            posicao.append([linha, coluna])
            linha += 1
        elif orientacao == "horizontal":
            posicao.append([linha, coluna])
            coluna += 1
    return posicao

# Questão 2:
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicao)
    else:
        frota[nome_navio] = [posicao]
    return frota

# Questão 3:
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

#Questão 4:
def posiciona_frota(posicoes):
    tabuleiro = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    for navio in posicoes:
        for posicao in posicoes[navio]:
            for linha, coluna in posicao:
                tabuleiro[linha][coluna] = 1
    return tabuleiro