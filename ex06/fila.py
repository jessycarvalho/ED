fila = []


while True: 
    print("----Fila!!!-----")
    print("1- Adicionar á fila")
    print("2- Mostrar lista")
    print("3- Remover cliente atendido")
    print("4- Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        nome = input("Insira seu nome:. Para encerrar, digite 'sair':")
        fila.append(nome)
        print(f"{nome} adcionado com sucesso")

    elif opcao == "2":
        print("Na fila: ", fila)
    elif opcao == "3":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"{atendido} já foi atendido.")
        else:    
            print("Fila vazia")
        
    elif opcao == "4":
        print("Encerrando....")
        break
    else:
        print("Opção inválida!! Tente novamente")


    


