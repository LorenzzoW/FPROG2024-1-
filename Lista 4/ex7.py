# Recebe os cinco nomes do usuário
nome1 = input("Informe o 1º nome: ")
nome2 = input("Informe o 2º nome: ")
nome3 = input("Informe o 3º nome: ")
nome4 = input("Informe o 4º nome: ")
nome5 = input("Informe o 5º nome: ")

# lista com os nomes
nomes = [nome1, nome2, nome3, nome4, nome5]

# Inicializa o primeiro nome em ordem alfabética com o primeiro nome da lista
primeiro_nome = nomes[0]

# Itera sobre os nomes da lista...
for nome in nomes:
    # Se o nome atual for menor que o primeiro nome em ordem alfabética
    if nome < primeiro_nome:
        # Atualiza o primeiro nome em ordem alfabética com o nome atual
        primeiro_nome = nome

# Imprime o primeiro nome em ordem alfabética
print("O primeiro nome em ordem alfabética é:", primeiro_nome)
