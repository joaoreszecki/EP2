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