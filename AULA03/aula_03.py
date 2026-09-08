from mod_rh import cadastrar_colaborador, exibir_colaboradores


lista_colaboradores = []


while True:
    print("\n===== SISTEMA DE RH =====")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do colaborador: ")
        cargo = input("Digite o cargo do colaborador: ")
        salario = float(input("Digite o salário do colaborador: "))

        colaborador = cadastrar_colaborador(nome, cargo, salario)
        lista_colaboradores.append(colaborador)

        print("\nColaborador cadastrado com sucesso!")

    elif opcao == "2":
        if len(lista_colaboradores) == 0:
            print("\nNenhum colaborador cadastrado.")
        else:
            print("\n===== COLABORADORES =====")
            exibir_colaboradores(lista_colaboradores)

    elif opcao == "0":
        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida. Tente novamente.")