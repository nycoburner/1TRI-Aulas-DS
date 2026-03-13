palavra = "KENNEDY"
letrasAcertadas = ["_","_","_","_","_","_","_"]
acertou = False

def mostrar_letras_acertadas():
    for letra in letrasAcertadas:
        print(letra, end=" ")

print("Letras acertadas:")

print("Tente advinha adivinhar a palavra secreta: ")
while (not acertou):
    mostrar_letras_acertadas()

    print(" ")
    chute = input("Digite uma letra: ")
    indice = 0
    for letra in palavra:
        if chute.upper() == letra:
            letrasAcertadas [indice] = letra
        indice = indice +1
    if letrasAcertadas.count("_") == 0:
        print("Parabens, você acertou!")
        mostrar_letras_acertadas()
        acertou = True
