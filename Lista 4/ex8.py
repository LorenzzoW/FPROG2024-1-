
while True:
    # Recebe um número do usuário
    numero = int(input("Digite um número: "))

    # Inicializa o fatorial com 1
    fatorial = 1

    # Calcula o fatorial do número
    for i in range(1, numero + 1):
        fatorial = fatorial * i

    # Imprime o fatorial do número
    print("O fatorial de", numero, "é", fatorial)

    # Pergunta ao usuário se deseja calcular outro número
    resposta = input("Quer calcular outro número? (s/n) ")

    # Se a resposta for "n", sai do loop
    if resposta == "n":
        break