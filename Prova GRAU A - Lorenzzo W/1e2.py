##############################################################################      

          #PROVA GRAU A EXERCÍCIOS 1 E 2 (jUNTOS): 

#divisível por 2:
def divisivelPor2(numero):
    return numero % 2 == 0

#verifica se um número é divisível por outro:
def divisivelPorN(numero, divisor):
    if divisor == 0:
        print("Não é possível dividir ele por zero...")
        return False
    return numero % divisor == 0

#pede paradigitar o número inteiro qualquer:
numero_t = int(input("Digite um número inteiro qualquer: "))

if divisivelPor2(numero_t):
    print(f"{numero_t} é divisível por 2 !! ")
    print("True")
else:
    print(f"{numero_t} não é divisível por 2...")
    print("False")

#Pede para digitar um divisor qualquer...
divisor_t = int(input("Agora, digite outro número inteiro como divisor: "))

if divisor_t == 0:
    print("Não é possível dividir por zero!")
else:
    if divisivelPorN(numero_t, divisor_t):
        print(f"{numero_t} é divisível por {divisor_t}.")
        print("True")
    else:
        print(f"{numero_t} não é divisível por {divisor_t}.")
        print("False")

##############################################################################