#Gestão e Controle de Transações Bancárias 1/2

''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

def calcular_saldo(transacoes):
    saldo = 0

    # Itera sobre cada transação na lista e adiciona ao saldo
    for transacao in transacoes:
        saldo += transacao

    # Retorna o saldo formatado em moeda brasileira com 2 casas decimais
    return f"Saldo: R$ {saldo:.2f}"

# Lê a entrada do usuário
entrada_usuario = input()

# Remove os caracteres indesejados e converte a string para uma lista de valores numéricos
entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")
transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# Calcula o saldo com base nas transações informadas
resultado = calcular_saldo(transacoes)

# Imprime o resultado
print(resultado)
