def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Erro: Divisão por zero!")
        return None

def menu():
    print("Calculadora Simples")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

def main():
    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 0:
            print("Saindo...")
            break
        elif opcao >= 1 and opcao <= 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == 1:
                print("Resultado da soma:", somar(num1, num2))
            elif opcao == 2:
                print("Resultado da subtração:", subtrair(num1, num2))
            elif opcao == 3:
                print("Resultado da multiplicação:", multiplicar(num1, num2))
            elif opcao == 4:
                resultado = dividir(num1, num2)
                if resultado is not None:
                    print("Resultado da divisão:", resultado)
        else:
            print("Opção inválida! Escolha uma opção válida.")

if __name__ == "__main__":
    main()
