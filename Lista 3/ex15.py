# Solicita o preço normal de etiqueta do produto
preco_etiqueta = float(input("Digite o preço normal de etiqueta do produto: "))

# Solicita a condição de pagamento escolhida
condicao_pagamento = int(input("Escolha a condição de pagamento (1 - À vista em dinheiro, 2 - À vista no cartão de crédito, 3 - Em duas vezes, 4 - Em três vezes): "))

# Inicializa a variável para armazenar o valor a ser pago
valor_pago = 0

# Calcula o valor a ser pago de acordo com a condição de pagamento escolhida
if condicao_pagamento == 1:
    valor_pago = preco_etiqueta * 0.85  # 15% de desconto
if condicao_pagamento == 2:
    valor_pago = preco_etiqueta * 0.9  # 10% de desconto
if condicao_pagamento == 3:
    valor_pago = preco_etiqueta  # Preço normal em duas vezes
if condicao_pagamento == 4:
    valor_pago = preco_etiqueta * 1.1  # Preço normal mais 10% de juros em três vezes

# Imprime o valor a ser pago pelo produto
print("O valor a ser pago pelo produto é R$", valor_pago)
