import adivinhacao as adivinhacao
import forca as forca
import roletarussa as roletarussa
def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3) Russian Roulette")

    jogo = int(input("Qual jogo você quer?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    elif(jogo == 3):
        print("Jogando Russian Roulette")
        roletarussa.jogar()

if(__name__ == "__main__"):
        escolhe_jogo()