import random

def exibir_tabuleiro(tabuleiro):
    print(tabuleiro[0] + ' | ' + tabuleiro[1] + ' | ' + tabuleiro[2])
    print('--+---+--')
    print(tabuleiro[3] + ' | ' + tabuleiro[4] + ' | ' + tabuleiro[5])
    print('--+---+--')
    print(tabuleiro[6] + ' | ' + tabuleiro[7] + ' | ' + tabuleiro[8])

def verificar_vitoria(tabuleiro, jogador):
    comb_ganhadoras = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
                       [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
                       [0, 4, 8], [2, 4, 6]]             # diagonais
    for comb in comb_ganhadoras:
        if tabuleiro[comb[0]] == tabuleiro[comb[1]] == tabuleiro[comb[2]] == jogador:
            return True
    return False

def jogada_aleatoria(tabuleiro):
    jogadas_disponiveis = [i for i in range(len(tabuleiro)) if tabuleiro[i] == ' ']
    return random.choice(jogadas_disponiveis)

def jogada_facil(tabuleiro):
    return jogada_aleatoria(tabuleiro)

def jogada_media(tabuleiro, jogador):
    # Verifica se a IA pode vencer em uma jogada
    for i in range(len(tabuleiro)):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = jogador
            if verificar_vitoria(tabuleiro, jogador):
                return i
            tabuleiro[i] = ' '

def jogada_dificil(tabuleiro):
    # Verifica se a IA pode vencer em uma jogada
    for i in range(len(tabuleiro)):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'O'
            if verificar_vitoria(tabuleiro, 'O'):
                return i
            tabuleiro[i] = ' '

    # Verifica se o jogador humano pode vencer em uma jogada e bloqueia
    for i in range(len(tabuleiro)):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'X'
            if verificar_vitoria(tabuleiro, 'X'):
                tabuleiro[i] = 'O'
                return i
            tabuleiro[i] = ' '

    # Escolhe o melhor movimento disponível usando o algoritmo de minimax
    melhor_pontuacao = float('-inf')
    melhor_jogada = None

    for i in range(len(tabuleiro)):
        if tabuleiro[i] == ' ':
            tabuleiro[i] = 'O'
            pontuacao = minimax(tabuleiro, 0, False)
            tabuleiro[i] = ' '

            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_jogada = i

    return melhor_jogada

def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vitoria(tabuleiro, 'O'):
        return 1
    elif verificar_vitoria(tabuleiro, 'X'):
        return -1
    elif ' ' not in tabuleiro:
        return 0

    if maximizando:
        melhor_pontuacao = float('-inf')
        for i in range(len(tabuleiro)):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = 'O'
                pontuacao = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = ' '
                melhor_pontuacao = max(melhor_pontuacao, pontuacao)
        return melhor_pontuacao
    else:
        melhor_pontuacao = float('inf')
        for i in range(len(tabuleiro)):
            if tabuleiro[i] == ' ':
                tabuleiro[i] = 'X'
                pontuacao = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = ' '
                melhor_pontuacao = min(melhor_pontuacao, pontuacao)
        return melhor_pontuacao

def jogar_jogo_da_velha(dificuldade):
    tabuleiro = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    jogador_atual = 'X'
    jogo_em_andamento = True

    while jogo_em_andamento:
        exibir_tabuleiro(tabuleiro)

        if jogador_atual == 'X':
            posicao = input("É a sua vez. Escolha uma posição de 1 a 9: ")
            posicao = int(posicao) - 1

            if tabuleiro[posicao] == ' ':
                tabuleiro[posicao] = jogador_atual

                if verificar_vitoria(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print("Parabéns! Você venceu!")
                    jogo_em_andamento = False
                elif ' ' not in tabuleiro:
                    exibir_tabuleiro(tabuleiro)
                    print("O jogo empatou!")
                    jogo_em_andamento = False
                else:
                    jogador_atual = 'O'
            else:
                print("Posição inválida. Tente novamente.")
        else:
            print("É a vez do jogador O (IA)")

            # Escolher uma jogada para a IA
            if dificuldade == 1:
                posicao = jogada_facil(tabuleiro)
            elif dificuldade == 2:
                posicao = jogada_media(tabuleiro, jogador_atual)
            elif dificuldade == 3:
                posicao = jogada_dificil(tabuleiro)
            else:
                print("Dificuldade inválida. Jogando como IA fácil.")
                posicao = jogada_facil(tabuleiro)

            tabuleiro[posicao] = jogador_atual

            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print("A IA venceu!")
                jogo_em_andamento = False
            elif ' ' not in tabuleiro:
                exibir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                jogo_em_andamento = False
            else:
                jogador_atual = 'X'

dificuldade = int(input("Escolha a dificuldade da IA (1 - Fácil, 2 - Média, 3 - Difícil): "))
jogar_jogo_da_velha(dificuldade)
