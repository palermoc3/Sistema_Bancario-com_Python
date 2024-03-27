class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.numero_saque = 0
    def extrato(self):
        return f"Seu saldo atual é: R$ {self.saldo}"

    def deposito(self, valor):
        self.saldo += valor
        return f"Depósito de R$ {valor} realizado com sucesso."

    def saque(self, valor):
        if valor > 500:
            return "Limite de saque excedido (máximo: R$ 500)"
        elif valor > self.saldo:
            return "Saldo insuficiente para saque."
        elif self.numero_saque > 3:
            return "Quantidade maxima de saques realizadas."
        else:
            self.saldo -= valor
            self.numero_saque +=1
            return f"Saque de R$ {valor} realizado com sucesso."


conta = ContaBancaria()

while True:
    print("\nEscolha a operação:")
    print("e - Extrato")
    print("d - Depósito")
    print("s - Saque")
    print("q - Sair")

    opcao = input("Escolha a opção (e/d/s/q): ")

    if opcao == 'e':
        print(conta.extrato())
    elif opcao == 'd':
        valor_deposito = float(input("Digite o valor do depósito: "))
        print(conta.deposito(valor_deposito))
    elif opcao == 's':
        valor_saque = float(input("Digite o valor do saque: "))
        print(conta.saque(valor_saque))
    elif opcao == 'q':
        break
