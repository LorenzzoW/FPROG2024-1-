#Solicitando entrada do usuário para os números
dividendo = float(input("Digite o dividendo: "))
divisor = float(input("Digite o divisor: "))

#Verificando se o divisor é diferente de zero antes de efetuar a divisão

if divisor != 0:
    resultado = dividendo / divisor
    print("O resultado da divisão é:", resultado) 

else:
    print("Erro: Divisão por zero não é permitida.")  
