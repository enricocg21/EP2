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

# Questão 5:

def afundados(dicio, tabuleiro):
    resp = 0
    for chave,valor in dicio.items():
        for navio in valor:
            i = 0
            for coordenadas in navio:
                if tabuleiro[coordenadas[0]][coordenadas[1]] == 'X':
                    i += 1
            if i == len(navio):
                resp += 1
    return resp

# Questão 6:

def posicao_valida(dicio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    for nome,infos in dicio.items():
        for um_navio in infos:
            for coordenadas in um_navio:
                for posicao in posicoes:
                    if posicao == coordenadas:
                        return False
                    for eixo in posicao:
                        if eixo > 9:
                            return False
    for posicao in posicoes:
        for eixo in posicao:
            if eixo > 9:
                return False
    else:
        return True
    
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto