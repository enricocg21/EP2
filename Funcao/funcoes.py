# Questão 1:
def define_posicoes(linha,coluna,orientacao,tamanho):
    posicao_inicial = [[linha,coluna]]
    i = 1
    while i < tamanho:
        if orientacao == 'vertical':
            linha += 1
            posicao_inicial.append([linha, coluna])
        elif orientacao == 'horizontal':
            coluna += 1
            posicao_inicial.append([linha, coluna])
        i += 1
    return posicao_inicial
