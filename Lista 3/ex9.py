# Solicita ao usuário as cotações das moedas
cotacao_real = float(input("Digite a cotação do Real em relação ao Euro: "))
cotacao_dolar = float(input("Digite a cotação do Dólar em relação ao Euro: "))

# Apresenta o menu
print("\nMenu:")
print("1) Converter de Real para Euro")
print("2) Converter de Real para Dólar")
print("3) Converter de Euro para Dólar")
print("4) Converter de Euro para Real")
print("5) Converter de Dólar para Euro")
print("6) Converter de Dólar para Real")

#Solicita ao usuário que escolha uma opção do menu
opcao = int(input("\nEscolha uma opção do menu: "))

#Conversão com base na opção escolhida
if opcao == 1:
    valor_real = float(input("Digite o valor em Real: "))
    valor_euro = valor_real / cotacao_real
    print("Valor em Euro:", valor_euro)
else:
    if opcao == 2:
        valor_real = float(input("Digite o valor em Real: "))
        valor_dolar = valor_real / cotacao_dolar
        print("Valor em Dólar:", valor_dolar)
    else:
        if opcao == 3:
            valor_euro = float(input("Digite o valor em Euro: "))
            valor_dolar = valor_euro * cotacao_dolar
            print("Valor em Dólar:", valor_dolar)
        else:
            if opcao == 4:
                valor_euro = float(input("Digite o valor em Euro: "))
                valor_real = valor_euro * cotacao_real
                print("Valor em Real:", valor_real)
            else:
                if opcao == 5:
                    valor_dolar = float(input("Digite o valor em Dólar: "))
                    valor_euro = valor_dolar / cotacao_dolar
                    print("Valor em Euro:", valor_euro)
                else:
                    valor_dolar = float(input("Digite o valor em Dólar: "))
                    valor_real = valor_dolar * cotacao_dolar
                    print("Valor em Real:", valor_real)
