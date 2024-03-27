#Lendo os valor de A, B e C
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

#Verificando se a soma de A+B é menor do que A+C
if  a + b < a + c:
    print("A soma de A + B é menor que A + C.")

else:
    print("A soma de A + B não é menor que A + C.")