#Valor dos eletrônicos
valor_smartphone = 1000.00
valo_tablets = 1500.00

#Número de smartphones e tablets vendidos em um dia
num_smartphones = float(input("Quantidade de smarthphones vendidos no dia:"))
num_tablets = float(input("Quantidade de tablets vendidos no dia:"))

#Valor arrecadado no fim do dia
total_arrecadado = (num_smartphones * valor_smartphone) + (num_tablets * valo_tablets)

#Resultado
print(f"O total arrecadado com a venda dos smartphones e tablets é: R$ {total_arrecadado:.2f}")