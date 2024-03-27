#Solicita a idade do conveniado
idade_conveniado = int(input("Digite a idade do conveniado: "))

#Inicializa o valor base do plano
valor_plano = 300

#Verifica a faixa etária do conveniado e adiciona o valor correspondente
if idade_conveniado < 10:
    valor_plano += 100
else:
    if idade_conveniado <= 30:
        valor_plano += 220
    else:
        if idade_conveniado <= 60:
            valor_plano += 395
        else:
            valor_plano += 480

#Imprime o valor total a ser pago pelo plano de saúde
print("O valor a ser pago pelo plano de saúde é R$", valor_plano)
