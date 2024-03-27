#Solicita ao usuário o valor desejado
valor = int(input("Digite o valor desejado em R$: "))

#Calcula a quantidade de notas de R$ 100
if valor >= 100:
    qtd_cedulas_100 = valor // 100
    print(f"{qtd_cedulas_100} nota(s) de R$ 100.")
    valor %= 100

#Calcula a quantidade de notas de R$ 50
if valor >= 50:
    qtd_cedulas_50 = valor // 50
    print(f"{qtd_cedulas_50} nota(s) de R$ 50.")
    valor %= 50

#Calcula a quantidade de notas de R$ 20
if valor >= 20:
    qtd_cedulas_20 = valor // 20
    print(f"{qtd_cedulas_20} nota(s) de R$ 20.")
    valor %= 20

#Calcula a quantidade de notas de R$ 10
if valor >= 10:
    qtd_cedulas_10 = valor // 10
    print(f"{qtd_cedulas_10} nota(s) de R$ 10.")
    valor %= 10

#Calcula a quantidade de notas de R$ 5
if valor >= 5:
    qtd_cedulas_5 = valor // 5
    print(f"{qtd_cedulas_5} nota(s) de R$ 5.")
    valor %= 5

#Imprime a quantidade de notas de R$ 1 restante
if valor > 0:
    print(f"{valor} nota(s) de R$ 1.")
