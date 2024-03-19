#Preço do litro da gasolina
preco_no_litro_da_gasolina = float(input("Digite o preço do litro da gasolina: "))

#Valor disponivel para abastecer
valor_disponivel = float(input("Digite o valor disponivel para abastecer: "))

#Cálculo da quantidade de litros que o motorista pode colocar no tanque
litros_abastecidos = valor_disponivel / preco_no_litro_da_gasolina

#Resultado
print(f"O motorista pode colocar {litros_abastecidos:.2f} litros no tanque.")