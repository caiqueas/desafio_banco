from datetime import date, datetime, time

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_transacoes = 0
LIMITE_TRANSACOES = 10

while True:

    opcao = input(menu)

    if opcao == "1":
        if numero_transacoes >= LIMITE_TRANSACOES:  # Verifica se o número máximo de transações foi atingido
            print("Você atingiu o número máximo de transações. Tente novamente amanhã.")
        else:
            valor_deposito = float(input("Digite o valor do depósito: "))
            
            if valor_deposito > 0:
                saldo += valor_deposito

                # Pega a data e hora da transação
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                # Adiciona ao extrato com a data e hora
                extrato += f"Depósito: R$ {valor_deposito:.2f} em {data_hora}\n"
                print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso em {data_hora}.")
                
                numero_transacoes += 1  # Incrementa o contador de transações
                print(f"Você já realizou {numero_transacoes} de {LIMITE_TRANSACOES} transações diárias.")
            else:
                print("Valor inválido para depósito. O valor deve ser maior que 0.")

    elif opcao == "2":
        if numero_transacoes >= LIMITE_TRANSACOES:  # Verifica se o número máximo de transações foi atingido
            print("Você atingiu o número máximo de transações. Tente novamente amanhã.")
        else:
            valor_saque = float(input("Digite o valor do saque: "))

            # Verifica se o valor é maior que o limite, menor ou igual a 0, ou maior que o saldo disponível
            while valor_saque > limite or valor_saque <= 0 or valor_saque > saldo:
                if valor_saque > saldo:
                    print(f"\nSaldo insuficiente. Seu saldo atual é de R$ {saldo:.2f}.\n")
                else:
                    print("\nO valor mínimo permitido precisa ser maior que R$0 e o valor máximo permitido é de R$ 500.00. \nPor favor, digite novamente.\n")
                
                valor_saque = float(input("Digite o valor do saque: "))

            saldo -= valor_saque  # Realiza o saque
            
            # Pega a data e hora da transação
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            # Adiciona ao extrato com a data e hora
            extrato += f"Saque: R$ {valor_saque:.2f} em {data_hora}\n"

            numero_transacoes += 1  # Incrementa o contador de transações

            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso em {data_hora}.")
            print(f"Você já realizou {numero_transacoes} de {LIMITE_TRANSACOES} transações diárias.")

    elif opcao == "3":
        print("\n===== EXTRATO =====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("====================\n")

    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
