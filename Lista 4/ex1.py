#A) Gerar e escrever todos os números inteiros do intervalo [0,100] #

print("Números inteiros do intervalo [0,100]")
for i in range (101):
    print(i, end=" ")
print("\n")

#B) Gerar e escrever os números pares do intervalo [20,50] #

print("Números pares do intervalo [20,50]")
for i in range (20, 51, 2):
    print(i, end=" ")
print("\n")

#C) Gerar e escrever os números inteiros do intervalo [25,70] em ordem decrescente #

print("Números inteiros do intervalo [25,70]")
for i in range [70, 24, -1]:
    print(i, end=" ")
print("\n")

#D) Gerar e escrever os números ímpares do intervalo [25,95] em ordem decrescente #

print("Números ímpares do intervalo [25,95] em ordem decrescente:")
for i in range(95, 24, -1):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")

#E) Ler 15 números e escrever a soma e a média dos números lidos #

soma = 0
for _ in range(15):
    num = float(input("Digite um número: "))
    soma += num

media = soma / 15
print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}\n")

#F) Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números ímpares lidos #

pares = 0
impares = 0

for _ in range(10):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}\n")

#G) Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem “POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso. No final, imprimir a quantidade de números positivos e negativos lidos#

import random

positivos = 0
negativos = 0

print("Números sorteados com seus respectivos sinais:")
for _ in range(20):
    num = random.randint(-10, 10)
    if num > 0:
        print(f"{num} POSITIVO")
        positivos += 1
    elif num < 0:
        print(f"{num} NEGATIVO")
        negativos += 1
    else:
        print(f"{num} NULO")

print(f"\nQuantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}\n")

#H) Ler n números e imprimir no final a soma dos números lidos #

n = int(input("Quantos números você deseja ler? "))
soma = 0

for _ in range(n):
    num = float(input("Digite um número: "))
    soma += num

print(f"Soma dos {n} números lidos: {soma}")
