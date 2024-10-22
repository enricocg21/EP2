#Questão 7:

from funcoes import posicao_valida
from funcoes import define_posicoes
from funcoes import preenche_frota

i = 0
frota = {}
while i < 10:
    if i == 0:
        nome = 'porta-aviões'
        tamanho = 4
    elif i > 0 and i < 3:
        nome = 'navio-tanque'
        tamanho = 3
    elif i > 2 and i < 6:
        nome = 'contratorpedeiro'
        tamanho = 2
    elif i > 5:
        nome = 'submarino'
        tamanho = 1
    
    print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if i < 6:
        perg_ori = int(input('[1] Vertical [2] Horizontal >'))
        if perg_ori == 1:
            orientacao = 'vertical'
        else:
            orientacao = 'horizontal'

    chama = posicao_valida(frota, linha, coluna, orientacao, tamanho)
    while chama == False:
        print('Esta posição não está válida!')
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if i < 6:
            perg_ori = int(input('[1] Vertical [2] Horizontal >'))
            if perg_ori == 1:
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'
        chama = posicao_valida(frota, linha, coluna, orientacao, tamanho)

    define_posicoes(linha,coluna,orientacao,tamanho)
    preenche_frota(frota,nome,linha,coluna,orientacao,tamanho)

    i += 1

print(frota)