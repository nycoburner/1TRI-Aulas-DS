#importação da biblioteca
import random
# sorteio do número aleatorio
numero = random.randint(0,10)
tentativas = 1 
while (tentativas <= 3):
    print("Tentativas:", tentativas)
    chute = int(input("Digite um número de 0 a 10:"))
    if chute == numero:
        print("Parabéns! Vocé acertou!")
        break
    else:
        print("Errou e perdeu to seu dinheiro do tigrinho")
        tentativas = tentativas + 1 
        print("###FIM DE JOGO###")