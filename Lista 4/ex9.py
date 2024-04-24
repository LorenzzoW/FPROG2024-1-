
# Recebe o número de linhas do usuário
n = int(input("Entre com um número: "))

# Recebe o caractere do usuário
caracter = input("Entre com um caracter: ")

# Imprime o padrão de linhas
for i in range(1, n + 1):
    # Imprime o caractere i vezes
    print(caracter * i)