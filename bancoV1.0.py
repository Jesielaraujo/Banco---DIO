
user = "Jesiel"
passd = "123"
saldo = 1500
op = -1  # Inicializa a variável para entrar no loop

print("BEM-VINDO AO BANCO EASYMONEY")
name = input("Digite seu nome:\n")
senha = input("Digite sua senha:\n")

if name == user and senha == passd:
    print(f"Bem-vindo {user}, seu saldo é: R${saldo}")

    while op != "0":
        print("\nEscolha uma operação:")
        print("1 - Sacar Dinheiro")
        print("2 - Depósito")
        print("3 - Empréstimo")
        print("4 - Extrato")
        print("0 - Sair")
        
        op = input("\nDigite a opção desejada: ")

        #  Opção de SAQUE
        if op == "1":
            print(f"\nSeu saldo atual é R${saldo}")
            sacar = input("Quanto deseja sacar?\n")

            if sacar.isdigit():  # Verifica se é um número
                sacar = int(sacar)
                if sacar > saldo:
                    print("Você não tem dinheiro suficiente!")    
                else:
                    saldo -= sacar
                    print(f"Você sacou R${sacar}. Seu novo saldo é R${saldo}.")
            else:
                print("Valor inválido! Digite um número.")

        #  Opção de DEPÓSITO
        elif op == "2":
            deposito = input("\nQuanto deseja depositar?\n")

            if deposito.isdigit():
                deposito = int(deposito)
                saldo += deposito
                print(f"Você depositou R${deposito}. Seu novo saldo é R${saldo}.")
            else:
                print("Valor inválido! Digite um número.")

        #  Opção de EMPRÉSTIMO
        elif op == "3":
            emprestimo = saldo * 2
            print(f"\nVocê tem disponível um empréstimo de até R${emprestimo}.")
            
            yesoN = input("Você deseja retirar? (Sim ou Não)\n").strip().lower()
            
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

        #  Opção de EXTRATO
        elif op == "4":
            print(f"\nSeu saldo atual é R${saldo}.")

        # Opção de SAIR
        elif op == "0":
            print("Obrigado por usar o Banco EasyMoney! Até mais.")
            break  # Sai do loop

        else:
            print("\nOpção inválida! Tente novamente.")

else:
    print("Nome ou senha incorretos.")
