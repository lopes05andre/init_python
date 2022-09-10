import random

def jogar():

    print("**********************************")
    print("Bem-vindo no jogo de adivinhação!")
    print("**********************************")

    # variável para representar a rodada
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil)")

    # input irá devolver uma string e será convertido em int
    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # Laço de repetição
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
        # Solicita a entrada de dados para o usuário
        chute_str = input("Digite o seu número entre 1 e 100: ")
        # Converter a entrada do dado em Int
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        # A variável recebe o chute que, por sua vez, recebe o número secreto
        acertou = chute == numero_secreto
        # Maior recebe a variável chute que, por sua vez, recebe número secreto
        maior = chute > numero_secreto
        # Menor recebe a variável chute que, por sua vez, recebe número secreto
        menor = chute < numero_secreto
        # Se acertou, a verificação interrompe a checagem no break
        if (acertou):
            print("Você acertou e fez {} !".format(pontos))
            break
        else:
            if (maior):
                print("O seu chute foi maior do que o número secretp")
            elif (menor):
                print("O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)  # irá devolver um número absoluto
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")

# Permite a execução do arquivo pelo console de forma independente
if(__name__ == "__main__"):
    jogar()
