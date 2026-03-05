# Menu de opções usando o terminal
while True:
    print("1 - opção 1")
    print("2 - opção 2")
    print("3 - opção 3")
    print("4 - opção 4")
    print("5- Sair 5")
    opção = input("Digite a opção que deseja(1 a 5)")

    if opção == "1":
        print("Selecionado opção 1!")
    elif opção == "2":
        print("Selecionado opção 2!!")
    elif opção == "3":
        print("Selecionado opção 3!!!")
    elif opção == "4":
        print("Selecionado opção 4!?!?")
    elif opção == "5":
        print("Você selecionou sair")
        break
    else:
        print("Ops! não existe está opção:p")

