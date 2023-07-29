menu = """
_____ Sistema Bancário _____

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo_conta = 0
limite_diario = 500
extrato_conta = ""
nro_saques_conta = 0
LIMITE_SAQUES_CONTA = 3




while True:

    opcao_menu = int(input(menu))

    if opcao_menu == 1:
        valor_deposito = float(input("Valor do Depósito: "))
        if valor_deposito > 0:
            saldo_conta += valor_deposito
            extrato_conta += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print("Valor incorreto para depósito!")

    elif opcao_menu == 2:
        valor_saque = float(input("Valor do Saque: "))
                            
        if valor_saque > saldo_conta:
            print("Falha na operação! Não tem saldo.")

        elif valor_saque > limite_diario:
            print("Falha na operação! Saque excedeu o limite diário.") 

        elif nro_saques_conta >= LIMITE_SAQUES_CONTA:
            print ("Falha na operação! Número máximo de saques excedido.")

        elif valor_saque > 0:
            saldo_conta -= valor_saque
            extrato_conta += f"Saque: R$ {valor_saque:.2f}\n"
            nro_saques_conta += 1
        
        else:
            print("Falha na Operação! Valor inválido.")
    
    elif opcao_menu == 3:
        print("\n____________Extrato da Conta____________")
        print("Sem movimentações na conta" if not extrato_conta else extrato_conta)
        print(f"Saldo R$: {saldo_conta:.2f}")
        print("________________________________________")
        

    elif opcao_menu == 4:
        break

    else:
        print("Operação selecionada inválida!!!")


