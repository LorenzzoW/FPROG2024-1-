#Lendo o número
numero = float(input("Digite um número: "))

#Verificando se o número é positivo ou negativo
if numero > 0:
    resultado = numero * 2  # Se for positivo, calcula o dobro
    print("O dobro do número é:", resultado)
else:
    resultado = numero * 3  # Se for negativo ou zero, calcula o triplo
    print("O triplo do número é:", resultado)