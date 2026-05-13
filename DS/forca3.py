import random
def jogar():
    palavras = []

    print("1-Advinhe os Jogo!")
    print("2-Advinhe os Animais!")
    print("3-Advinhe os Animes!")
    opcao = input("Digite a opção desejada(1 a 3)")
    if opcao == "1":
        arquivo = open("forca_jogos.txt", "r")
    elif opcao =="2":
        arquivo = open("forca_animais.txt", "r")
    elif opcao == "3":
        arquivo = open("forca_anime.txt", "r")
    else:
        print("opção invalida, selecionado opção jogo")
        arquivo = open("forca_anime.txt", "r")
    for linha in arquivo:
        palavras.append(linha.strip())
    
    palavra = random.choice(palavras)
    palavra = palavra.upper()
    letras_acertadas = []
    for letra in palavra:
        if letra == " ":
            letras_acertadas.append("-")
        else: 
            letras_acertadas.append("_")    

    acertou = False
    enforcou = False
    limite_tentativas = len(palavra) + 6
    tentativa = 1

    def mostrar_letras_acertadas():
        for letra in letras_acertadas:
            print(letra, end=" ")

    print("Tente adivinhar a palavra secreta: ")
    while(not acertou and not enforcou):
        # mostrar as letras acertadas
        mostrar_letras_acertadas()
        
        print("")
        chute = input("Digite uma letra: ")
        indice = 0

        for letra in palavra:
            if chute.upper() == letra:
                letras_acertadas[indice] = letra
            indice = indice + 1

        if tentativa == limite_tentativas:
            print ("você perdeu :( A palavra era ", palavra)
            enforcou = True

        if letras_acertadas.count("_") == 0:
            print("Parabéns, você acertou a palavra secreta!")
            mostrar_letras_acertadas()
            acertou = True
        tentativa = (tentativa + 1)

        

if (__name__ == "__main__"):
    jogar()