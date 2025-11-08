fila = []  

while True:
        print("\n=====☆BEM VINDO AO NOSSO CHAT!!!!☆=====")
        print("1 - Enviar mensagem")
        print("2 - Ler última mensagem")
        print("3 - Abrir chat")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            usuario = input("Nome de usuário: ")
            texto = input("Mensagem: ")
            mensagem = {"usuario": usuario, "texto": texto}
            fila.append(mensagem)  # adiciona no fim da fila
            print("Mensagem enviada!")

        elif opcao == '2':
            if len(fila) == 0:
                print("Nenhuma mensagem na fila.")
            else:
                msg = fila.pop(0)  # remove do início da fila
                print(f"\n📨 {msg['usuario']} diz: {msg['texto']}")

        elif opcao == '3':
            if len(fila) == 0:
                print("Nenhuma mensagem na fila.")
            else:
                print("\nMensagens na fila:")
                for i, msg in enumerate(fila, start=1):
                    print(f"{i}. {msg['usuario']}: {msg['texto']}")

        elif opcao == '0':
            print("Encerrando chat... Até breve!!")
            break

        else:
            print("Opção inválida, tente novamente.")