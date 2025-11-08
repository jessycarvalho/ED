sanduiche = []  
while True:   
        print("\n--Monte seu sanduíche!!!!--")
        print("1 - Adcionar ingrediente") 
        print("2 - Remover ingrediente") 
        print("3 - Mostrar último ingrediente") 
        print("4 - Ver sanduíche completo") 
        print("5 - Finalizar")   
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            item = input("Digite um ingrediente:")
            sanduiche.append(item)
            print(f" {item} foi adcionado ao topo do sanduíche!!")
        elif opcao == "2":
            if len(sanduiche) > 0:
                removido = sanduiche.pop()
                print(f"Você removeu {removido} do sanduíche")
            else:
                print("Sem ingredientes.")
        elif opcao == "3":
            if sanduiche: 
                print(f"Último ingrediente: {sanduiche[-1]}")
            else: 
                print("Sem ingredientes.")
        elif opcao == "4":
            if sanduiche:
                print("Veja como está ficando seu sanduíche!!") 
                for item in reversed(sanduiche):
                  print(f"-{item}")
            else:
                print("Sem ingredientes")
        elif opcao == "5":
            print("Seu sanduíche está pronto. Volte sempre!!")
            break
        else:
            print("Opção inválida. Tente novamente.") 



        
