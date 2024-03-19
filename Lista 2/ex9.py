#valor da compra
valor_compra = float(input("Digite o valor da compra: "))

#valor do desconto (quinze por cento)
desconto = valor_compra * 0.15

#valor da compra com desconto
valor_com_desconto = valor_compra - desconto

#resultado
print(f"O valor da compra com desconto é: R$ {valor_com_desconto:.2f}")