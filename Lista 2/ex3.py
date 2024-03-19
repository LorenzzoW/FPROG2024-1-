#Definido o preço por quilo
preco_por_quilo = 40
#Leitura do peso do prato do cliente 
peso_prato = float(input("Digite o peso do prato em quilogramas:"))
#Cálculo do valor a ser pago
valor_a_pagar = preco_por_quilo * peso_prato
#Impressão do resultado
print(f"O valor a ser pago é: R${valor_a_pagar:.2f}")