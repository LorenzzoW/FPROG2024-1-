# Solicita o valor do divisor ao usuário
divisor = int(input("Entre com o valor do divisor: "))

# Solicita o valor inicial do intervalo
inicio_intervalo = int(input("Início do intervalo: "))

# Solicita o valor final do intervalo
final_intervalo = int(input("Final do intervalo: "))

print(f"Números divisíveis por {divisor} no intervalo de {inicio_intervalo} a {final_intervalo}:")
for i in range(inicio_intervalo, final_intervalo + 1):
    if i % divisor == 0:
        print(i, end=" ")
print()
