def tabuada (num):
    print(f"Tabuada do {num}:")
    for i in range (1, 11):
        print(f"{num} x {i} = {num * i}")

numero = int(input("Digite um núm. inteiro para ver sua tabuada: "))
tabuada(numero)

