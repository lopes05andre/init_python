import forca # importar o arquivo que contém o jogo da forca
import adivinhacao # importar o arquivo que contém o jogo da adivinhação

def escolhe_jogo():
    print("**********************************")
    print("Escolha o seu jogo!")
    print("**********************************")

    print("(1) Forca (2) Adivinhação)")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando FORCA")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando ADIVINHAÇÃO")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()