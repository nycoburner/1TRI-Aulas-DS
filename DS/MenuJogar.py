
   
opcao = int(input("Digite a opção desejada:"))
import advinhacao3
import forca3

if opcao == 1:
    advinhacao3.jogar()
elif opcao == 2:
    forca3.jogar()
else:
    print("Opção inválida")