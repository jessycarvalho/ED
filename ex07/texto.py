texto_atual = ""          
pilha_undo = []           
pilha_redo = []  
while True:
    print("\n--- MENU ---")
    print("1 - Digitar texto")
    print("2 - Desfazer (Undo)")
    print("3 - Refazer (Redo)")
    print("4 - Mostrar texto atual")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ") 

    if opcao == "1":
            novo_texto = input("Digite o novo texto: ")

            # Guarda o estado anterior antes de modificar
            pilha_undo.append(texto_atual)

            # Novo texto substitui o atual
            texto_atual = novo_texto

            # Ao digitar algo novo, o histórico de redo é limpo
            pilha_redo.clear()

            print("Texto atualizado!")

    elif opcao == "2":  # Desfazer
            if pilha_undo:
                pilha_redo.append(texto_atual)
                texto_atual = pilha_undo.pop()
                print("Desfazer realizado!")
            else:
                print("Nada para desfazer.")

    elif opcao == "3":  # Refazer
            if pilha_redo:
                pilha_undo.append(texto_atual)
                texto_atual = pilha_redo.pop()
                print("Refazer realizado!")
            else:
                print("Nada para refazer.")

    elif opcao == "4":
            print(f"\nTexto atual: {texto_atual}")

    elif opcao == "5":
            print("Saindo... Até mais!")
            break

    else:
            print("Opção inválida, tente novamente.")

