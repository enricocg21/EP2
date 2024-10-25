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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

from funcoes import posiciona_frota
from funcoes import monta_tabuleiros
from funcoes import faz_jogada
from funcoes import afundados

posicao_oponente = posiciona_frota(frota_oponente)

posicao_jogador = posiciona_frota(frota)

jogando = True

lista_coordenadas = []

while jogando == True:

    tabuleiros = monta_tabuleiros(posicao_jogador, posicao_oponente)
    

    print(tabuleiros)

    resposta = False
    while resposta == False:
        linha = int(input("Qual linha você quer atacar? "))
        while linha > 9 or linha < 0:
            print("Linha inválida!")
            linha = int(input("Qual linha você quer atacar? "))
        
        coluna = int(input("Qual coluna você quer atacar? "))
        while coluna > 9 or coluna < 0:
            print("Coluna inválida!")
            coluna = int(input("Qual coluna você quer atacar? "))

        coordenada = [{linha}, {coluna}]

        if coordenada in lista_coordenadas:
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
            resposta = False
        else:
            resposta = True
        

    lista_coordenadas.append(coordenada)

    
    tabuleiro = faz_jogada(posicao_oponente, linha, coluna)
    afundado = afundados(frota_oponente, tabuleiro)

    if afundado == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
