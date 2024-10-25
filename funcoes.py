# Questão 1:
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicao=[]
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
