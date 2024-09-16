from datetime import datetime

# Constantes
LIMITE_TRANSACOES = 10

# Classes do Sistema

class Transacao:
    def __init__(self, valor):
        self.valor = valor
        self.data_hora = datetime.now()

    def registrar(self, conta):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

class Deposito(Transacao):
    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(self)
        else:
            print("Saldo insuficiente para realizar o saque.")

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, numero, cliente, agencia="0001"):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0.0
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo

    def realizar_transacao(self, transacao):
        transacao.registrar(self)

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Funções de Transação

def depositar(conta, valor):
    if valor > 0:
        deposito = Deposito(valor)
        conta.realizar_transacao(deposito)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido para depósito.")

def sacar(conta, valor):
    if valor > 0 and valor <= 500:
        saque = Saque(valor)
        conta.realizar_transacao(saque)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido ou maior que o limite de R$ 500.")

def exibir_extrato(conta):
    print("\n===== EXTRATO =====")
    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta.historico.transacoes:
            tipo = "Depósito" if isinstance(transacao, Deposito) else "Saque"
            print(f"{tipo}: R$ {transacao.valor:.2f} em {transacao.data_hora.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"\nSaldo atual: R$ {conta.saldo_atual():.2f}")
    print("====================\n")

# Funções de Cadastro

def criar_usuario(clientes):
    cpf = input("Digite o CPF (somente números): ").strip()
    for cliente in clientes:
        if cliente.cpf == cpf:
            print("Já existe um cliente cadastrado com este CPF.")
            return None

    nome = input("Digite o nome: ").strip()
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ").strip()
    endereco = input("Digite o endereço (logradouro, nro bairro cidade/estado): ").strip()
    
    novo_cliente = Cliente(nome, data_nascimento, cpf, endereco)
    print("Usuário cadastrado com sucesso!")
    return novo_cliente

def criar_conta_corrente(cliente, numero_conta_sequencial):
    nova_conta = Conta(numero=numero_conta_sequencial, cliente=cliente)
    cliente.adicionar_conta(nova_conta)
    print(f"Conta criada com sucesso! Agência: {nova_conta.agencia}, Conta: {nova_conta.numero}")
    return nova_conta

# Sistema Principal

def main():
    clientes = []
    contas = []
    numero_conta_sequencial = 1
    
    while True:
        opcao = input(menu)

        if opcao == "1":  # Depositar
            cpf = input("Digite o CPF do cliente: ").strip()
            cliente_encontrado = next((cliente for cliente in clientes if cliente.cpf == cpf), None)

            if cliente_encontrado and cliente_encontrado.contas:
                valor_deposito = float(input("Digite o valor do depósito: "))
                depositar(cliente_encontrado.contas[0], valor_deposito)
            else:
                print("Cliente ou conta não encontrado.")

        elif opcao == "2":  # Sacar
            cpf = input("Digite o CPF do cliente: ").strip()
            cliente_encontrado = next((cliente for cliente in clientes if cliente.cpf == cpf), None)

            if cliente_encontrado and cliente_encontrado.contas:
                valor_saque = float(input("Digite o valor do saque: "))
                sacar(cliente_encontrado.contas[0], valor_saque)
            else:
                print("Cliente ou conta não encontrado.")

        elif opcao == "3":  # Exibir Extrato
            cpf = input("Digite o CPF do cliente: ").strip()
            cliente_encontrado = next((cliente for cliente in clientes if cliente.cpf == cpf), None)

            if cliente_encontrado and cliente_encontrado.contas:
                exibir_extrato(cliente_encontrado.contas[0])
            else:
                print("Cliente ou conta não encontrado.")

        elif opcao == "4":  # Criar Usuário
            novo_cliente = criar_usuario(clientes)
            if novo_cliente:
                clientes.append(novo_cliente)

        elif opcao == "5":  # Criar Conta Corrente
            cpf = input("Digite o CPF do cliente: ").strip()
            cliente_encontrado = next((cliente for cliente in clientes if cliente.cpf == cpf), None)

            if cliente_encontrado:
                nova_conta = criar_conta_corrente(cliente_encontrado, numero_conta_sequencial)
                contas.append(nova_conta)
                numero_conta_sequencial += 1
            else:
                print("Cliente não encontrado. Cadastre o cliente antes de criar uma conta.")

        elif opcao == "0":  # Sair
            print("Obrigado por utilizar nossos serviços!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta Corrente
    [0] Sair

    => """
    main()
