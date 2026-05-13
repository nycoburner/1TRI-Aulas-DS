
print("1 - Facil")
print("2 - Medium")
print("3 - Dificil")
opção = input("Digite a opção que deseja(1 a 3)")
if opção == "1":
    print("Selecionado opção 1!")
    tentativas_max = 5
    sorteio_max = 10

elif opção == "2":
    print("Selecionado opção 2!!")
    tentativas_max = 3
    sorteio_max = 10
    
elif opção == "3":
    print("Selecionado opção 3!!!")
    tentativas_max = 10
    sorteio_max = 100
    
else:
    print("Ops! não existe está opção:p")

import random

def jogar():
    # Configurações do jogo
    tentativas = 1
    errou = True
    numero = random.randint(0,sorteio_max)
        
        
        

    while (tentativas <= tentativas_max):
        print("Tentativa:", tentativas)
        chute = int(input(f"Digite o seu chute (0 a {sorteio_max})"))
        if chute == numero:
            print("Parabéns, você é o bonzão mesmo")
            errou = False
            break
        else:
            print("Errou :c")
            if chute > numero:
                print("O numero sorteado é menor")
            else:
                print("O numero sorteado é maior")
        tentativas = tentativas + 1
        
    if errou == True:
        print("O número sorteado era:", numero) # mostra p quem errou
    print("### FIM DO JOGO ###")

if (__name__ == "__main__"):
    jogar()