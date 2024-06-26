menu = """

[d] Depositar 
[S] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor que você vai depositar por favor: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor: .2f}\n"
        else:
            print("A sua Operação não pode ser concluída! O valor que você informou é inválido.")


    elif opcao == "S":
        valor = float(input("Informe o valor que você deseja sacar: "))

        excedeu_saldo = valor > saldo
        
        execedeu_limite = valor > limite

        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("A sua operação não pode ser concluída! Você não tem saldo suficiente.")

        elif execedeu_limite:
            print("A sua operação não pode ser concluída! O valor do eu saque excede o seu limite.")

        elif execedeu_saques:
            print("A sua operação nao poder ser concluída! O numero de saques maximo foi ecedido.")

        elif valor >0:
            saldo -= valor
            extrato += f"saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("A sua operação não pode ser concluída! O valor que você informou é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Nenhuma movimentação foi realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Opção selecionada inválida, por favor selecione novamente a opção desejada.")





