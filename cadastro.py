def cadastrar_usuario(cadastro):
    try:
        novo_nome = input("Digite o nome da pessoa: ")
        if not novo_nome.strip():
            raise ValueError("O nome não pode estar vazio.")
        cadastro.append(novo_nome)
        print(f"Usuário {novo_nome} foi adicionado!")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def listar_usuario(cadastro): 
    print("--------------------------------")
    print("\nLista de nomes cadastrados:")
    if not cadastro:
        print("Nenhum usuário cadastrado.")
    else:
        for i, nome in enumerate(cadastro, start=1):
            print(f"{i}. {nome}")
    print("--------------------------------")

def excluir_usuario(cadastro):
    try:
        excluir_nome = input("Digite o nome para excluir: ")
        if not excluir_nome.strip():
            raise ValueError("O nome não pode estar vazio.")
        if excluir_nome in cadastro:
            cadastro.remove(excluir_nome)
            print(f"{excluir_nome} foi removido.")
        else:
            print("Nome não encontrado.")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def menu():
    cadastro = []
    while True:
        try:
            print("\nSistema de Cadastro")
            print("[1] Cadastrar nome")
            print("[2] Listar nomes")
            print("[3] Excluir nome")
            print("[0] Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                cadastrar_usuario(cadastro)
            elif opcao == '2':
                listar_usuario(cadastro)
            elif opcao == '3':
                excluir_usuario(cadastro)
            elif opcao == '0':
                print("Saindo...")
                break
            else:
                print("!!! Opção inválida. Tente novamente. !!!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

menu()