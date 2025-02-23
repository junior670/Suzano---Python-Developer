''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f"{self.titular}: R$ {self.saldo}"


class SistemaBancario:
    def __init__(self):
        self.contas = []  # Inicializa a lista de contas

    def criar_conta(self, titular, saldo):
        conta = ContaBancaria(titular, saldo)  # Cria uma nova conta
        self.contas.append(conta)  # Adiciona à lista de contas

    def listar_contas(self):
        print(", ".join(str(conta) for conta in self.contas))  # Lista todas as contas


# Criando uma instância do sistema bancário
sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()
