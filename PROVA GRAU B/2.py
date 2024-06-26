######{ - PROVA GRAU B - Lorenzzo Willian - }######
#2)

import random

def gerarToupeiras():
    #Vai iniciar a matriz 4x4 com bur. vazios "-" 
    matriz = [["-" for _ in range(4)] for _ in range(4)]
    
    #Adiciona 4 toupeiras em posições aleatórias...
    toupeiras_colocadas = 0
    while toupeiras_colocadas < 4:
        i = random.randint(0, 3)
        j = random.randint(0, 3)
        if matriz[i][j] == "-":
            matriz[i][j] = "T"
            toupeiras_colocadas += 1
    
    return matriz

def imprimirMatriz(matriz, geracao):
    print(f"Geração {geracao}:")
    for linha in matriz:
        print(" ".join(linha))
    print()

#Gera e imprime 3 gerações de matrizes com as toperas
for geracao in range(1, 4):
    matriz = gerarToupeiras()
    imprimirMatriz(matriz, geracao)

##################################################

#(👍≖‿‿≖)👍 | 👍(≖‿‿≖👍)