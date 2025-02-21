user = "Jesiel"
passd = "123"
saldo = 1500
op = -1  # Inicializa op para entrar no loop

print("BEM-VINDO AO BANCO EASYMONEY")
name = input("Digite seu nome:\n")
senha = input("Digite sua senha:\n")

if name == user and senha == passd: 
    print(f"Bem-vindo {user}, seu saldo é: R${saldo}")

    while op != 0:
        print("\nEscolha uma operação:")
        print("1 - Sacar Dinheiro")
        print("2 - Empréstimo")
        print("3 - Extrato")
        print("0 - Sair")
        reciver = input("Digite o número da operação desejada:\n")

        if reciver == "1":
            print(f"Você tem R${saldo} na sua conta.")
            sacar = input("Quanto deseja sacar?\n")

            if sacar.isdigit():  # Verifica se o valor digitado é um número
                sacar = int(sacar)
                if sacar > saldo:
                    print("Você não tem dinheiro suficiente!")    
                else:
                    saldo -= sacar
                    print(f"Você sacou R${sacar}. Agora seu saldo é R${saldo}.")
            else:
                print("Valor inválido! Digite um número.")

        elif reciver == "2":
            emprestimo = saldo * 2
            print(f"Você tem disponível um empréstimo de até R${emprestimo}.")

            yesoN = input("Você deseja retirar? Sim ou Não\n").strip().lower()

            if yesoN == "sim":
                empre1 = input("Digite o valor do empréstimo desejado:\n")

                if empre1.isdigit():
                    empre1 = int(empre1)

                    if empre1 > emprestimo:
                        print("\nVocê não pode pegar esse valor, pois passou do seu limite permitido.\n")
                    else:
                        saldo += empre1
                        print(f"\nEmpréstimo de R${empre1} concedido! Seu novo saldo é R${saldo}.\n")
                else:
                    print("Valor inválido! Digite um número.")
            else:
                print("Tudo bem, continue experimentando o nosso banco.")

        elif reciver == "3":
            print(f"Seu saldo atual é R${saldo}.")

        elif reciver == "0":
            print("Obrigado por utilizar o Banco EasyMoney! Até mais.")
            op = 0  # Atualiza op para sair do loop

        else:
            print("\nOpção não encontrada!\n")

else:
    print("Nome ou senha incorretos.")
