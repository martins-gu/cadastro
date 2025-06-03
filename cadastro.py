def menu():
    cadastro = []
    while True:
        print("\nSistema de Cadastro")
        print("[1] Cadastrar nome")
        print("[2]Listar nomes")
        print("[3] Excluir nome")
        print("[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            novo_nome = input("Digite o nome da pessoa:")
            cadastro.append(novo_nome)
            print(f"Usuario {novo_nome} foi adicionado !")
        elif opcao == '2':
            print("n\Lista de nomes cadastrados: ")
            for i, nome in enumerate(cadastro, start=1):
                print(f"{i}. {nome}")
        elif opcao == '3':
            excluir_nome = input("Digite o nome para excluir: ")
            if excluir_nome in cadastro:
                cadastro.remove(excluir_nome)
                print(f"{excluir_nome} foi removido.")
            else:
                print("Nome não encontrado.")
        if opcao == '0':
            print("Saindo...")
            break
        else:
            print("!!! Opção inválida. Tente novamente. !!! ")

menu()