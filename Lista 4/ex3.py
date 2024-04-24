while True:
    # Solicita um número ao usuário
    numero = int(input("Entre com um número (1 a 9): "))
    
    # Verifica se o número está no intervalo válido
    if 1 <= numero <= 9:
        # Exibe a tabuada de multiplicação do número
        print(f"Tabuada de multiplicação do {numero}:")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
        
        # Pergunta se o usuário deseja calcular outro número
        opcao = input("Calcular outro número (s/n)? ")
        
        # Se o usuário não quiser calcular outro número, sai do loop
        if opcao.lower() != 's':
            break
    else:
        print("Número fora do intervalo válido. Tente novamente.\n")
