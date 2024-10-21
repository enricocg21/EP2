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

# Questão 2:

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista = []
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    lista.append(posicao)
    if nome_navio in frota.keys():
        frota[nome_navio] += lista
    else:
        frota[nome_navio] = lista
    return frota

# Questão 3:

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

# Questão 4:

def posiciona_frota(frota):
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
    for posicao in frota.values():
        for posicao in posicao:
            for linha, coluna in posicao:
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro