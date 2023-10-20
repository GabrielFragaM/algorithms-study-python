# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

# Função para verificar se alguém ganhou
def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

# Função para verificar se o tabuleiro está cheio
def tabuleiro_cheio(tabuleiro):
    return all(casa != " " for linha in tabuleiro for casa in linha)

# Função para calcular o resultado do jogo com o algoritmo Minimax
def minimax(tabuleiro, profundidade, maximizando):
    # Define os jogadores
    jogador_max = "X"
    jogador_min = "O"

    # Verifica o estado atual do jogo
    if verificar_vitoria(tabuleiro, jogador_max):
        return 1
    if verificar_vitoria(tabuleiro, jogador_min):
        return -1
    if tabuleiro_cheio(tabuleiro):
        return 0

    if maximizando:
        melhor_pontuacao = -float("inf")
        for linha in range(3):
            for coluna in range(3):
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador_max
                    pontuacao = minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[linha][coluna] = " "
                    melhor_pontuacao = max(pontuacao, melhor_pontuacao)
        return melhor_pontuacao
    else:
        melhor_pontuacao = float("inf")
        for linha in range(3):
            for coluna in range(3):
                if tabuleiro[linha][coluna] == " ":
                    tabuleiro[linha][coluna] = jogador_min
                    pontuacao = minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[linha][coluna] = " "
                    melhor_pontuacao = min(pontuacao, melhor_pontuacao)
        return melhor_pontuacao

# Função para escolher a melhor jogada usando o algoritmo Minimax
def melhor_jogada(tabuleiro):
    melhor_pontuacao = -float("inf")
    melhor_jogada = None

    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = "X"
                pontuacao = minimax(tabuleiro, 0, False)
                tabuleiro[linha][coluna] = " "
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_jogada = (linha, coluna)

    return melhor_jogada

# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        if jogador_atual == "X":
            linha, coluna = map(int, input("Digite a linha e coluna para a sua jogada (ex: 1 2): ").split())
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = "X"
                jogador_atual = "O"
        else:
            print("Computador está pensando...")
            linha, coluna = melhor_jogada(tabuleiro)
            tabuleiro[linha][coluna] = "O"
            jogador_atual = "X"

        if verificar_vitoria(tabuleiro, "X"):
            exibir_tabuleiro(tabuleiro)
            print("Você venceu!")
            break
        elif verificar_vitoria(tabuleiro, "O"):
            exibir_tabuleiro(tabuleiro)
            print("O computador venceu!")
            break
        elif tabuleiro_cheio(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

jogo_da_velha()