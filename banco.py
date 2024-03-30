class ContaBancaria:
    def __init__(self, nome_usuario, saldo_inicial=0):
        self.nome_usuario = nome_usuario
        self.saldo = saldo_inicial
        self.historico = []

    def deposito(self, valor):
        self.saldo += valor
        self.historico.append(f"Depósito de R$ {valor}")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque de R$ {valor}")
        else:
            print("Saldo insuficiente para saque.")

    def extrato(self):
        print(f"Extrato para o usuário {self.nome_usuario}:")
        print(f"Saldo atual: R$ {self.saldo}")
        print("Histórico:")
        for operacao in self.historico:
            print("-", operacao)

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, nome_usuario, saldo_inicial=0):
        if nome_usuario not in self.contas:
            conta = ContaBancaria(nome_usuario, saldo_inicial)
            self.contas[nome_usuario] = conta
            print(f"Conta para o usuário {nome_usuario} criada com sucesso.")
        else:
            print("Este usuário já possui uma conta associada.")

# Função para interação com o usuário via terminal
def menu_principal():
    banco = Banco()

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Criar conta")
        print("2. Acessar conta")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_usuario = input("Digite o nome do usuário: ")
            saldo_inicial = 0.0
            banco.criar_conta(nome_usuario, saldo_inicial)
        elif opcao == "2":
            nome_usuario = input("Digite o nome do usuário: ")
            if nome_usuario in banco.contas:
                conta = banco.contas[nome_usuario]
                print(f"\n--- BEM-VINDO, {nome_usuario.upper()} ---")
                while True:
                    print("\n1. Depositar")
                    print("2. Sacar")
                    print("3. Extrato")
                    print("4. Voltar ao menu principal")

                    opcao_conta = input("Escolha uma opção: ")

                    if opcao_conta == "1":
                        valor_deposito = float(input("Digite o valor do depósito: "))
                        conta.deposito(valor_deposito)
                    elif opcao_conta == "2":
                        valor_saque = float(input("Digite o valor do saque: "))
                        conta.saque(valor_saque)
                    elif opcao_conta == "3":
                        conta.extrato()
                    elif opcao_conta == "4":
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
            else:
                print("Usuário não encontrado. Por favor, crie uma conta primeiro.")
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu_principal()
