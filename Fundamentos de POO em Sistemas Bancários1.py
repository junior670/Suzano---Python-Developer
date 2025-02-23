''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"+{valor}")

    def sacar(self, valor):
        if self.saldo >= abs(valor):
            self.saldo += valor  # valor já é negativo
            self.operacoes.append(str(valor))
        else:
            self.operacoes.append("Saque não permitido")

    def extrato(self):
        print(f"Operações: {', '.join(self.operacoes)}; Saldo: {self.saldo}")

# Entrada de dados
nome_titular = input().strip()
conta = ContaBancaria(nome_titular)

entrada_transacoes = input().strip()
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Processamento das transações
for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)
    else:
        conta.sacar(valor)

# Exibição do extrato
conta.extrato()
