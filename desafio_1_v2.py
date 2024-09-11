from datetime import datetime

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[0] Sair

=> """

# Listas para armazenar usuários e contas
usuarios = []
contas = []
numero_conta_sequencial = 1
LIMITE_TRANSACOES = 10

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"Depósito: R$ {valor:.2f} em {data_hora}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso em {data_hora}.")
    else:
        print("Valor inválido para depósito. O valor deve ser maior que 0.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_transacoes, limite_transacoes):
    if numero_transacoes >= limite_transacoes:
        print("Você atingiu o número máximo de transações. Tente novamente amanhã.")
        return saldo, extrato

    if valor > saldo:
        print(f"Saldo insuficiente. Seu saldo atual é de R$ {saldo:.2f}.")
    elif valor > limite or valor <= 0:
        print("O valor permitido precisa ser maior que 0 e menor ou igual a R$ 500.00.")
    else:
        saldo -= valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"Saque: R$ {valor:.2f} em {data_hora}\n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso em {data_hora}.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n===== EXTRATO =====")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("====================\n")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ").strip()
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe um usuário cadastrado com este CPF.")
            return usuarios

    nome = input("Digite o nome: ").strip()
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ").strip()
    endereco = input("Digite o endereço (logradouro, nro bairro cidade/estado): ").strip()

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")
    return usuarios

def criar_conta_corrente(usuarios, contas, numero_conta_sequencial):
    cpf = input("Digite o CPF do usuário: ").strip()

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Usuário não encontrado. Verifique o CPF.")
        return contas, numero_conta_sequencial

    nova_conta = {
        "agencia": "0001",
        "numero_conta": numero_conta_sequencial,
        "usuario": usuario_encontrado
    }

    contas.append(nova_conta)
    numero_conta_sequencial += 1
    print(f"Conta criada com sucesso! Agência: 0001, Conta: {nova_conta['numero_conta']}")

    return contas, numero_conta_sequencial

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_transacoes = 0
    global contas  # Declaração de variável global
    global numero_conta_sequencial  # Declaração de variável global

    while True:
        opcao = input(menu)

        if opcao == "1":
            if numero_transacoes < LIMITE_TRANSACOES:
                valor_deposito = float(input("Digite o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor_deposito, extrato)
                numero_transacoes += 1
                print(f"Você já realizou {numero_transacoes} de {LIMITE_TRANSACOES} transações diárias.")
            else:
                print("Você atingiu o número máximo de transações. Tente novamente amanhã.")
        
        elif opcao == "2":
            if numero_transacoes < LIMITE_TRANSACOES:
                valor_saque = float(input("Digite o valor do saque: "))
                saldo, extrato = sacar(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_transacoes=numero_transacoes, limite_transacoes=LIMITE_TRANSACOES)
                numero_transacoes += 1
                print(f"Você já realizou {numero_transacoes} de {LIMITE_TRANSACOES} transações diárias.")
            else:
                print("Você atingiu o número máximo de transações. Tente novamente amanhã.")
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            contas, numero_conta_sequencial = criar_conta_corrente(usuarios, contas, numero_conta_sequencial)

        elif opcao == "0":
            print("Obrigado por utilizar nossos serviços!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
