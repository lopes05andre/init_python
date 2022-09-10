import random

def jogar():
    # Executa a função para carregar a mensagem de abertura
    imprime_mensagem_abertura()
    # Executa a função para carregar a palabra secreta
    palavra_secreta = carrega_palavra_secreta()
    # Executa a função que inicializa a palavra secreta
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        # Executa a função que solicita o chute ao usuário
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

# Função que imprime a mensagem ao vencedor
def imprime_mensagem_vencedor():
    print("Você ganhou!")

# Função que imprime a mensagem ao perdedor
def imprime_mensagem_perdedor():
    print("Você perdeu!")

# Função que trata o chute, letras_acertadas e palavra_secreta
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    # Laço de repetição
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1

# Função que pede o chute ao usuário
def pede_chute():
    chute = input("Qual letra? ")
    # Trata a palavra que contém espaços vazios
    chute = chute.strip().upper()
    return chute

# Função que imprime a mensagem de abertura dos jogos
def imprime_mensagem_abertura():
    print("**********************************")
    print("Bem-vindo no jogo dda FORCA!")
    print("**********************************")

def carrega_palavra_secreta():
    # Abrir um arquivo em modo de leitura
    arquivo = open("palavras.txt", "r")
    # Inicializar a variável
    palavras = []
    # Laço de repetição dentro do arquivo
    for linha in arquivo:
        # Remover espaços vazios
        linha = linha.strip()
        # Variável palavra recebe as linhas do laço de repetição
        palavras.append(linha)
    # Fechar a leitura do arquivo
    arquivo.close()
    # Variável irá receber um número aleatório contido em palavras
    numero = random.randrange(0, len(palavras))
    # Variável irá receber palavras contendo o tamanho da leitura
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

# Permite a execução do arquivo pelo console de forma independente
if(__name__ == "__main__"):
    jogar()
