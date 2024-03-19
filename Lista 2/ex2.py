#Leitura da cotação de dólar
cotacao_dolar = float(input("Digite a cotação do dólar em reais:"))

#Leitura da quantidade de dólares
quantidade_dolares = float(input("Digite a quantidade de dólares que deseja comprar:"))

#Cálculo do valor total em reais
valor_total_reais = cotacao_dolar * quantidade_dolares

#Impressão do resultado
print(f"O valor total em reais que você precisará pagar é R${valor_total_reais:.2f}")