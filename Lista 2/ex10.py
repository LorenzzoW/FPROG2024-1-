# Definindo os preços dos produtos
preco_camiseta = 25.00
preco_calca = 100.00
preco_cinto = 40.00

# Leitura da quantidade de camisetas, calças e cintos comprados
num_camisetas = int(input("Digite o número de camisetas compradas: "))
num_calcas = int(input("Digite o número de calças compradas: "))
num_cintos = int(input("Digite o número de cintos comprados: "))

# Calculando o total da compra
total_compra = (num_camisetas * preco_camiseta) + (num_calcas * preco_calca) + (num_cintos * preco_cinto)

# Calculando o valor do desconto (10% sobre o total da compra)
desconto = total_compra * 0.10

# Calculando o valor final com desconto
valor_final = total_compra - desconto

# Exibindo na tela o valor do desconto e o valor da compra com desconto
print(f"O valor do desconto é: R$ {desconto:.2f}")
print(f"O valor da compra com desconto é: R$ {valor_final:.2f}")
